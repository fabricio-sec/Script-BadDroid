import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_final = os.path.join(diretorio_atual, "payload_android2.dd")

# Alterar somente o número de DELAY'S caso ache lento ou rápido d+
composto = """
CTRL t
DELAY 500
STRING localhost
DELAY 200
ENTER
DELAY 500
"""
# Alterar somente o número de DELAY'S caso ache lento ou rápido d+
inicio = """REM --- CONFIGURAÇÃO INICIAL ---
DELAY 500
GUI b
DELAY 3000
CTRL l
DELAY 150
STRING localhost
DELAY 150
ENTER
DELAY 350
"""

quantidade_de_abas = 300 # Alteravel dependendo da sua finalidade

with open(caminho_final, "w", encoding="utf-8") as f:
    f.write(inicio)
    for _ in range(quantidade_de_abas):
        f.write(composto)

print(f"Sucesso! Novo payload ultra-rápido gerado em:\n-> {caminho_final}")
