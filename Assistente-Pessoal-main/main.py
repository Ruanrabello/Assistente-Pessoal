from Core.voz import ouvir_microfone, falar_texto
from Core.ia import chamar_ia
from Core.comandos import interpretar_comando
from Core.historico import carregar_historico, adicionar_mensagem

historico = carregar_historico()                                                        # ? Hisótico da conversa

print("Assistente iniciado. Diga 'PARAR' para encerrar.")

while True:                                                                             # ? Loop infinito que mantém o assistente escutando até receber o comando de encerrar (break).
    comando = ouvir_microfone()                                                         # ? Chama a função eque pega oque vc fala e retorna o texto transcrito(string) e associa a variavel
    if comando == "":                                                                   # ? Se a função retorna "", então continue reinicia o loop sem processar nada.
        continue

    if "parar" in comando.lower() or "encerrar" in comando.lower():                     #? Se encontrar parar ou encerrar nbo que vc falou ele encerra 
        falar_texto(
            "Encerrando assistente. foi um prazer auxiliá-lo SENHOR Ruan.")
        break

    resposta_comando = interpretar_comando(comando)                                     # ? Ele chama função que abre as urls e apps de acordo com a palavra chave q a gente fala, se a funçlãoindetificar a palavra chave vai abrir, exemplo o youtube
    if resposta_comando:                                                                  
        falar_texto(resposta_comando)                                                   # ? e vai retornar um texto (Exemplo: ("Abrindo Youtube..."))
        continue
                                               
    
    resposta_ia = chamar_ia(comando, historico)                              # ? Se não for comando direto, enviar para a IA
    adicionar_mensagem(historico, "user", comando)                           # ? Vai adicionar assim no meu historico.json  historico.append({"role": "user", "content": comando}), comando é oque eu falei
    adicionar_mensagem(historico, "assistant", resposta_ia)                  # ? e depois vai adicionar nese formato porem a resposta da ia
    
    falar_texto(resposta_ia)                                                 # ? Falar a respsota da IA

