🐙 Tutorial GitHub — Do Zero ao Pull Request
Para estudantes que nunca usaram Git ou GitHub

O que é o GitHub e por que usar?
Pensa assim: o GitHub é um Google Drive para código, mas com superpoderes:

Guarda o histórico de tudo que você mudou (dá pra voltar no tempo!)
Permite colaborar com outras pessoas sem sobrescrever o trabalho de ninguém
É onde todo programador do mundo guarda seus projetos
Seu perfil no GitHub é seu portfólio para o mercado de trabalho


Parte 1 — Criar sua conta

Acesse https://github.com
Clique em Sign up
Escolha um nome de usuário profissional (ex: joao-silva, não xXgamer2009Xx 😄)
Use seu e-mail e crie uma senha
Confirme seu e-mail

✅ Pronto! Você tem uma conta GitHub.

Parte 2 — Conceitos essenciais (leia com calma!)
Antes de usar, entenda esses 5 termos. Você vai ver eles o tempo todo:
TermoO que significaAnalogiaRepository (repo)Uma pasta com seu projetoPasta no Google DriveCommitSalvar uma versão com uma mensagem"Salvar como" com descriçãoBranchUma versão paralela do projetoRascunho de um documentoForkCopiar o repositório de alguém para o seu perfil"Fazer uma cópia"Pull Request (PR)Pedir para juntar sua branch com a principalEnviar o rascunho para revisão
Visualizando o fluxo completo:
Repositório original (professor)
        │
        │  fork (você faz uma cópia)
        ▼
Seu repositório (cópia no seu perfil)
        │
        │  você trabalha aqui, faz commits
        ▼
Sua branch (ex: atividades/seu-nome)
        │
        │  Pull Request (você pede para juntar)
        ▼
Repositório original recebe sua entrega ✅

Parte 3 — Instalando o Git no seu computador
O Git é o programa que roda no seu computador. O GitHub é o site. São coisas diferentes!
Windows

Acesse https://git-scm.com/download/win
Baixe e instale (pode clicar "Next" em tudo)
Abra o Git Bash (aparece no menu iniciar)

Mac

Abra o Terminal
Digite: git --version
Se não estiver instalado, o Mac vai oferecer instalar automaticamente

Linux (Ubuntu/Debian)
bashsudo apt update
sudo apt install git
Verificar se funcionou
Abra o terminal (Git Bash no Windows) e digite:
bashgit --version
# Deve aparecer algo como: git version 2.43.0

Parte 4 — Configuração inicial (só uma vez!)
Antes de usar, diga ao Git quem você é:
bashgit config --global user.name "Seu Nome Aqui"
git config --global user.email "seu@email.com"

# Verifique se ficou certo:
git config --list

Parte 5 — Fazendo o Fork do repositório da aula

Fork = copiar o repositório do professor para o SEU perfil


Acesse o repositório da aula (o professor vai passar o link)
No canto superior direito, clique no botão Fork

   ┌─────────────────────────────────────┐
   │  professor/atividades-ia      ⭐ Fork │
   └─────────────────────────────────────┘

Clique em Create fork
Agora você tem uma cópia em: github.com/SEU-USUARIO/atividades-ia


Parte 6 — Clonando para seu computador

Clone = baixar o repositório do GitHub para sua máquina

bash# 1. Abra o terminal na pasta onde quer salvar o projeto
# (ex: Documentos)

# 2. Clone o SEU fork (não o do professor!)
git clone https://github.com/SEU-USUARIO/atividades-ia.git

# 3. Entre na pasta
cd atividades-ia

# 4. Veja o que tem lá
ls
Vai aparecer a estrutura de pastas do projeto!

Parte 7 — Criando sua branch

Nunca trabalhe direto na branch main! Crie sempre uma branch com seu nome.

bash# Cria e já entra na nova branch
git checkout -b atividades/seu-nome

# Exemplo real:
git checkout -b atividades/joao-silva

# Verifique em qual branch você está:
git branch
# O * indica a branch atual
# * atividades/joao-silva
#   main

Parte 8 — O ciclo de trabalho diário
Esse é o ciclo que você vai repetir toda vez que trabalhar no projeto:
Trabalhar nos arquivos → git add → git commit → git push
Passo a passo:
bash# 1. Veja o que mudou
git status
# Arquivos em vermelho = modificados mas não salvos

# 2. Adicione os arquivos que quer salvar
git add respostas-01.md
# Ou adicione tudo de uma vez:
git add .

# 3. Faça o commit com uma mensagem descritiva
git commit -m "feat: responde atividade 01 - tokens"

