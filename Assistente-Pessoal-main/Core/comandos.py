import webbrowser                                               # ? Importa o modulu que permite que o python abra urls no navegador, como youtube etc
import datetime                                                 # ? módulo de data/hora
import os                                                       # ? módulo do sistema operacional
from googleapiclient.discovery import build                     # ? importa a função build da biblioteca googleapiclient. Esta função é crucial para conectar seu código à API de Dados do YouTube.
import pyautogui                                                # ? Importa biblioteca que simula comandos do teclado
import time                                                     # ? Importa biblioteca com funçoes de tempo
from Config.keys import YOUTUBE_API_KEY
    
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)              # ? Cria um objeto chamado youtube que será usado para fazer todas as chamadas à API, meio que o telefone para ligar para o servidor

def abrir_youtube():
    webbrowser.open("https://www.youtube.com/")
    return "Abrindo YouTube."

def Pausar_video():                                                         # ? Função que pausa o video do youtube
    pyautogui.press("k")
    return "Video pausado."

def fechar_aba_atual():                                                     # ? Função que vai fechar a aba atual do youtube para abrir outra
    pyautogui.hotkey("ctrl", "w")
    return ""

def abrir_google():
    webbrowser.open("https://www.google.com.br/index.html")
    return "Abrindo Google."

def dizer_hora():                                                           # ? pega a hora atual e retorna uma string formatada.
    agora = datetime.datetime.now().strftime("%H:%M")                       # ?  retorna um objeto datetime com data e hora atuais e converte esse objeto em uma str formatada, %H = hora com 2 dígitos, %M = minuto com 2 dígitos
    return f"Agora são {agora}"

def abrir_programa(caminho):                                                # ? abre um programa no Windows pelo caminho completo.
    try:
        os.startfile(caminho)
        return f"Abrindo programa em: {caminho}"
    except Exception as e:
        return f"Erro ao abrir o programa: {e}"

def buscar_video(termo):                                                    # ? Busca o primeiro vídeo correspondente ao termo.
    req = youtube.search().list(                                            # ? constrói a requisição para a API
        q=termo,                                                            # ? termo de busca
        part="snippet",                                                     # ! especifica que quer o trecho snippet dos resultados (título/descrição).
        maxResults=1,                                                       # ? pede só 1 resultado
        type="video"                                                        # ? restringe a busca a vídeos (não playlists ou canais)
    )

    res = req.execute()

    if not res["items"]:                                                     # ? resposta da API tem uma estrutura JSON; se nada for encontrado, none em caso de erro e tals
        return None

    video_id = res["items"][0]["id"]["videoId"]
    return f"https://www.youtube.com/watch?v={video_id}"

def abrir_video(termo, fechar_anterior=True):
    if fechar_anterior == True:
        fechar_aba_atual()
        time.sleep(0.5)
    url = buscar_video(termo)                                                # ? chama a função para obter a url. 1- envia a requisição para a API do YouTube, 2- recebe a lista de resultados, 3- pega apenas o primeiro vídeo retornado, 4- extrai o videoId, 5- e monta a url(exempli: https://www.youtube.com/watch?v=VIDEO_ID_AQUI)

    if not url:
        return "Não encontrei esse vídeo. Verifique o nome ou sua API KEY."

    webbrowser.open(url)
    return f"Reproduzindo {termo} no YouTube."

def interpretar_comando(texto):
    texto = texto.lower()                                                   # ? Deixa tudo em minusculo
    comandos_musica = ["tocar", "ouvir", "reproduzir"]                      # ? Palavras chaves para exexutar a função

    for cmd in comandos_musica:                                             # ? Faz loop dentro da lista de palavras de ativação
        if cmd in texto:                                                    # ? Procura essa palavra no testo que vc falou
            indice = texto.find(cmd)                                        # ? ele pega o indice aonde esta a plavra de ativação
            termo_busca = texto[indice + len(cmd):].strip()                 # ? e pega o texto a frente(exemplo: tocar ride, ele pega ride para pesquisar)
            if termo_busca:
                return abrir_video(termo_busca)
            else:
                return "Qual música você quer ouvir?"
            
    if "youtube" in texto:
        return abrir_youtube()
    elif "google" in texto:
        return abrir_google()
    elif "pausar" in texto or "despausar" in texto:
        return Pausar_video()
    elif "hora" in texto:
        return dizer_hora()
    elif "calculadora" in texto:
        return abrir_programa("C:\\Windows\\System32\\calc.exe")

    return None
