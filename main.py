from openai import OpenAI

chave_api = "key"

# Configurando o cliente OpenAI
client = OpenAI(api_key=chave_api)

def enviar_mensagem(mensagem):
    # Criando uma conclusão de bate-papo
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": mensagem,
            },
        ],
    )
    return completion.choices[0].message['content']

print(enviar_mensagem("Em que ano Einstein publicou a teoria geral da relatividade?"))
