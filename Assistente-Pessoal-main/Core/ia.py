from google import genai
from google.genai import types                        
from Config.keys import GOOGLE_API_KEY              
from Core.Personalidade import SYSTEM_PROMPT

client = genai.Client(api_key=GOOGLE_API_KEY)       

def chamar_ia(mensagem, historico=None):          
    if historico is None:
        historico = []

    mensagens_para_api = []

    # 1. Converter o histórico
    for msg in historico:
        # Garante a conversão de 'assistant' para 'model'
        role_gemini = "model" if msg["role"] == "assistant" else "user"
        
        mensagens_para_api.append(
            types.Content(
                role=role_gemini,
                parts=[types.Part(text=msg["content"])] # <--- MUDANÇA AQUI
            )
        )

    # 2. Adicionar a mensagem ATUAL do usuário
    mensagens_para_api.append(
        types.Content(
            role="user",
            parts=[types.Part(text=mensagem)] # <--- MUDANÇA AQUI
        )
    )

    try:
        # 3. Chamada à API
        resposta = client.models.generate_content(
            model="gemini-2.5-flash-lite", 
            contents=mensagens_para_api,        
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT 
            )
        )
        return resposta.text

    except Exception as e:
        print(f"Erro na API Gemini: {e}")
        return "Desculpe, tive um problema técnico."