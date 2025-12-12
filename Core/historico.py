import json
import os

CAMINHO_HISTORICO = "C:/Users/ruanb/Downloads/AssistenteV2/data/Historico.json"


def limpar_texto(texto):
    caracteres_validos = "abcdefghijklmnopqrstuvwxyzáéíóúâêôãõç 0123456789"
    texto_limpo = "".join(c for c in texto.lower() if c in caracteres_validos)
    return texto_limpo.strip()


def carregar_historico():
    if os.path.exists(CAMINHO_HISTORICO):
        try:
            with open(CAMINHO_HISTORICO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def salvar_historico(historico):
    with open(CAMINHO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


def adicionar_mensagem(historico, role, content):
    # 🔹 Limpa texto ANTES de salvar para evitar *, #, etc.
    content_limpo = limpar_texto(content)

    historico.append({"role": role, "content": content_limpo})

    # 🔹 Mantém no máximo 50 mensagens
    if len(historico) > 50:
        historico.pop(0)

    salvar_historico(historico)
    return historico


def limpar_historico():
    if os.path.exists(CAMINHO_HISTORICO):
        os.remove(CAMINHO_HISTORICO)
