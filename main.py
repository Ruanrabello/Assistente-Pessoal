from Core.voz import ouvir_microfone, falar_texto
from Core.ia import chamar_ia
from Core.comandos import interpretar_comando
from Core.historico import carregar_historico, adicionar_mensagem


# ? Hisótico da conversa
historico = carregar_historico()

print("Assistente iniciado. Diga 'PARAR' para encerrar.")

# ? Loop infinito que mantém o assistente escutando até receber o comando de encerrar (break).
while True:

    # ? Chama a função eque pega oque vc fala e retorna o texto transcrito(string) e associa a variavel
    comando = ouvir_microfone()
    # ? Se a função retorna "", então continue reinicia o loop sem processar nada.
    if comando == "":
        continue

    if "parar" in comando.lower() or "encerrar" in comando.lower():
        falar_texto(
            "Encerrando assistente. foi um prazer auxiliá-lo SENHOR Ruan.")
        break

    # ? Ele chama função que abre as urls e apps de acordo com a palavra chave q a gente fala, se a funçlãoindetificar a palavra chave vai abrir, exemplo o youtube
    resposta_comando = interpretar_comando(comando)
    # ? e vai retornar um texto (Exemplo: ("Abrindo Youtube..."))
    if resposta_comando:
        falar_texto(resposta_comando)
        continue
        # ? Se não for comando direto, enviar para a IA
    # ? Vai adicionar assim no meu historico.json  historico.append({"role": "user", "content": comando}), comando é oque eu falei
    resposta_ia = chamar_ia(comando, historico)
    # ? e depois vai adicionar nese formato porem a resposta da ia
    adicionar_mensagem(historico, "user", comando)
    adicionar_mensagem(historico, "assistant", resposta_ia)

    # ? Falar a respsota da IA
    falar_texto(resposta_ia)
