import pyttsx4                                              # ? Importa biblioteca para sintese de voz
import speech_recognition as sr                             # ? Importa biblioteca que converte oque eu falo em texto
import time                                                 # ? importa biblioteca com funcoes relacionadas ao tempo

reconhecedor = sr.Recognizer()                                          # ? Objeto que gerencia a captura/interpretacão de áudio
sintetizador = pyttsx4.init('sapi5')                                    # ? Inicializa o engine do pyttsx4 e escolhe o driver sapi5
sintetizador.setProperty('rate', 235)                                   # ? Defini a velocidade de fala da IA
sintetizador.setProperty('volume', 1.0)                                 # ? Define o volume da fala; 1.0

voices = sintetizador.getProperty('voices')                             # ? pega a lista de vozes disponíveis do modulo/pc para a ia usar e vc escolher
sintetizador.setProperty('voice', voices[0].id)                         # ? Define a voz a ser usada; aqui usa a primeira voz disponível

def falar_texto(texto):                                                 # ? Converte texto em voz
    texto = texto
    if not texto.strip():                                               # ? Verifica se texto está vazio ou contém só espaços(strip() remover espaços em branco nas extremidades). Se estiver vazio, vai evitar tentar falar algo.)
        return
    try:
        time.sleep(0.5)                                                  # ? Pausa de meio segundo antes de falar
        sintetizador.say(texto)                                         # ? Faz o computador falar.
        sintetizador.runAndWait()                                       # ? Bloqueante: espera terminar de falar
    except Exception as e:                                              # ? Captura qualquer exceção que ocorra dentro do try (por exemplo, problema com driver de áudio)
        print(f"❌ Erro ao falar: {e}")


def ouvir_microfone():                                                                              #? Função que vai capturar e processar o audio do usuario(oque vc fala vira texto)
    with sr.Microphone() as mic:                                                                    #? o with garante que o microfone sera aberto e fechado, MIC é a variavel que vai representar o microfone
        print("🎤 Ouvindo...")
        reconhecedor.adjust_for_ambient_noise(mic, duration=1)                                      #? reconhecedor "escuta" o ambiente por 1 segundo para detectar ruído e ajustar automaticamente a sensibilidade.
        audio = reconhecedor.listen(mic)                                                            #? Captura o áudio do microfone e armazena na variável audio. porem no formato AudioData

    try:
        texto = reconhecedor.recognize_google(audio, language="pt-BR")                              #? Envia o áudio capturado para o Google Speech Recognition e recebe o texto transcrito, em português do Brasil. e armazena na variavel em formato string
        texto_lower = texto.lower()                                                                 #? Comverte tudo para minusculo

        wake_words = ["jarvis", "jarbas", "jarvi", "jarv", "jarve", "jarvs", "jarves"]              #? palavras de ativação

        if any(w in texto_lower for w in wake_words):                                               #? 1- any retorna true se o criterio for atendido.A expressão percorre todas as wake words e verifica se alguma delas aparece no texto             
            for w in wake_words:
                if w in texto_lower:
                    wake_words = w
                    break
            comando = texto_lower.replace(wake_words, "", 1).strip()                                 #? replace ele subistitui a wake word por "" ou seja nada, e o .strip() remove espaços no começo e no fim.

            caracteres_validos = "abcdefghijklmnopqrstuvwxyzáéíóúâêôãõç 0123456789"                 #? Caracteres validos, assim ele remove caracteres invalidos no historico
            comando_limpo = "".join(                                                            
                c for c in comando.lower() if c in caracteres_validos)                              #? Ele primeiro padroniza convertendo para minusculo e depois faz um loop por todos os caracteres de forma individual e verifica se o caractere e valido. O método join pega o iterável (aqui, os caracteres aprovados) e concatena todos

            print(f"Você disse: {comando_limpo}")                                                   #? Aparece no terminal oque vc disse

            return comando_limpo
        else:
            return ""

    except Exception:
        return ""