# 4. Envie para o GitHub
git push origin atividades/seu-nome
Boas mensagens de commit (importante! 💡)
bash# ✅ Bom — diz O QUE mudou
git commit -m "feat: completa atividade 03 com gráfico de temperatura"
git commit -m "fix: corrige erro na função comparar_idiomas"
git commit -m "docs: adiciona respostas da atividade 05"

# ❌ Ruim — não diz nada útil
git commit -m "mudanças"
git commit -m "atualizando"
git commit -m "aaaa"

Parte 9 — Abrindo o Pull Request
Quando terminar as atividades, é hora de entregar!

Acesse seu repositório no GitHub: github.com/SEU-USUARIO/atividades-ia
Vai aparecer um aviso amarelo:

   ⚡ atividades/joao-silva had recent pushes
   [Compare & pull request]  ← clique aqui!

Preencha o formulário:

   Título: Atividades completas - João Silva
   
   Descrição:
   ## O que fiz
   - [x] Atividade 01 - Tokens
   - [x] Atividade 02 - Prompt Engineering
   - [x] Atividade 03 - Temperatura
   - [x] Atividade 04 - Alucinações
   - [x] Atividade 05 - Ética e Viés
   
   ## Qual atividade me surpreendeu mais?
   (escreva aqui sua resposta!)
   
   ## Dificuldades encontradas
   (opcional, mas ajuda o professor!)

Clique em Create Pull Request ✅


Parte 10 — Usando o Google Colab (alternativa ao terminal)
Se você não quer instalar nada no computador, o Google Colab permite usar Git direto no navegador!
python# Cole isso em uma célula do Colab

# Configurar git
!git config --global user.name "Seu Nome"
!git config --global user.email "seu@email.com"

# Clonar o repositório
!git clone https://github.com/SEU-USUARIO/atividades-ia.git
%cd atividades-ia

# Criar branch
!git checkout -b atividades/seu-nome

# --- trabalhe nos arquivos ---

# Salvar e enviar
!git add .
!git commit -m "feat: atividades completas"

# Para push no Colab, precisamos autenticar:
# Use um Personal Access Token (veja abaixo)
!git push https://SEU-TOKEN@github.com/SEU-USUARIO/atividades-ia.git atividades/seu-nome
Criando um Personal Access Token (para push no Colab)

GitHub → foto do perfil → Settings
Developer settings → Personal access tokens → Tokens (classic)
Generate new token → marque repo → Generate token
Copie o token (ele só aparece uma vez!)
Use no lugar de SEU-TOKEN no comando acima


Parte 11 — Erros comuns e como resolver
❌ "Permission denied"
bash# Solução: configure o token de acesso ou use SSH
git remote set-url origin https://SEU-TOKEN@github.com/SEU-USUARIO/atividades-ia.git
❌ "Your branch is behind main"
bash# Solução: atualize sua branch com as mudanças do professor
git pull origin main
❌ "Nothing to commit"
bash# Nenhum arquivo foi modificado. Verifique se salvou os arquivos!
git status
❌ "Merge conflict"
bash# Dois commits mudaram a mesma linha. Abra o arquivo,
# procure por <<<<<<< e edite manualmente para ficar como quer.
# Depois:
git add arquivo-conflitante.md
git commit -m "fix: resolve conflito"

Resumo Visual — Os comandos mais usados
bash# ─── SETUP (só uma vez) ───────────────────────────
git config --global user.name "Nome"
git config --global user.email "email"

# ─── COMEÇAR UM PROJETO ───────────────────────────
git clone <url>          # baixar repositório
git checkout -b <branch> # criar e entrar em branch

# ─── CICLO DIÁRIO ─────────────────────────────────
git status               # ver o que mudou
git add .                # preparar tudo para commit
git commit -m "mensagem" # salvar versão
git push origin <branch> # enviar para o GitHub

# ─── OUTROS ÚTEIS ─────────────────────────────────
git log --oneline        # ver histórico de commits
git diff                 # ver o que mudou linha a linha
git stash                # guardar mudanças temporariamente
git pull origin main     # puxar atualizações do professor

Checklist de entrega ✅
Antes de abrir o PR, verifique:

 Fiz fork do repositório correto
 Criei uma branch com meu nome (atividades/meu-nome)
 Completei os arquivos respostas-0X.md de cada atividade
 Os notebooks .ipynb rodam sem erro
 Fiz git push da minha branch
 Abri o Pull Request com título e descrição preenchidos
 Respondi a pergunta "qual atividade me surpreendeu mais?" no PR


Dúvidas? Abra uma Issue no repositório da aula — é como um fórum de perguntas! 🙋