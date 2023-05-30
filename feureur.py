import discord
import random

###################################################
###                  prérequis                  ###
###################################################

# Definit une variable intents qui contient les "intents" par defaut de la bibliotheque discord.
# Les intents sont des informations sur les donnees que vous voulez recevoir depuis le serveur Discord.
intents = discord.Intents.default()
# Cette ligne active l'intent pour les "guilds" (serveurs), ce qui signifie que votre bot sera informe de tous les changements au sein du serveur.
intents.guilds = True
# Cette ligne active l'intent pour les "guild_messages" (messages de salon), 
# ce qui signifie que le bot sera informe de tous les messages dans les salons auxquels il a acces.
intents.guild_messages = True
# Cette ligne cree un objet "client" pour se connecter a Discord en utilisant les intents définis dans la variable intents.
client = discord.Client(intents=intents)

###################################################
###                   listes                    ###
###################################################

# Liste de String contenant une liste de mots autorises
authorised_words = ['quoiqu','quoique','quoi que ce','quoi que se','piquoit','pouquoi','séquoia','taquoir','carquois','claquoir','dacquois','iroquois','manquoit','marquoir','narquois','pourquoi','quoi que','séquoias','taquoirs','claquoirs','iroquoise','marquoirs','narquoise','turquoise','iroquoises','narquoises','turquoises','métaséquoia','tu-sais-quoi','narquoisement','je-ne-sais-quoi']
# Liste de gif repondant 'feur'
tab_gif = ["https://tenor.com/view/feur-gif-23547897","https://tenor.com/view/feur-theobabac-quoi-gif-24294658","https://tenor.com/view/feur-meme-gif-24407942","https://tenor.com/view/multicort-feur-gif-23304150"]

###################################################
###                  fonctions                  ###
###################################################

def returned_message(message):
    '''
    Cette fonction renvoie une chaine de caracteres que le bot enverra dans le chat, personnalise en fonction du message passe en parametre
    Arguments :
        message (Any) : le message auquel on souhaite repondre
    Retourne :
        str (String) : une chaine de caracteres qui sera publie dans le chat par le bot
    Idees de cas de figures ou on peut repondre 'feur' :
        - c'est quoi [...]
        - tu fais quoi 
        - quoi de neuf
    '''
    for word in authorised_words:
        if (word in message.content):
            return "...👀"
    if ('antifeur' or 'anti feur' or 'anti-feur') in message.content:
        return "👌"
    elif message.content == "quoi":
        n = random.randint(0,3)
        return tab_gif[n]
    elif ('c\'est' in message.content and 'quoi' in message.content):
        return 'c\'est feur je pense non ?\nt\'en penses quoi ? (anti-feur lol)'
    elif (('fais' in message.content or 'fait' in message.content) and 'quoi' in message.content):
        return "personnellement j'adore faire feur"
    elif ('?' in message.content and 'quoi' in message.content and message.channel.type != discord.ChannelType.private):
        return "moi je crois savoir, mais je suis pas sûr"
    elif ('quoi' in message.content):
        n = random.randint(0,19)
        if n > 3:
            return "feur"
        return tab_gif[n]

###################################################
### fonctions d'evenement lie au client Discord ###
###################################################

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print("liste des salons disponibles :\n[serveur] : [salon]")
    for guild in client.guilds: # parcourt les serveurs ou le bot est integre
        for channel in guild.text_channels: # parcourt les salons du serveur
            if channel.permissions_for(guild.me).read_messages: # on regarde ceux ou le bot peut lire les messages
                if channel.permissions_for(guild.me).send_messages: # on regarde ceux ou le bot peut envoyer des messages
                    print(f"{guild.name} : {channel.name}")

@client.event
async def on_message(message):
    # conversion du message en minuscules
    message.content = message.content.lower()

    # pour eviter que le bot ne se reponde a lui-meme
    if message.author == client.user:
        return

    # gerer la discussion privee avec le bot
    elif 'quoi' in message.content and message.channel.type == discord.ChannelType.private and message.author != client.user:
        message_to_send = returned_message(message)
        await message.channel.send(message_to_send)

    # gerer la discussion dans un serveur
    else:
        for guild in client.guilds: # parcourt les serveurs ou le bot est integre
            for channel in guild.text_channels: # parcourt les salons du serveur
                if channel.permissions_for(guild.me).read_messages: # on regarde ceux ou le bot peut lire les messages
                    if channel.permissions_for(guild.me).send_messages: # on regarde ceux ou le bot peut envoyer des messages
                        try: # certains salons auront un message qui fera planter le code
                            last_message = await channel.fetch_message(channel.last_message_id)
                            last_message.content = last_message.content.lower()
                            if 'quoi' in last_message.content and last_message.author != client.user:
                                message_to_send = returned_message(last_message)
                                await channel.send(message_to_send)
                        except:
                            print(f"error detected in {channel.name} but program still running")

###################################################
###                  lancement                  ###
###################################################

client.run("MTA1MzIyOTI5ODIxMjk0MTg1NA.GtTYrZ.6WLOt582X4EKzGD5sudvlp-uGaLgGBNS0fh5SU")