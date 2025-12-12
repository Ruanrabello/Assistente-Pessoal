from groq import Groq                             #? 📌 Importa a classe groq que é responsável por fazer chamadas para o endpoint
from Config.keys import GROQ_API_KEY              #? 📌 Esta importando a variavel/chave do arquivo ja criado da past config
from Core.Personalidade import SYSTEM_PROMPT

client = Groq(api_key= GROQ_API_KEY)              #? 📌 Equivale a abrir a conexão para chamar a API.

def chamar_ia(mensagem, historico=None):          #? 📌 função que recebe o texto que o usuario digitou e a lista de mensagens anteriores
    if historico is None:                         #? 📌 Se for a primeira vez chamando a função, ainda não existe histórico entap cria uma função
        historico =[]

    mensagens_para_api = [{"role": "system", "content": SYSTEM_PROMPT}]         #? Criamos uma lista Nova para envio começando sempre coma personalidade
    mensagens_para_api.extend(historico)                                        #? Adicionamos todo o histórico da conversa (User + Assistant anteriores)
    mensagens_para_api.append({"role": "user", "content": mensagem})            #? # 3. Adicionamos a pergunta ATUAL do usuário

    resposta = client.chat.completions.create(          #! Chama o endpoint chat/completions
        model="llama-3.1-8b-instant",                   #! Passa o modelo
        messages=mensagens_para_api                     #! Envia as mensagens (histórico + nova)
    )

    texto = resposta.choices[0].message.content         #! Pega só o texto que a IA gerou
    return texto


'''
 A resposta da Groq vem dentro de um array choices.
1-Você pega a primeira resposta (0)
2-Depois pega o atributo message
3-E por fim pega somente o texto (content)

💡 Exemplo da estrutura real:
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Olá! Como posso ajudar?"
      }
    }
  ]
}
'''
    