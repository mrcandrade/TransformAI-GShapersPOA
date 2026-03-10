"""
AgentOS - Agente Avaliador da Prova TransformAI
================================================

Este servidor expoe o agente avaliador via API REST.
Execute com: fastapi dev prova_agent.py

Endpoints disponiveis em: http://localhost:8000/docs
UI do AgentOS: https://os.agno.com (conecte ao localhost:8000)
"""

import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.os import AgentOS
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURACAO - Carrega variaveis do .env
# ═══════════════════════════════════════════════════════════════════════════
load_dotenv()

# Verifica se a chave existe
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY nao encontrada! Crie um arquivo .env com sua chave.")

MODEL_ID = "llama-3.3-70b-versatile"

# ═══════════════════════════════════════════════════════════════════════════
# INSTRUCOES DO AGENTE AVALIADOR
# ═══════════════════════════════════════════════════════════════════════════
INSTRUCOES_AVALIADOR = """
Voce e o Professor Avaliador da prova TransformAI - Global Shapers Porto Alegre.
Sua funcao e avaliar respostas de alunos sobre conceitos de Inteligencia Artificial.

TOPICOS DA PROVA:
1. Tokens - unidades de texto, custo de APIs
2. Prompt Engineering - tecnicas para melhorar prompts (Persona, CoT, Few-Shot, Restricoes, XML Tags)
3. Temperatura - parametro de criatividade (0 = deterministico, alto = criativo)
4. Alucinacoes - quando a IA inventa informacoes falsas
5. Etica e Vies - preconceitos nos dados de treinamento

COMO AVALIAR:
Quando receber uma questao e resposta do aluno, voce deve:
1. Analisar se a resposta esta correta, parcialmente correta ou incorreta
2. Dar uma nota de 0 a 10
3. Explicar o que estava certo e o que faltou
4. Dar uma dica de como melhorar (se aplicavel)

FORMATO DE RESPOSTA:
Sempre responda em JSON valido:
{
    "nota": <numero de 0 a 10>,
    "status": "correta" | "parcial" | "incorreta",
    "feedback": "<explicacao do que estava certo/errado>",
    "dica": "<sugestao de melhoria ou null se perfeito>"
}

POSTURA:
- Seja encorajador mas honesto
- O objetivo e que o aluno aprenda
- Nao seja muito rigido, valorize o esforco
- Mas tambem nao dê nota alta para respostas vagas
"""

# ═══════════════════════════════════════════════════════════════════════════
# DEFINICAO DOS AGENTES
# ═══════════════════════════════════════════════════════════════════════════

# Agente principal: Avaliador de Prova
avaliador_prova = Agent(
    name="Professor Avaliador",
    description="Avalia respostas de alunos na prova sobre IA",
    model=Groq(id=MODEL_ID),
    instructions=INSTRUCOES_AVALIADOR,
    db=SqliteDb(db_file="prova_sessions.db"),  # Armazena sessoes dos alunos
    add_datetime_to_context=True,
    add_history_to_context=True,  # Lembra das questoes anteriores
    num_history_runs=10,  # Ultimas 10 interacoes
    markdown=False,  # Responde em JSON
)

# Agente auxiliar: Tutor (para tirar duvidas)
tutor_ia = Agent(
    name="Tutor IA",
    description="Tira duvidas sobre conceitos de IA sem dar respostas diretas",
    model=Groq(id=MODEL_ID),
    instructions="""
    Voce e um tutor de IA para alunos do TransformAI.
    Ajude os alunos a entender conceitos, mas NAO de respostas diretas da prova.
    
    Se perguntarem algo que parece ser da prova, ajude com:
    - Analogias e exemplos
    - Perguntas guiadas (metodo socratico)
    - Indicacao de onde estudar mais
    
    Topicos que voce pode ajudar:
    - Tokens e tokenizacao
    - Prompt Engineering
    - Temperatura em LLMs
    - Alucinacoes
    - Etica e Vies em IA
    """,
    db=SqliteDb(db_file="tutor_sessions.db"),
    add_datetime_to_context=True,
    add_history_to_context=True,
    num_history_runs=5,
    markdown=True,
)

# ═══════════════════════════════════════════════════════════════════════════
# AGENTOS - SERVIDOR
# ═══════════════════════════════════════════════════════════════════════════

agent_os = AgentOS(
    agents=[avaliador_prova, tutor_ia],
    tracing=True,  # Habilita rastreamento
)

# FastAPI app
app = agent_os.get_app()

# ═══════════════════════════════════════════════════════════════════════════
# ROTAS CUSTOMIZADAS (opcional)
# ═══════════════════════════════════════════════════════════════════════════

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class AvaliacaoRequest(BaseModel):
    numero_questao: int
    pergunta: str
    resposta_aluno: str
    criterios: Optional[str] = None

@app.post("/api/avaliar")
async def avaliar_questao(request: AvaliacaoRequest):
    """
    Endpoint customizado para avaliar uma questao diretamente.
    """
    prompt = f"""
    QUESTAO {request.numero_questao}:
    {request.pergunta}
    
    RESPOSTA DO ALUNO:
    {request.resposta_aluno}
    
    {f'CRITERIOS: {request.criterios}' if request.criterios else ''}
    
    Avalie e retorne o JSON de avaliacao.
    """
    
    response = avaliador_prova.run(prompt)
    return {"resultado": response.content if hasattr(response, 'content') else str(response)}

@app.get("/api/health")
async def health_check():
    """Verifica se o servidor esta funcionando."""
    return {
        "status": "ok",
        "model": MODEL_ID,
        "agents": ["Professor Avaliador", "Tutor IA"]
    }

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import uvicorn
    print("=" * 60)
    print("   TransformAI - AgentOS Prova")
    print("=" * 60)
    print(f"Modelo: {MODEL_ID}")
    print(f"Agentes: Professor Avaliador, Tutor IA")
    print()
    print("Iniciando servidor em http://localhost:8000")
    print("Documentacao da API: http://localhost:8000/docs")
    print("UI do AgentOS: https://os.agno.com")
    print("=" * 60)
    uvicorn.run(app, host="0.0.0.0", port=8000)
