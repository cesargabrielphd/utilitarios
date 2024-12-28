import os
import shutil

# Função para criar a estrutura de diretórios
def criar_estrutura(disciplina="disciplina-01"):
    dirs = [
        f"{disciplina}/Estudos/conteúdos/bibliografia",
        f"{disciplina}/Estudos/conteúdos/teoria-leve",
        f"{disciplina}/Estudos/conteúdos/teoria-avançada",
        f"{disciplina}/exercícios/teoria-leve",
        f"{disciplina}/exercícios/teoria-avançada",
        f"{disciplina}/projeto/data/bruto",
        f"{disciplina}/projeto/data/tratados",
        f"{disciplina}/projeto/code/importação",
        f"{disciplina}/projeto/code/tratamento",
        f"{disciplina}/projeto/code/analise",
        f"{disciplina}/projeto/resultado/graficos",
        f"{disciplina}/projeto/resultado/relatórios"
    ]

    if os.path.exists(disciplina):
        print(f"O diretório '{disciplina}' já existe.")
        return

    for dir in dirs:
        os.makedirs(dir, exist_ok=True)

    print(f"Estrutura de diretórios para '{disciplina}' criada com sucesso!")

# Função para deletar a estrutura de diretórios
def deletar_estrutura(disciplina):
    if os.path.exists(disciplina):
        shutil.rmtree(disciplina)
        print(f"Estrutura de diretórios para '{disciplina}' deletada com sucesso!")
    else:
        print(f"O diretório '{disciplina}' não existe.")

# Solicita ao usuário a ação desejada
acao = input("Digite 'c' para criar uma disciplina ou 'd' para deletar uma disciplina: ").strip().lower()

acao = acao.lower(acao)
if acao in ['c', 'criar', 's', 'sim']:
    # Solicita os nomes das disciplinas ao usuário
    disciplinas_input = input("Digite os nomes das disciplinas separados por vírgula (ex: disciplina-01,disciplina-02): ")
    if not disciplinas_input.strip():
        criar_padrao = input("Nenhuma disciplina foi digitada. Deseja criar a disciplina padrão 'disciplina-01'? (s/n): ").strip().lower()
        if criar_padrao in ['s', 'sim']:
            criar_estrutura("disciplina-01")
        else:
            print("Nenhuma disciplina foi criada.")
    else:
        disciplinas = [disciplina.strip() for disciplina in disciplinas_input.split(",")]
        for disciplina in disciplinas:
            criar_estrutura(disciplina)

elif acao in ['d', 'deletar', 'n', 'nao']:
    # Solicita o nome da disciplina a ser deletada
    disciplina = input("Digite o nome da disciplina a ser deletada: ").strip()
    if not disciplina:
        print("Nenhuma disciplina foi digitada. Por favor, digite o nome de uma disciplina.")
    else:
        deletar_estrutura(disciplina)

else:
    print("Ação inválida. Por favor, digite 'c' para criar ou 'd' para deletar.")



# créditos: copilot do vscode

# Só mandei os comandos......... digite: F
