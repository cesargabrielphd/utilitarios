import os


def create_project_structure():
    # Diretórios a serem criados
    directories = ["data", "docs", "scripts/R", "scripts/python", "tests"]

    # Arquivos a serem criados
    files = [
        "data/base_completa.xlsx",
        "data/CNPJ - pag.Lei-doBem & pasta.P-rede.xlsx",
        "data/cnpj-participantes-lei-do-bem-2006-a-2023.xlsx",
        "docs/README.md",
        "docs/resultados.html",
        "docs/resultados.Rmd",
        "scripts/R/cnpj_analysis.R",
        "scripts/R/calculate_new_cnpjs.R",
        "scripts/R/calculate_accumulated_cnpjs.R",
        "scripts/python/modify_regex_files.py",
        "scripts/python/rename_files_to_standard.py",
        "scripts/python/remove_standard_names.py",
        "scripts/python/split_pdf_pages.py",
        "scripts/python/replace_patterns.py",
        "scripts/python/test_rename_files.py",
        "tests/funcao_cnpj_novo.R",
        "tests/teste_funcao.html",
        "tests/teste_funcao.Rmd",
        ".Rhistory",
    ]

    # Criar diretórios
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Criar arquivos
    for file in files:
        with open(file, "w") as f:
            pass

    print("Estrutura do projeto criada com sucesso!")


# Executar a função
create_project_structure()
