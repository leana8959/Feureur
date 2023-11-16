import discord
import random
from unidecode import unidecode
from dotenv import load_dotenv
import os

###################################################
###                  prérequis                  ###
###################################################

# Read more:
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=intent#discord.Intents
intents = discord.Intents()
intents.guilds = True
intents.messages = True
intents.message_content = True
bot = discord.Client(intents=intents)

###################################################
###                   listes                    ###
###################################################

# Liste de String contenant une liste de mots autorises
authorised_words = [
    'quoiqu',
    'quoique',
    'quoi que ce',
    'quoi que se',
    'piquoit',
    'pouquoi',
    'séquoia',
    'taquoir',
    'carquois',
    'claquoir',
    'dacquois',
    'iroquois',
    'manquoit',
    'marquoir',
    'narquois',
    'pourquoi',
    'quoi que',
    'séquoias',
    'taquoirs',
    'claquoirs',
    'iroquoise',
    'marquoirs',
    'narquoise',
    'turquoise',
    'iroquoises',
    'narquoises',
    'turquoises',
    'métaséquoia',
    'tu-sais-quoi',
    'narquoisement',
    'je-ne-sais-quoi'
]
# Liste de gifs repondant 'feur'
tab_gif = [
    "https://tenor.com/view/feur-gif-23547897",
    "https://tenor.com/view/feur-theobabac-quoi-gif-24294658",
    "https://tenor.com/view/feur-meme-gif-24407942",
    "https://tenor.com/view/multicort-feur-gif-23304150"
]

###################################################
###                  fonctions                  ###
###################################################


def returned_message(content: str):
    '''
    Cette fonction renvoie une chaine de caracteres que le bot enverra dans le chat, personnalise en fonction du message passe en parametre
    Arguments :
        message (Any) : le message auquel on souhaite repondre
    Retourne :
        str (String) : une chaine de caracteres qui sera publie dans le chat par le bot
    '''
    liste = content.split()
    if 'quoi' in liste and ('antifeur' in liste or 'anti-feur' in liste):
        return ''
    elif 'quoi' in liste and ('anti' in liste and 'feur' in liste):
        return ''
    elif 'quoi' not in liste and ('antifeur' in liste or 'anti-feur' in liste):
        return "Pourquoi se protéger si l'on n'utilise même pas le q-word ? 🙄"
    elif 'quoi' not in liste and ('anti' in liste and 'feur' in liste):
        return "Pourquoi se protéger si l'on n'utilise même pas le q-word ? 🙄"
    elif 'quoi' in liste:
        n = random.randint(0, 11)
        if n in range(4):
            return tab_gif[n]
        else:
            return 'feur'
    for word in authorised_words:
        if (word in liste):
            return "...👀"
    else:
        return None

##################################################
### fonctions d'evenement lies au bot Discord  ###
##################################################


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print("liste des salons disponibles :\n[serveur] : [salon]")
    for guild in bot.guilds:  # parcourt les serveurs ou le bot est integre
        for channel in guild.text_channels:  # parcourt les salons du serveur
            print(f"{guild.name} : {channel.name}")


@bot.event
async def on_message(message: discord.Message):
    contenu = message.content

    # pour eviter que le bot ne se reponde a lui-meme
    if message.author.bot:
        return

    contenu = contenu.lower()  # on enleve les maj
    contenu = unidecode(contenu)  # on enleve les accents
    message_to_send = returned_message(contenu)
    if message_to_send:
        await message.channel.send(message_to_send)

###################################################
###                  lancement                  ###
###################################################

load_dotenv()
bot.run(os.environ['TOKEN'])
