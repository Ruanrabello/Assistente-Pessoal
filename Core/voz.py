import pyttsx4  # ? Importa biblioteca para sintese de voz
# ? Importa biblioteca que converte oque eu falo em texto
import speech_recognition as sr
import time  # ? importa biblioteca com funcoes relacionadas ao tempo

# Inicializadores
# ! Objeto que gerencia a captura/interpretacão de áudio
reconhecedor = sr.Recognizer()
# ? Inicializa o engine do pyttsx4 e escolhe o driver sapi5
sintetizador = pyttsx4.init('sapi5')
# ? Ajusta a velocidade de fala (palavras por minuto).
sintetizador.setProperty('rate', 220)
sintetizador.setProperty('volume', 1.0)  # ? Define o volume da fala; 1.0

# ? Recupera a lista de vozes disponíveis do engine
voices = sintetizador.getProperty('voices')
# ? Define a voz a ser usada; aqui usa a primeira voz disponível
sintetizador.setProperty('voice', voices[0].id)


def falar_texto(texto):  # ? Converte texto em voz
    # ? (adiciona no início) a string "Senhor, " ao texto recebido
    texto = texto
    if not texto.strip():  # ? Verifica se texto está vazio ou contém só espaços(strip() remover espaços em branco nas extremidades). Se estiver vazio, vai evitar tentar falar algo.)
        return
    try:
        time.sleep(1)  # ? Pausa de 1 segundo antes de falar
        sintetizador.say(texto)  # ? Faz o computador falar.
        sintetizador.runAndWait()  # ? Bloqueante: espera terminar de falar
    except Exception as e:
        # ? Captura qualquer exceção que ocorra dentro do try (por exemplo, problema com driver de áudio)
        print(f"❌ Erro ao falar: {e}")


def ouvir_microfone():
    with sr.Microphone() as mic:
        print("🎤 Ouvindo...")
        reconhecedor.adjust_for_ambient_noise(mic, duration=1)
        audio = reconhecedor.listen(mic)

    try:
        texto = reconhecedor.recognize_google(audio, language="pt-BR")
        texto_lower = texto.lower()

        wake_words = ["jarvis", "jarbas", "jarvi"]  # coloque quantas quiser

        # --- VERIFICA SE COMEÇA COM ALGUMA WAKE WORD ---
        if any(texto_lower.startswith(w) for w in wake_words):

            # remove a wake-word da frente
            wake_word = next(
                w for w in wake_words if texto_lower.startswith(w))
            comando = texto[len(wake_word):].strip()

            # --- remove simbolos indesejados ---
            caracteres_validos = "abcdefghijklmnopqrstuvwxyzáéíóúâêôãõç 0123456789"
            comando_limpo = "".join(
                c for c in comando.lower() if c in caracteres_validos)

            # 🔥 Só aqui aparece no console:
            print(f"Você disse: {comando_limpo}")

            return comando_limpo
        else:
            return ""

    except Exception:
        return ""
