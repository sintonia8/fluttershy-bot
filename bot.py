import discord
import random
import os
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "A Fluttershy tá maluca, mas tá viva!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

acoes = [
    "lambeu uma nuvem de algodão-doce radioativo",
    "conversou com a torradeira sobre física quântica",
    "escondeu o arco-íris debaixo do travesseiro",
    "fingiu ser uma capivara espacial",
    "dançou balé em cima de um pudim cósmico"
]

objetos = [
    "de gelo nuclear",
    "feito de pura purpurina estelar",
    "que chora leite condensado",
    "com sabor de terça-feira passada",
    "movido a abraços de urso robô"
]

reacoes_fluttershy = [
    "*(fala bem baixinho e treme)*",
    "*(esconde o rosto na crina com desespero)*",
    "*(dá um gritinho agudo que estilhaça copos)* YAY...",
    "*(olha fixamente para o nada com os olhos brilhando)*"
]

@client.event
async def on_ready():
    print(f'🤖 Fluttershy 24h tá ON! {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    reacao = random.choice(reacoes_fluttershy)
    acao = random.choice(acoes)
    objeto = random.choice(objetos)
    resposta = f"E-eai {message.author.mention}... {reacao} O-olha só: eu {acao} num lugar {objeto}! 🦄✨ É bem fofinho, mas meio apocalíptico... oush!"
    await message.channel.send(resposta)

t = Thread(target=run_web)
t.start()

TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
