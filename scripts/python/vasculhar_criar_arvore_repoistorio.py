import os
def print_tree(startpath, file_output, prefix=""):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        file_output.write(f"{prefix}|--- {os.path.basename(root)}/\n")
        subindent = " " * 4 * (level + 1)
        for f in files:
            file_output.write(f"{subindent}|____ {f}\n")
        prefix = " " * 4 * (level + 1)
# Caminho do repositório local
caminho_do_repositorio = "."
# Cria e escreve no arquivo directory_tree.txt com codificação UTF-8
with open("directory_tree.txt", "w", encoding="utf-8") as file_output:
    print_tree(caminho_do_repositorio, file_output)
print("A árvore de diretórios foi salva em 'directory_tree.txt'")
