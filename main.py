import os
from discord import *
from discord.ext import commands
from random import *
from csv import *
from discord.utils import get
from csv import *
import fichier_stuff as fs

client = Client()

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=";", description="Bot de clem#1777", intents=intents)

bot.remove_command('help')



@bot.event
async def on_ready():
    print("Ready !")
    activity = Game(name="$help", type=1)
    await bot.change_presence(status=Status.online, activity=activity)


# commande bonjour
@bot.command()
async def bonjour(ctx):
    """
     : vous dit bonjour
    """
    embed = Embed(title=" bonjour", description="Bonjour ! Comment vas-tu? (jmen fou mdr)", color=0x33CAFF)
    await ctx.send(embed=embed)


# commande infoserveur
@bot.command()
async def infoserveur(ctx):
    """
     : donne les informations pricipales de ce serveur
    """
    serveur = ctx.guild
    nombreDeChainesTexte = len(serveur.text_channels)
    nombreDeChainesVocale = len(serveur.voice_channels)
    Description_du_serveur = serveur.description
    Nombre_de_personnes = serveur.member_count
    Nom_du_serveur = serveur.name
    Nombre_de_roles = len(serveur.roles)

    embed = Embed(title=" information du serveur",
                  description=f"Le serveur **{Nom_du_serveur}** contient {Nombre_de_personnes} personnes ! \nLa description du serveur est {Description_du_serveur}. \nCe serveur possède {nombreDeChainesTexte} salons écrit, {nombreDeChainesVocale} salon vocaux \nEt {Nombre_de_roles} roles.",
                  color=0x33CAFF)

    await ctx.send(embed=embed)


# commande rôles
@bot.command()
async def roles(ctx):
    """
     : renvoi tous les roles d'un serveur
    """
    serv = ctx.guild
    liste_roles = []
    liste_roles1 = []
    roles_serv = serv.roles
    roles_serv.reverse()
    for role in roles_serv:
        nom = "<@&" + str(role.id) + ">"
        liste_roles.append(nom)
        if len(str(liste_roles)) > 2000:
            liste_roles1.append(liste_roles)
            liste_roles = []

    liste_roles1.append(liste_roles)
    liste_roles1[0].pop(0)

    for liste_roles in liste_roles1:
        embed = Embed(title="roles", description=str(liste_roles).replace("'", "").replace("[", "").replace("]", ""),
                      color=0x33CAFF)
        await ctx.send(embed=embed)


# message de bienvenue
@bot.event
async def on_member_join(member):
    """
     : envoi un message à l'arrivée d'un nouveau membre
    """
    try :
        serveur = member.guild
        Nombre_de_personnes = serveur.member_count
        salons = member.guild.text_channels
        roles = member.guild.roles
        for role in roles :
            if role.name == "membre" or role.name == "Membre" :
                role_membre = role
        await member.add_roles(role_membre)

        for salon in salons:
            if salon.name == "bienvenue":
                channel = salon
        embed = Embed(title="Bienvenue",
                    description=f"Bienvenue à {member.mention} sur le serveur \n Nous sommes {Nombre_de_personnes} avec toi <3",
                    color=0x33CAFF)
        await channel.send(embed=embed)
    except :
        pass

# message d'au revoir
@bot.event
async def on_member_remove(member):
    """
     : envoi un message lorsque quelqu'un quitte le serveur
    """
    try :    
        serveur = member.guild
        Nombre_de_personnes = serveur.member_count
        salons = member.guild.text_channels
        for salon in salons:
            if salon.name == "bienvenue" :
                channel = salon
        embed = Embed(title="Au revoir",
                    description=f"Au revoir à {member.name} \n Nous sommes {Nombre_de_personnes} sans toi :(",
                    color=0x33CAFF)
        await channel.send(embed=embed)
    except :
        pass

# commande bulle
@bot.command()
async def bulle(ctx, *, arg):
    """
     : fait dire au bot ce que vous voulez
    """
    embed = Embed(title=" Mes pensées", description=f"Je pense que {arg} \nenvoyé par {ctx.message.author.mention}",
                  color=0x33CAFF)
    await ctx.send(embed=embed)


# commande ping
@bot.command()
async def ping(ctx):
    """
    : renvoit pong
    """
    embed = Embed(title=" Ping-Pong", description=f"pong! ;)", color=0x33CAFF)
    await ctx.send(embed=embed)


@bot.command()
async def shino (ctx) :
    """
     : envoi un message à shino
    """
    message = "shino... cv bae?"
    embed = Embed(Title = "shinouille" , description = message , color = 0x33CAFF)
    
    await bot.get_user(462730008289345538).send(embed = embed)

   


# commande auto_goulag
liste_goulag = ["Tu devrais faire un tour au goulag", "TA PLACE C'EST AU GOULAG!!!",
                "Il y a des goulags qui se perdent"]


@bot.command()
async def auto_goulag(ctx):
    """
     : le bot pense que vous devriez aller au goulag
    """
    indice = randint(0, len(liste_goulag) - 1)
    phrase = liste_goulag[indice]
    embed = Embed(title=" auto goulag", description=f"{phrase}", color=0x33CAFF)
    await ctx.send(embed=embed)


# commande rôle goulag et ungoulag

# cherche le role Goulag dans les roles du serveur
async def getGoulagRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Goulag" or role.name == "goulag":
            return role

    # commande goulag




@bot.command(name="goulag", pass_context=True)
@commands.has_permissions(administrator=True)
async def goulag(ctx, member: Member):
    """
     : vous envoi directement au goulag
    """
    role_goulag = await getGoulagRole(ctx)

    await member.add_roles(role_goulag)
    embed = Embed(title=" AU GOULAG !!", description=f"{member.mention} vous êtes goulagisé ", color=0x33CAFF)
    await ctx.send(embed=embed)

    # commande ungoulag


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ungoulag(ctx, member: Member ):


    role_goulag = await  getGoulagRole(ctx)
    await  member.remove_roles(role_goulag)
    embed = Embed(title=" Libération du goulag",
                  description=f"{member.mention} vous êtes degoulagisé par {ctx.message.author.mention}! ",
                  color=0x33CAFF)
    await ctx.send(embed=embed)



async def getMuteRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "mute" or role.name == "Mute" or role.name == "Muted" or role.name == "muted": 
            return role



raison_mute = ""
@bot.command(name="mute", pass_context=True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: Member , *args):

    raison = str(args).replace("(","").replace(")","").replace("'","").replace(",","")
    raison_mute = raison


    role_mute = await getMuteRole(ctx)

    await member.add_roles(role_mute)
    embed = Embed(title="Mute", description=f"{member.mention} vous êtes mute par {ctx.message.author.mention} \nRaison : {raison} ", color=0x33CAFF)
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: Member ):
    

    role_mute = await  getMuteRole(ctx)
    await  member.remove_roles(role_mute)
    embed = Embed(title="Unmute",description=f"{member.mention} vous êtes unmute par {ctx.message.author.mention}" ,color=0x33CAFF)
    await ctx.send(embed=embed)





# liste des images pour la commande hug
liste_image_hug = ["https://i.imgur.com/JX6jzSf.gif", "https://i.imgur.com/q2Chvem.gif",
                   "https://i.imgur.com/wB6Iq1X.gif", "https://i.imgur.com/L9mTYVF.gif",
                   "https://i.imgur.com/khr9zw9.gif", "https://i.imgur.com/2QLJCKk.gif"]


# commande hug
@bot.command()
async def hug(ctx, arg):
    """
     : faites un calin a la personne de votre choix
    """

    indice = randint(0, len(liste_image_hug) - 1)
    embed = Embed(title=" calin", description=f"{arg} vous recevez un hug de {ctx.message.author.mention} ",
                  color=0x33CAFF)
    embed.set_image(url=liste_image_hug[indice])
    await ctx.send(embed=embed)

    # liste des images pour la commande pat


liste_image_pat = ["https://i.imgur.com/NNOz81F.gif", "https://i.imgur.com/2lacG7l.gif",
                   "https://i.imgur.com/UWbKpx8.gif", "https://i.imgur.com/LUypjw3.gif",
                   "https://i.imgur.com/4ssddEQ.gif"]


# commande pat pat
@bot.command()
async def pat(ctx, arg):
    """
    tes un pat pat a la personne de votre choix
    """

    indice = randint(0, len(liste_image_pat) - 1)
    embed = Embed(title="pat pat <3", description=f"{arg} vous vous faites pat pat par {ctx.message.author.mention}",
                  color=0x33CAFF)
    embed.set_image(url=liste_image_pat[indice])
    await ctx.send(embed=embed)


# commande pour tester les images
@bot.command()
async def octa(ctx):
    """
     :renvoi une image d'un octaling
    """
    embed = Embed(title="voila un octa <3", description=f"tiens ton octa", color=0x33CAFF)
    embed.set_image(url="https://i.imgur.com/lJ7GyCg.png")
    await ctx.channel.send(embed=embed)


# commande spam
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def spam(ctx, arg_1, arg_2: int):
    """
     : ctx = none ; arg_1 = mention ; arg_2 = int
    """
    if "<@&" in arg_1 and ">" in arg_1:
        embed_e = Embed(title="pings", description="ping pas ça espece de garnement", color=0x33CAFF)
        await ctx.send(embed = embed_e)
        
    elif "<@" in arg_1 and ">" in arg_1  :
       
        liste_message = [f"{arg_1} ramène toi wsh", f"on va appeler ta darone {arg_1}", f"{arg_1} bouge ton cul",
                         f"le FBI est devant chez {arg_1} on fait quoi?"]
        for salon in ctx.guild.text_channels :
            if salon.name == "ping" :
                channel = salon
            elif salon.name == "spam" :
                channel = salon
        
        channel_id = channel.id
        embed = Embed(title="pings", description="la commande a bien éte exécutée. rendez vous dans <#" + str(channel_id) + "> \nvous êtes ping par " + ctx.message.author.mention + "", color=0x33CAFF)

        await ctx.send(embed=embed)

        for i in range(arg_2):
            

            indice = randint(0, len(liste_message) - 1)
            message = liste_message[indice]

            await channel.send(message)
    


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def stop(ctx) :
    return 1



"""
#ajoute le role membre a tout les membres
@bot.command()
async def verif_roles(ctx) :

     : ajoute le role membre a tout le monde

    membres = ctx.guild.members
    roles_serv = ctx.guild.roles
    embed = Embed(title = "vérification des rôles" , description = "la vérification est bien enclenchée" , color = 0x33CAFF)
    await ctx.send(embed=embed)
    for role in roles_serv :
        if role.name == "Membre" or role.name == "membre":
            role_membre = role

    for membre in membres :
        if not "{Bot}" in membre.roles : 
            print(membre.roles)
            await membre.add_roles(role_membre)
        elif "{Bot}" in membre.roles :
            await membre.remove_roles(role_membre)
"""


# commande arme random
@bot.command()
async def clemw(ctx, *args) :
    """
     : vous donne une arme de splatoon 2 au hasard
    """
    liste_arg = []
    for i in args :
        
        liste_arg.append(i)

    liste_shooter = ["https://leanny.github.io/splat2/weapons/Wst_Shooter_Short_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Short_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Short_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_First_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_First_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_First_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Precision_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Precision_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Blaze_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Blaze_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Blaze_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_Oct.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Gravity_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Gravity_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Gravity_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_QuickMiddle_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_QuickMiddle_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_QuickMiddle_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Expert_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Expert_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Expert_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Heavy_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Heavy_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Long_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Long_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterShort_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterShort_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterShort_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterMiddle_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterMiddle_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterMiddle_H.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLong_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLong_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLong_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLightShort_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLightShort_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLight_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLight_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLight_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLightLong_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLightLong_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleQuick_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleQuick_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleQuick_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleMiddle_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleMiddle_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleMiddle_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Flash_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Flash_01.png"] 

    liste_roller = ["https://leanny.github.io/splat2/weapons/Wst_Roller_Compact_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Compact_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Normal_02.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Heavy_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Heavy_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Heavy_02.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Hunter_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Hunter_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushMini_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushMini_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushMini_02.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushNormal_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushNormal_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushNormal_02.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushNormal_H.png"]

    liste_charger = ["https://leanny.github.io/splat2/weapons/Wst_Charger_Quick_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Quick_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Quick_02.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Normal_02.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Charger_NormalScope_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_NormalScope_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_NormalScope_02.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Long_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Long_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_LongScope_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_LongScope_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Light_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Light_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Light_02.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Keeper_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Keeper_01.png"]

    liste_slosher = ["https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_h.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_01.png"]

    liste_splatling = ["https://leanny.github.io/splat2/weapons/Wst_Spinner_Quick_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Quick_01.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Quick_02.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Standard_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Standard_01.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Standard_02.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Standard_H.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Hyper_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Hyper_01.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Downpour_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Downpour_01.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Serein_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Serein_01.png"]

    liste_dualies = ["https://leanny.github.io/splat2/weapons/Wst_Twins_Short_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Short_01.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Short_02.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Normal_02.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Gallon_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Gallon_01.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Gallon_02.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Dual_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Dual_01.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Stepper_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Stepper_01.png"]

    liste_brella = ["https://leanny.github.io/splat2/weapons/Wst_Umbrella_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Wide_00.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Wide_01.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Wide_02.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Compact_00.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Compact_01.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Compact_02.png"]

    liste_image_armes = [
        #shooter
        "https://leanny.github.io/splat2/weapons/Wst_Shooter_Short_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Short_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Short_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_First_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_First_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_First_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Precision_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Precision_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Blaze_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Blaze_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Blaze_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Normal_Oct.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Gravity_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Gravity_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Gravity_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_QuickMiddle_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_QuickMiddle_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_QuickMiddle_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Expert_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Expert_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Expert_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Heavy_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Heavy_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Long_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Long_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterShort_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterShort_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterShort_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterMiddle_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterMiddle_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterMiddle_H.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLong_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLong_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLong_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLightShort_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLightShort_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLight_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLight_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLight_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLightLong_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_BlasterLightLong_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleQuick_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleQuick_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleQuick_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleMiddle_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleMiddle_01.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_TripleMiddle_02.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Flash_00.png","https://leanny.github.io/splat2/weapons/Wst_Shooter_Flash_01.png" ,

        #roller
        "https://leanny.github.io/splat2/weapons/Wst_Roller_Compact_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Compact_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Normal_02.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Heavy_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Heavy_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Heavy_02.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Hunter_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_Hunter_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushMini_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushMini_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushMini_02.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushNormal_00.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushNormal_01.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushNormal_02.png","https://leanny.github.io/splat2/weapons/Wst_Roller_BrushNormal_H.png" ,

        #charger
        "https://leanny.github.io/splat2/weapons/Wst_Charger_Quick_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Quick_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Quick_02.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Normal_02.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Charger_NormalScope_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_NormalScope_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_NormalScope_02.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Long_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Long_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_LongScope_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_LongScope_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Light_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Light_01.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Light_02.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Keeper_00.png","https://leanny.github.io/splat2/weapons/Wst_Charger_Keeper_01.png" ,

        #slosher
        "https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_h.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_01.png",

        #splatling
        "https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_h.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_01.png",
    
        #dualies
        "https://leanny.github.io/splat2/weapons/Wst_Twins_Short_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Short_01.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Short_02.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Normal_02.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Gallon_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Gallon_01.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Gallon_02.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Dual_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Dual_01.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Stepper_00.png","https://leanny.github.io/splat2/weapons/Wst_Twins_Stepper_01.png" ,

        #brella
        "https://leanny.github.io/splat2/weapons/Wst_Umbrella_Normal_00.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Normal_01.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Normal_H.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Wide_00.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Wide_01.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Wide_02.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Compact_00.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Compact_01.png","https://leanny.github.io/splat2/weapons/Wst_Umbrella_Compact_02.png"
    ]
    
    



    
    if len(liste_arg) == 0 or liste_arg[0]=="random":
        indice = randint(0, len(liste_image_armes) - 1)
        image = liste_image_armes[indice]
        embed = Embed(title="clem w", description=f"{ctx.message.author.mention} vous devez prendre : ", color=0x33CAFF)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    elif liste_arg[0] == "shooter":
        indice = randint(0, len(liste_shooter) - 1)
        image = liste_shooter[indice]
        embed = Embed(title="clem w", description=f"{ctx.message.author.mention} vous devez prendre : ", color=0x33CAFF)
        embed.set_image(url = image)
        await ctx.send(embed=embed)
        

    elif liste_arg[0] == "roller":
        indice = randint(0, len(liste_roller) - 1)
        image = liste_roller[indice]
        embed = Embed(title="clem w", description=f"{ctx.message.author.mention} vous devez prendre : ", color=0x33CAFF)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    elif liste_arg[0] == "charger":
        indice = randint(0, len(liste_charger) - 1)
        image = liste_charger[indice]
        embed = Embed(title="clem w", description=f"{ctx.message.author.mention} vous devez prendre : ", color=0x33CAFF)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    elif liste_arg[0] == "slosher":
        indice = randint(0, len(liste_slosher) - 1)
        image = liste_slosher[indice]
        embed = Embed(title="clem w", description=f"{ctx.message.author.mention} vous devez prendre : ", color=0x33CAFF)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    elif liste_arg[0] == "splatling":
        indice = randint(0, len(liste_splatling) - 1)
        image = liste_splatling[indice]
        embed = Embed(title="clem w", description=f"{ctx.message.author.mention} vous devez prendre : ", color=0x33CAFF)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    elif liste_arg[0] == "dualies":
        indice = randint(0, len(liste_dualies) - 1)
        image = liste_dualies[indice]
        embed = Embed(title="clem w", description=f"{ctx.message.author.mention} vous devez prendre : ", color=0x33CAFF)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    elif liste_arg[0] == "brella":
        indice = randint(0, len(liste_brella) - 1)
        image = liste_brella[indice]
        embed = Embed(title="clem w", description=f"{ctx.message.author.mention} vous devez prendre : ", color=0x33CAFF)
        embed.set_image(url=image)
        await ctx.send(embed=embed)


@bot.command()
async def invit(ctx):
    lien = "https://discord.com/api/oauth2/authorize?client_id=842442847982452816&permissions=8&scope=bot"
    embed = Embed(title="invitation", description=f"voici un lien pour m'inviter : {lien}", color=0x33CAFF)
    await ctx.send(embed=embed)


@bot.command()
async def docu(ctx):
    embed = Embed(title="documentation",
                  description=f"voici les sites utilisés pour le bot ainsi que les personnes m'ayant aidées :\n \n inkpedia -> https://splatoonwiki.org/wiki/Main_Page \n \n replit et vscode -> pour coder le bot \n \n la documentation de discord.py \n \n cocopw qui m'aide pour le code \n mishy la overtime (RIP) et beacoup d'autres pour les idées \n Bot codé par clem#1777 (discord) @clem_spl (twitter)\n\n\n merci à la region occitanie pour avoir donner le pc portable qui fait uniquemment tourner ce bot 🤡",
                  color=0x33CAFF)
    await ctx.send(embed=embed)


def addincsv(url_file,objet,newline =True, delimiter =  None):
    csv = open(url_file,'a',encoding='utf-8')
    if newline:
        csv.write((str(objet)+'\n'))
    else:
        csv.write(str(objet))
        csv.write(str(delimiter))
    csv.close()

@bot.command()  
async def citation(ctx, arg1 , arg2 ):
    """
     : arg_1 str (la citation)
    """
    
    if arg2.startswith("<@!") :
        embed = Embed(description = "veuillez mettre le nom et non une mention de la personne" , color = 0x33CAFF)
        await ctx.send(embed = embed)
    else :
        serveur = str(ctx.guild.name)
        message = f"{str(arg1)} par {str(arg2)}"
        addincsv(f"stockage/citations/citation_{serveur}.csv",message)
        embed = Embed(title="citations", description=f"voici la citations ajoutées \n{message}", color=0x33CAFF)
        await ctx.send(embed=embed)
    
@bot.command()
async def show(ctx):
    serveur = str(ctx.guild.name)
    fichier = [File(str(f"stockage/citations/citation_{serveur}")+'.csv')]
    
    embed = Embed(title="citations", description="voici les citations\n " , File = fichier  , color=0x33CAFF)
    await ctx.send(embed=embed)
    await ctx.send(files = fichier)




def verif(auteur) :
    fichier = reader(open("stockage/personne.csv"))
    
    for ligne in fichier :
        
        if str(auteur.id) == str(ligne).replace("'", "").replace("[", "").replace("]", "") :
            return(True)
            

@bot.command()
async def anniv(ctx,jour = None ,mois = None) :
    auteur = ctx.message.author
    mois = str(mois)
    if jour==None :
        await tableau(ctx)
    else :  
        if verif(auteur) == True :
            embed = Embed(title="anniversaire", description="vous avez déjà rentré cette date", color=0x33CAFF)
            await ctx.send(embed = embed)  
        
        else :
            if 1<=int(jour)<=31 and 1<=int(mois)<=12 :
            
                addincsv("stockage/personne.csv",auteur.id)
                embed = Embed(title="anniversaire", description=f"la date ajoutée est le {jour}/{mois}", color=0x33CAFF)
                await ctx.send(embed = embed)
                données = [auteur.id,[f" est né(e) le {jour}"]]
        
                if mois == "1" or  mois == "01" :
                    addincsv("mois/janvier.csv",données)
                elif mois == 2 or  mois == "02":
                    addincsv("mois/fevrier.csv",données)
                elif mois == 3 or  mois == "03":
                    addincsv("mois/mars.csv",données)
                elif mois == 4 or  mois == "04":
                    addincsv("mois/avril.csv",données)
                elif mois == 5 or  mois == "05":
                    addincsv("mois/mai.csv",données)
                elif mois == 6 or  mois == "06":
                    addincsv("mois/juin.csv",données)
                elif mois == 7 or  mois == "07":
                    addincsv("mois/juillet.csv",données)
                elif mois == 8 or  mois == "08":
                    addincsv("mois/aout.csv",données)
                elif mois == 9 or  mois == "09":
                    addincsv("mois/septembre.csv",données)
                elif mois == 10 or  mois == "10":
                    addincsv("mois/octobre.csv",données)
                elif mois == 11 or  mois == "11":
                    addincsv("mois/novembre.csv",données)
                elif mois == 12 or  mois == "12":
                    addincsv("mois/decembre.csv",données)   
                    
            else :
                embed = Embed(title="anniversaire", description=f"le format de date n'est pas correct \nveuillez essayer sous la forme 'jour mois'",color=0x33CAFF)
                await ctx.send(embed = embed)         
                

@bot.command()
async def tableau(ctx) :
    membre = ctx.author
#janvier
    noms_janvier = []
    jour_janvier = []
    message_janvier = ""
    janvier = reader(open("mois/janvier.csv"))
    for data in janvier :
        noms_janvier.append(data[0])
        jour_janvier.append(data[1])
   
    
    for i in range(len(noms_janvier)) :
        a=noms_janvier[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = bot.get_user(int(a))
        b=jour_janvier[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_janvier = message_janvier + str(personne) + str(b) + str("""
""")


    embed_janvier = Embed(title = "janvier" , description = f"voici les personnes nées en janvier : \n {message_janvier}" , color = 0x33CAFF)
    #await membre.send( embed = embed_janvier)

#fevrier
    noms_fevrier = []
    jour_fevrier = []
    message_fevrier = ""
    fevrier = reader(open("mois/fevrier.csv"))
    for data in fevrier :
        noms_fevrier.append(data[0])
        jour_fevrier.append(data[1])
    print(noms_fevrier)
    
    for i in range(len(noms_fevrier)) :
        a=noms_fevrier[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_fevrier[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_fevrier = message_fevrier + str(personne) + str(b) + str("""
""")
    
    embed_fevrier = Embed(title = "fevrier" , description = f"voici les personnes nées en fevrier : \n {message_fevrier}" , color = 0x33CAFF)
    #await membre.send( embed = embed_fevrier)


#mars
    noms_mars = []
    jour_mars = []
    message_mars = ""
    mars = reader(open("mois/mars.csv"))
    for data in mars :
        noms_mars.append(data[0])
        jour_mars.append(data[1])
    print(noms_mars)
    
    for i in range(len(noms_mars)) :
        a=noms_mars[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_mars[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_mars = message_mars + str(personne) + str(b) + str("""
""")

    embed_mars = Embed(title = "mars" , description = f"voici les personnes nées en mars : \n {message_mars}" , color = 0x33CAFF)
    #await membre.send( embed = embed_mars)


#avril
    noms_avril = []
    jour_avril = []
    message_avril = ""
    avril = reader(open("mois/avril.csv"))
    for data in avril :
        noms_avril.append(data[0])
        jour_avril.append(data[1])
    print(noms_avril)
    
    for i in range(len(noms_avril)) :
        a=noms_avril[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_avril[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_avril = message_avril + str(personne) + str(b) + str("""
""")

    embed_avril = Embed(title = "avril" , description = f"voici les personnes nées en avril : \n {message_avril}" , color = 0x33CAFF)
    #await membre.send( embed = embed_avril)
    


    embed_1_4 = Embed(title = "anniversaires" , description = f"Voici les personnes nées en mai : \n {message_janvier} \n \nVoici les personnes nées en fevrier : \n {message_fevrier} \n \nVoici les personnes nées en mars : \n {message_mars}\n \nVoici les personnes nées en avril : \n {message_avril}" , color = 0x33CAFF )
    await membre.send(embed = embed_1_4)    


#mai
    noms_mai = []
    jour_mai = []
    message_mai = ""
    mai = reader(open("mois/mai.csv"))
    for data in mai :
        noms_mai.append(data[0])
        jour_mai.append(data[1])
    print(noms_mai)
    
    for i in range(len(noms_mai)) :
        a=noms_mai[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_mai[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_mai = message_mai + str(personne) + str(b) + str("""
""")

    embed_mai = Embed(title = "mai" , description = f"voici les personnes nées en mai : \n {message_mai}" , color = 0x33CAFF)
    #await membre.send( embed = embed_mai)


#juin
    noms_juin = []
    jour_juin = []
    message_juin = ""
    juin = reader(open("mois/juin.csv"))
    for data in juin :
        noms_juin.append(data[0])
        jour_juin.append(data[1])
    print(noms_juin)
    
    for i in range(len(noms_juin)) :
        a=noms_juin[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_juin[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_juin = message_juin + str(personne) + str(b) + str("""
""")

    embed_juin = Embed(title = "juin" , description = f"voici les personnes nées en juin : \n {message_juin}" , color = 0x33CAFF)
    


#juillet
    noms_juillet = []
    jour_juillet = []
    message_juillet = ""
    juillet = reader(open("mois/juillet.csv"))
    for data in juillet :
        noms_juillet.append(data[0])
        jour_juillet.append(data[1])
    print(noms_juillet)
    
    for i in range(len(noms_juillet)) :
        a=noms_juillet[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_juillet[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_juillet = message_juillet + str(personne) + str(b) + str("""
""")

    embed_juillet = Embed(title = "juillet" , description = f"voici les personnes nées en juillet : \n {message_juillet}" , color = 0x33CAFF)
    #await membre.send( embed = embed_juillet)


#aout
    noms_aout = []
    jour_aout = []
    message_aout = ""
    aout = reader(open("mois/aout.csv"))
    for data in aout :
        noms_aout.append(data[0])
        jour_aout.append(data[1])
    print(noms_aout)
    
    for i in range(len(noms_aout)) :
        a=noms_aout[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_aout[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_aout = message_aout + str(personne) + str(b) + str("""
""")

    embed_aout = Embed(title = "aout" , description = f"voici les personnes nées en aout : \n {message_aout}" , color = 0x33CAFF)
    #await membre.send( embed = embed_aout)


    embed_4_8 = Embed(title = "anniversaires" , description = f"Voici les personnes nées en mai : \n {message_mai} \n \nVoici les personnes nées en juin : \n {message_juin} \n \nVoici les personnes nées en juillet : \n {message_juillet}\n \nVoici les personnes nées en aout : \n {message_aout}" , color = 0x33CAFF )
    await membre.send(embed = embed_4_8)





#septembre
    noms_septembre = []
    jour_septembre = []
    message_septembre = ""
    septembre = reader(open("mois/septembre.csv"))
    for data in septembre :
        noms_septembre.append(data[0])
        jour_septembre.append(data[1])
    print(noms_septembre)
    
    for i in range(len(noms_septembre)) :
        a=noms_septembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_septembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_septembre = message_septembre + str(personne) + str(b) + str("""
""")

    embed_septembre = Embed(title = "septembre" , description = f"voici les personnes nées en septembre : \n {message_septembre}" , color = 0x33CAFF)
    #await membre.send( embed = embed_septembre)


#octobre
    noms_octobre = []
    jour_octobre = []
    message_octobre = ""
    octobre = reader(open("mois/octobre.csv"))
    for data in octobre :
        noms_octobre.append(data[0])
        jour_octobre.append(data[1])
    print(noms_octobre)
    
    for i in range(len(noms_octobre)) :
        a=noms_octobre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_octobre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_octobre = message_octobre + str(personne) + str(b) + str("""
""")

    embed_octobre = Embed(title = "octobre" , description = f"voici les personnes nées en octobre : \n {message_octobre}" , color = 0x33CAFF)
    #await membre.send( embed = embed_octobre)


#novembre
    noms_novembre = []
    jour_novembre = []
    message_novembre = ""
    novembre = reader(open("mois/novembre.csv"))
    for data in novembre :
        noms_novembre.append(data[0])
        jour_novembre.append(data[1])
    print(noms_novembre)
    
    for i in range(len(noms_novembre)) :
        a=noms_novembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_novembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_novembre = message_novembre + str(personne) + str(b) + str("""
""")

    embed_novembre = Embed(title = "novembre" , description = f"voici les personnes nées en novembre : \n {message_novembre}" , color = 0x33CAFF)
    #await membre.send( embed = embed_novembre)


#decembre
    noms_decembre = []
    jour_decembre = []
    message_decembre = ""
    decembre = reader(open("mois/decembre.csv"))
    for data in decembre :
        noms_decembre.append(data[0])
        jour_decembre.append(data[1])
    print(noms_decembre)
    
    for i in range(len(noms_decembre)) :
        a=noms_decembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        
        b=jour_decembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        message_decembre = message_decembre + str(personne) + str(b) + str("""
""")

    embed_decembre = Embed(title = "decembre" , description = f"voici les personnes nées en decembre : \n {message_decembre}" , color = 0x33CAFF)
    #await membre.send( embed = embed_decembre)

    embed_8_12 = Embed(title = "anniversaires" , description = f"Voici les personnes nées en septembre : \n {message_septembre} \n \nVoici les personnes nées en cotobre : \n {message_octobre} \n \nVoici les personnes nées en novembre : \n {message_novembre}\n \nVoici les personnes nées en decembre : \n {message_decembre}" , color = 0x33CAFF )
    await membre.send(embed = embed_8_12)



@bot.command()
async def stuff(ctx,*args) :
    """
     : 12 arguments -> (ssu,rsu,scu,spu,ss,qsj,qr,os,mpu,iss,ism,bdu,cbl,ir,iru,dr,lde,sbpu,tnty,hnt,ns,thi,rsp,sj,og)
    """
    
    
    embed_message = Embed(description = f" sous quelle forme voulez vous votre stuff? ⏺ : emoji ou ⏹ : image\nNote : l'image peut prendre du temps à s'afficher " , color = 0x33CAFF)

    message = await ctx.send(embed = embed_message)
    await message.add_reaction("⏺")
    await message.add_reaction("⏹")


    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "⏺" or str(reaction.emoji) == "⏹")

 

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 20, check = checkEmoji)
        
        if reaction.emoji == "⏺" :
            stuf = []
            liste = []
            for n in args :
        
                liste.append(n)
            i = 0
            returne = True

            while i != 12:
                try:
                    if liste[i] == 'ssu' or liste[i] == "Ssu" or liste[i] == "SSU" :
                        stuf.append('<:ssu:855390371827023882>')
                        i += 1
                    elif liste[i] == 'rsu'or liste[i] == "Rsu" or liste[i] == "RSU":
                        stuf.append('<:rsu:855390367264407572>')
                        i += 1
                    elif liste[i] == 'scu' or liste[i] == "Scu" or liste[i] == "SCU":
                        stuf.append('<:scu:855390371840000001>')
                        i += 1
                    elif liste[i] == 'spu' or liste[i] == "Spu" or liste[i] == "SPU":
                        stuf.append('<:spu:855390372254318622>')
                        i += 1
                    elif liste[i] == 'ss' or liste[i] == "Ss" or liste[i] == "SS":
                        stuf.append('<:ss:855390372129144842>')
                        i += 1
                    elif liste[i] == 'qsj' or liste[i] == "Qsj" or liste[i] == "QSJ":
                        stuf.append('<:qsj:855390367745310750>')
                        i += 1
                    elif liste[i] == 'qr' or liste[i] == "Qr" or liste[i] == "QR":
                        stuf.append('<:qr:855390372208312330>')
                        i += 1
                    elif liste[i] == 'os' or liste[i] == "Os" or liste[i] == "OS":
                        stuf.append('<:os:855390368778027038>')
                        i += 1
                    elif liste[i] == 'mpu' or liste[i] == "Mpu" or liste[i] == "MPU":
                        stuf.append('<:mpu:855390368131842068>')
                        i += 1
                    elif liste[i] == 'iss' or liste[i] == "Iss" or liste[i] == "ISS":
                        stuf.append('<:iss:855390372125868063>')
                        i += 1
                    elif liste[i] == 'ism' or liste[i] == "Ism" or liste[i] == "ISM":
                        stuf.append('<:ism:855390367586975745>')
                        i += 1
                    elif liste[i] == 'bdu' or liste[i] == "Bdu" or liste[i] == "BDU":
                        stuf.append('<:bdu:855390365708058624>')
                        i += 1
                    elif liste[i] == 'cbk' or liste[i] == "Cbk" or liste[i] == "CBK":
                        stuf.append('<:cbk:855390366157242388>')
                        i += 1
                    elif liste[i] == 'ir' or liste[i] == "Ir" or liste[i] == "IR":
                        stuf.append('<:ir:855390370362556436>')
                        i += 1
                    elif liste[i] == 'dr' or liste[i] == "Dr" or liste[i] == "DR":
                        stuf.append('<:dr:855390372204773387>')
                        i += 1
                    elif liste[i] == 'iru' or liste[i] == "Iru" or liste[i] == "IRU":
                        stuf.append('<:iru:855390367464292352>')
                        i += 1
                    elif liste[i] == 'lde' or liste[i] == "Lde" or liste[i] == "LDE":
                        stuf.append('<:lde:855390366755717120>')
                        i += 1
                    elif liste[i] == 'sbpu' or liste[i] == "Sbpu" or liste[i] == "SBPU":
                        stuf.append('<:sbpu:855390365895753749>')
                        i += 1
                    elif liste[i] == 'tnty' or liste[i] == "Tnty" or liste[i] == "TNTY":
                        stuf.append('<:tnty:855390368065388576>')
                        i += 1
                    elif liste[i] == 'hnt' or liste[i] == "Hnt" or liste[i] == "HNT":
                        stuf.append('<:hnt:855390366453989426>')
                        i += 1
                    elif liste[i] == 'ns' or liste[i] == "Ns" or liste[i] == "NS":
                        stuf.append('<:ns:855390376185692180>')
                        i += 1
                    elif liste[i] == 'thi' or liste[i] == "Thi" or liste[i] == "THi":
                        stuf.append('<:ti:855390376374304798>')
                        i += 1
                    elif liste[i] == 'rsp' or liste[i] == "Rsp" or liste[i] == "RSP":
                        stuf.append('<:rp:855390366991646730>')
                        i += 1
                    elif liste[i] == 'sj' or liste[i] == "Sj" or liste[i] == "SJ":
                        stuf.append('<:sj:855390376235892756>')
                        i += 1
                    elif liste[i] == 'og' or liste[i] == "Og" or liste[i] == "OG":
                        stuf.append('<:og:855390372141465610>')
                        i += 1
                    elif liste[i] == 'ab' or liste[i] == "Ab" or liste[i] == "AB":
                        stuf.append('<:ab:855479824009527306> ')
                        i += 1
                    elif liste[i] == 'uk' or liste[i] == "?" or liste[i] == "Uk" or liste[i] == "UK" :
                        stuf.append('<:uk:855479856511057951>')
                        i += 1
                    else:
                        returne = False
                        break
                    if i == 4 or i == 8:
                        stuf.append('newline')


                except:
                    break
            if returne:
                a = str(stuf)

                a = a.replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace('newline', '''
                ''').replace('         ','')
                
                embed = Embed(title = "stuff" , description = f"{a}" , color = 0x33CAFF)

                await ctx.send(embed = embed)
            else:
                embed = Embed(title = "bonus inconnu" , description = 'le bonus n°' + str(i) + ' est introuvable' , color = 0x33CAFF)
                await ctx.send(embed = embed)
            
            

        elif reaction.emoji == "⏹" :
            stuf = []
            liste = []
            for n in args :
        
                liste.append(n)
            i = 0
            returne = True

            while i != 12:
                try:
                    if liste[i] == 'ssu' or liste[i] == "Ssu" or liste[i] == "SSU" :
                        fs.ssu(i+1)
                        i += 1
                    elif liste[i] == 'rsu'or liste[i] == "Rsu" or liste[i] == "RSU":
                        fs.rsu(i+1)
                        i += 1
                    elif liste[i] == 'scu' or liste[i] == "Scu" or liste[i] == "SCU":
                        fs.scu(i+1)
                        i += 1
                    elif liste[i] == 'spu' or liste[i] == "Spu" or liste[i] == "SPU":
                        fs.spu(i+1)
                        i += 1
                    elif liste[i] == 'ss' or liste[i] == "Ss" or liste[i] == "SS":
                        fs.ss(i+1)
                        i += 1
                    elif liste[i] == 'qsj' or liste[i] == "Qsj" or liste[i] == "QSJ":
                        fs.qsj(i+1)
                        i += 1
                    elif liste[i] == 'qr' or liste[i] == "Qr" or liste[i] == "QR":
                        fs.qr(i+1)
                        i += 1
                    elif liste[i] == 'os' or liste[i] == "Os" or liste[i] == "OS":
                        fs.os(i+1)
                        i += 1
                    elif liste[i] == 'mpu' or liste[i] == "Mpu" or liste[i] == "MPU":
                        fs.mpu(i+1)
                        i += 1
                    elif liste[i] == 'iss' or liste[i] == "Iss" or liste[i] == "ISS":
                        fs.iss(i+1)
                        i += 1
                    elif liste[i] == 'ism' or liste[i] == "Ism" or liste[i] == "ISM":
                        fs.ism(i+1)
                        i += 1
                    elif liste[i] == 'bdu' or liste[i] == "Bdu" or liste[i] == "BDU":
                        fs.bdu(i+1)
                        i += 1
                    elif liste[i] == 'cbk' or liste[i] == "Cbk" or liste[i] == "CBK":
                        fs.cbk(i+1)
                        i += 1
                    elif liste[i] == 'ir' or liste[i] == "Ir" or liste[i] == "IR":
                        fs.ir(i+1)
                        i += 1
                    elif liste[i] == 'dr' or liste[i] == "Dr" or liste[i] == "DR":
                        fs.dr(i+1)
                        i += 1
                    elif liste[i] == 'iru' or liste[i] == "Iru" or liste[i] == "IRU":
                        fs.iru(i+1)
                        i += 1
                    elif liste[i] == 'lde' or liste[i] == "Lde" or liste[i] == "LDE":
                        fs.lde(i+1)
                        i += 1
                    elif liste[i] == 'sbpu' or liste[i] == "Sbpu" or liste[i] == "SBPU":
                        fs.sbpu(i+1)
                        i += 1
                    elif liste[i] == 'tnty' or liste[i] == "Tnty" or liste[i] == "TNTY":
                        fs.tnty(i+1)
                        i += 1
                    elif liste[i] == 'hnt' or liste[i] == "Hnt" or liste[i] == "HNT":
                        fs.hnt(i+1)
                        i += 1
                    elif liste[i] == 'ns' or liste[i] == "Ns" or liste[i] == "NS":
                        fs.ns(i+1)
                        i += 1
                    elif liste[i] == 'thi' or liste[i] == "Thi" or liste[i] == "THi":
                        fs.thi(i+1)
                        i += 1
                    elif liste[i] == 'rsp' or liste[i] == "Rsp" or liste[i] == "RSP":
                        fs.rsp(i+1)
                        i += 1
                    elif liste[i] == 'sj' or liste[i] == "Sj" or liste[i] == "SJ":
                        fs.sj(i+1)
                        i += 1
                    elif liste[i] == 'og' or liste[i] == "Og" or liste[i] == "OG":
                        fs.og(i+1)
                        i += 1
                    elif liste[i] == 'ab' or liste[i] == "Ab" or liste[i] == "AB":
                        fs.ab(i+1)
                        i += 1
                    elif liste[i] == 'uk' or liste[i] == "?" or liste[i] == "Uk" or liste[i] == "UK" :
                        fs.uk(i+1)
                        i += 1
                    else:
                        returne = False
                        break            
                    

                except:
                    break
            if returne:
                        
                embed = Embed(title = "stuff" , description = f"voici le stuff en image" , color = 0x33CAFF)

                await ctx.send(embed = embed)

                await ctx.send(file = File(r"images_bot/emote_stuff/blanc_resultat.png")) 
                
                for i in range(1,12) :
                    fs.clear(i)
                

            else:
                embed = Embed(title = "bonus inconnu" , description = 'le bonus n°' + str(i) + ' est introuvable' , color = 0x33CAFF)
                await ctx.send(embed = embed)
                
                for i in range(1,12) :
                    fs.clear(i)
    except :
        pass


@bot.command()
async def scrim(ctx,arg1) :
    
    liste_map = ["https://cdn.wikimg.net/en/splatoonwiki/images/thumb/f/f7/S2_Stage_The_Reef.png/200px-S2_Stage_The_Reef.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/c/cd/S2_Stage_Musselforge_Fitness.png/200px-S2_Stage_Musselforge_Fitness.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/3/31/S2_Stage_Starfish_Mainstage.png/200px-S2_Stage_Starfish_Mainstage.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/e/ed/S2_Stage_Humpback_Pump_Track.png/200px-S2_Stage_Humpback_Pump_Track.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/c/c9/S2_Stage_Inkblot_Art_Academy.png/200px-S2_Stage_Inkblot_Art_Academy.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/6/62/S2_Stage_Sturgeon_Shipyard.png/200px-S2_Stage_Sturgeon_Shipyard.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/7/7e/S2_Stage_Manta_Maria.png/200px-S2_Stage_Manta_Maria.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/3/37/S2_Stage_Moray_Towers.png/200px-S2_Stage_Moray_Towers.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/f/f0/S2_Stage_Kelp_Dome.png/200px-S2_Stage_Kelp_Dome.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/9/91/S2_Stage_Snapper_Canal.png/200px-S2_Stage_Snapper_Canal.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/11/S2_Stage_Blackbelly_Skatepark.png/200px-S2_Stage_Blackbelly_Skatepark.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/6/6a/S2_Stage_Walleye_Warehouse.png/200px-S2_Stage_Walleye_Warehouse.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/6/6c/S2_Stage_Shellendorf_Institute.png/200px-S2_Stage_Shellendorf_Institute.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/4/49/S2_Stage_Port_Mackerel.png/200px-S2_Stage_Port_Mackerel.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/d/d4/S2_Stage_MakoMart.png/200px-S2_Stage_MakoMart.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/f/f5/S2_Stage_Arowana_Mall.png/200px-S2_Stage_Arowana_Mall.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/d/d0/S2_Stage_Goby_Arena.png/200px-S2_Stage_Goby_Arena.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/e/ef/S2_Stage_Camp_Triggerfish.png/200px-S2_Stage_Camp_Triggerfish.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/14/S2_Stage_Wahoo_World.png/200px-S2_Stage_Wahoo_World.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/d/da/S2_Stage_New_Albacore_Hotel.png/200px-S2_Stage_New_Albacore_Hotel.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/2/20/S2_Stage_Ancho-V_Games.png/200px-S2_Stage_Ancho-V_Games.png","https://cdn.wikimg.net/en/splatoonwiki/images/thumb/1/10/S2_Stage_Skipper_Pavilion.png/200px-S2_Stage_Skipper_Pavilion.png"]

    liste_modes = ["<:sz:853656465423990807>","<:rm:853656465725456424>","<:tc:853656463846146068>","<:cb:853656449825243166>","<:sz:853656465423990807>","<:rm:853656465725456424>","<:tc:853656463846146068>","<:cb:853656449825243166>","<:sz:853656465423990807>"]

    liste_modes2 = liste_modes
    mode = ""
    map_scrim = []
    liste_map_2 = liste_map
    compteur = 0
    if arg1 == "bo3" or arg1 == "3" :
        for i in range(3) :
            indice=randint(0,len(liste_map_2)-1)

            map_scrim.append(liste_map_2[indice])
            mode = liste_modes2[i]
            
            liste_map_2.pop(indice)
            compteur+=1
            embed = Embed(title = f"map n°{compteur} en : {mode} " ,color = 0x33CAFF)
            embed.set_image(url = map_scrim[i])
            await ctx.message.author.send(embed = embed)
    
    
    if arg1 == "bo5" or arg1 == "5" :
        for i in range(5) :
            indice=randint(0,len(liste_map_2)-1)
            
            map_scrim.append(liste_map_2[indice])
            mode = liste_modes2[i]
            
            liste_map_2.pop(indice)
            compteur+=1
            embed = Embed(title = f"map n°{compteur} en : {mode} " ,color = 0x33CAFF)
            embed.set_image(url = map_scrim[i])
            
            await ctx.message.author.send(embed = embed)

    if arg1 == "bo7" or arg1 == "7" :
        for i in range(7) :
            indice=randint(0,len(liste_map_2)-1)
            map_scrim.append(liste_map_2[indice])
            liste_map_2.pop(indice)
            mode = liste_modes2[i]
            compteur+=1
            liste_embed = []
            embed = Embed(title = f"map n°{compteur} en : {mode} " ,color = 0x33CAFF)
            embed.set_image(url = map_scrim[i])
            
            embed_bo7 = Embed(title = "bo7" , description = liste_embed , color = 0x33CAFF)
            await ctx.message.author.send(embed = embed)

    if arg1 == "bo9" or arg1 == "9" :
        for i in range(9) :
            indice=randint(0,len(liste_map_2)-1)
            map_scrim.append(liste_map_2[indice])
            liste_map_2.pop(indice)
            mode = liste_modes2[i]
            compteur+=1
            liste_embed = []
            embed = Embed(title = f"map n°{compteur} en : {mode} " ,color = 0x33CAFF)
            embed.set_image(url = map_scrim[i])
            
            embed_bo7 = Embed(title = "bo9" , description = liste_embed , color = 0x33CAFF)
            await ctx.message.author.send(embed = embed)
            
              
    #await ctx.send(map_scrim)        


@bot.command(name="role", pass_context=True)
@commands.has_permissions(administrator=True)
async def role(ctx,arg1 : Member , *args) :
    removerole = ""
    liste = []
    liste_roles = ctx.guild.roles
    for i in args :
        liste.append(i)

    removerole =  str(liste).replace("[","").replace("]","").replace("'","").replace(",","")
    print(removerole)
    for role in liste_roles :
        if role.name == removerole :
            removerole = role
            break
    membre = arg1
    await membre.add_roles(removerole)
    embed = Embed(title = "roles" , description=f"{membre.mention} a maintenant le rôle {removerole}" , color = 0x33CAFF)
    await ctx.send(embed = embed)


@bot.command(name="unrole", pass_context=True)
@commands.has_permissions(administrator=True)
async def unrole(ctx,arg1 : Member , *args) :
    removerole = ""
    liste = []
    liste_roles = ctx.guild.roles
    for i in args :
        liste.append(i)

    removerole =  str(liste).replace("[","").replace("]","").replace("'","").replace(",","")
    print(removerole)
    for role in liste_roles :
        if role.name == removerole :
            removerole = role
            break
    membre = arg1
    await membre.remove_roles(removerole)
    embed = Embed(title = "roles" , description=f"{membre.mention} n'a plus le rôle {removerole}" , color = 0x33CAFF)
    await ctx.send(embed = embed)


@bot.command()
async def voc (ctx) :
    embed = Embed(title = "vocabulaire compétitif splatoon" , description = "Tu es nouveau sur splatoon et tu veux connaître le vocabulaire compétitif? \n  Ca tombe bien car Ap6 a fait un document regroupant tout le vocabulaire et tu peux le retrouver ici \n  ➡https://docs.google.com/document/d/1_JCLlDEbeojN8XuVCTj2vLXlPljzQD56dqSHE5HfdOI/edit" , color = 0x33CAFF)
    await ctx.send(embed = embed)



def import_csv(url_file, delimiter) :
    with open(url_file, newline='', encoding='utf-8') as csvfile :
        file = reader(csvfile, delimiter=delimiter)
        list_list = []
        for row in file :
            list_list.append(row)
    return list_list

def suprligne(url, n):
    f = open(url,"r+")
    d = f.readlines()
    f.seek(0)
    for i in range(len(d)):
        
        if i != n:
            f.write(d[i])
    f.truncate()
    f.close()
    


@bot.command() # context is automatically passed in rewrite
async def info(ctx , membre : Member = None):
    if membre == None :
        pp = f"{str(ctx.author.avatar_url)[:-4]}128"
        nom = ctx.author.name
        ping = ctx.author.mention
        ID = ctx.author.id
        crea = ctx.author.created_at

    else :
        pp = f"{str(membre.avatar_url)[:-4]}128"
        nom = membre.name
        ping = membre.mention
        ID = membre.id
        crea = membre.created_at

    embed = Embed(description = f"voici les informations sur {ping} : \n" , color = 0x33CAFF)

    embed.set_author(name=nom , icon_url = pp)

    embed.add_field(name="ID", value=ID, inline=False)

    embed.add_field(name="date de création du compte", value=crea, inline=False)

    embed.add_field(name=f"photo de profil", value=f"voici la photo de profil de {nom}", inline=True)
    embed.set_image(url = pp )

    embed.set_footer(text = f"Informations demandées par {ctx.author.name}")

    await ctx.send(embed = embed)



@bot.command()
async def pp(ctx , membre : Member=None) :
    if membre == None :
        image = f"{str(ctx.author.avatar_url)[:-4]}128" 
        embed = Embed(Title = "photo de profil" , description = f"voici la photo de profil de {ctx.author.mention}" , color = 0x33CAFF)
        embed.set_image(url=  image)
        await ctx.send(embed = embed)


    else :
        image = f"{str(membre.avatar_url)[:-4]}128" 
        embed = Embed(Title = "photo de profil" , description = f"voici la photo de profil de {membre.mention}" , color = 0x33CAFF)
        embed.set_image(url=  image)
        await ctx.send(embed = embed)


def verif_code(code) :
    liste = []
    chiffre = [0,1,2,3,4,5,6,7,8,9]

    for caractere in code :
        liste.append(caractere)
    
    verif = True
    
    
    if len(liste) != 17 :
        verif = False

    elif str(liste[0]+liste[1]) != "SW" :
        verif = False

    elif liste[2] != "-" or liste[7] != "-" or liste[12] != "-" :
        verif = False
        
    elif int(liste[3]) not in chiffre or int(liste[4]) not in chiffre or int(liste[5]) not in chiffre or int(liste[6]) not in chiffre or int(liste[8]) not in chiffre or int(liste[9]) not in chiffre or int(liste[10]) not in chiffre or int(liste[11]) not in chiffre or int(liste[13]) not in chiffre or int(liste[14]) not in chiffre or int(liste[15]) not in chiffre or int(liste[16]) not in chiffre :
        verif = False      

    return(verif)



@bot.command()
async def add(ctx):
    fichier = reader(open("stockage/code_amis.csv"))
    code_amis = ""
    test = False
    cpt_lignes = 0
    for ligne in fichier :
        
        a = str(ligne[0]).replace("[","")
        cpt_lignes += 1
        if str(ctx.author.id) == a :
            test = True
             
            break

    
    if test == False :
        embed_ca = Embed(description = "Veuillez renseigner votre code amis sous la forme\nSW-0000-0000-0000" , color = 0x33CAFF)
        await ctx.send(embed = embed_ca)

        embed_error = Embed(description = "Veuillez réitérer la commande." , color = 0x33CAFF)

        def checkMessage(message):
	        return message.author == ctx.message.author and ctx.message.channel == message.channel

        try:
	        ca = await bot.wait_for("message", timeout = 45, check = checkMessage)
        except:
            await ctx.send(embed = embed_error)
            return
         

        if verif_code(ca.content) == True :
    
            embed_message = Embed(description = f"Veuillez valider votre code amis en réagissant avec ?\n{ca.content}.\n Sinon réagissez avec ❌" , color = 0x33CAFF)

            message = await ctx.send(embed = embed_message)
            await message.add_reaction("✅")
            await message.add_reaction("❌")


            def checkEmoji(reaction, user):
    	        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

            embed_valid = Embed(description = f"votre code amis ({ca.content}) est bien enregistré" , color = 0x33CAFF)
            embed_annul = Embed(description = f"votre code amis n'a pas été enregistré" , color = 0x33CAFF)

    
            ajout = [ctx.author.id , ca.content]
            

            try:
                reaction, user = await bot.wait_for("reaction_add", timeout = 20, check = checkEmoji)
        
                if reaction.emoji == "✅" :
            
                    await ctx.send(embed = embed_valid) and addincsv("stockage/code_amis.csv" , ajout)
            
        
            except:
	            await ctx.send(embed = embed_annul)
    
        else :
            embed_invalid = Embed(description = f"votre code amis n'a pas été enregistré car il ne semble pas valide" , color = 0x33CAFF)
            await ctx.send(embed = embed_invalid)
    else :
        
        fichier = reader(open("stockage/code_amis.csv"))
        code = ""
        for ligne in fichier :
            tempo =  str(ligne[0]).replace("'", "").replace("[", "").replace("]", "")
            
            if str(ctx.author.id) == tempo:
                code = str(ligne[1]).replace("'", "").replace("[", "").replace("]", "")
                
                
                embed_envoi = Embed(description = f"vous avez déjà entré un code amis : \n{code}" , color = 0x33CAFF)
                await ctx.send(embed = embed_envoi)

                embed_renvoi = Embed(description = f"si vous voulez entrer un nouveau code ajoutez la réaction 🔄" , color = 0x33CAFF)
                
                mess = await ctx.send(embed = embed_renvoi)

                await mess.add_reaction("🔄")

                embed_annul = Embed(description = f"votre code amis n'a pas été enregistré" , color = 0x33CAFF)

                def checkEmoji(reaction, user):
    	                return ctx.message.author == user  and (str(reaction.emoji) == "🔄") 
                
                reaction, user = await bot.wait_for("reaction_add", timeout = 20, check = checkEmoji)
        
                if reaction.emoji == "🔄" :

                    embed_ca = Embed(description = "Veuillez renseigner votre code amis sous la forme\nSW-0000-0000-0000" , color = 0x33CAFF)
                    await ctx.send(embed = embed_ca)

                    embed_error = Embed(description = "Veuillez réitérer la commande." , color = 0x33CAFF)

                    def checkMessage(message):
	                    return message.author == ctx.message.author and ctx.message.channel == message.channel

                    try:
	                    ca = await bot.wait_for("message", timeout = 15, check = checkMessage)
                    except:
                        await ctx.send(embed = embed_error)
                        return
        
                    if verif_code(ca.content) == True :

                        embed_message = Embed(description = f"Veuillez valider votre code amis en réagissant avec ?\n{ca.content}.\n Sinon réagissez avec ❌" , color = 0x33CAFF)

                        message = await ctx.send(embed = embed_message)
                        await message.add_reaction("✅")
                        await message.add_reaction("❌")


                        def checkEmoji(reaction, user):
    	                    return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

                        embed_valid = Embed(description = f"votre code amis ({ca.content}) est bien enregistré" , color = 0x33CAFF)
                        embed_annul = Embed(description = f"votre code amis n'a pas été enregistré" , color = 0x33CAFF)

    
                        ajout = [ctx.author.id , ca.content]
            

                        try:
                            reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
        
                            if reaction.emoji == "✅" :
                            
                                
                                suprligne("stockage/code_amis.csv",cpt_lignes-1) 
                                addincsv("stockage/code_amis.csv" , ajout) 
                                await ctx.send(embed = embed_valid)
                   
                
                
                        except:

	                        await ctx.send(embed = embed_annul)

                    else :
                        embed_invalid = Embed(description = f"votre code amis n'a pas été enregistré car il ne semble pas valide" , color = 0x33CAFF)
                        await ctx.send(embed = embed_invalid)

                break


@bot.command(name = "code" , alias = "ca")
async def code(ctx , membre : Member = None) :
    
    if membre == None :
        membre = ctx.author



    fichier = reader(open("stockage/code_amis.csv"))

    a=False

    for ligne in fichier :

        tempo =  str(ligne[0]).replace("'", "").replace("[", "").replace("]", "")
            
        if str(membre.id) == tempo:
            code = str(ligne[1]).replace("'", "").replace("[", "").replace("]", "")

            embed_1 = Embed(description = f"le code amis de {membre.mention} est : \n {code}" , color = 0x33CAFF)

            await ctx.send(embed = embed_1)
            a=True
            break
        else :
            a=False

    if a==False :
        embed_1 = Embed(description = f"Votre code amis n'est pas enregistré. Veuillez le rentrer via la commande add." , color = 0x33CAFF)

        await ctx.send(embed = embed_1)
        



# embed commande bot_help
@bot.command()
async def thelp(ctx):
    """
     : commande du bot pour les aides
    """
    membre = ctx.author
    embed_help_1 = Embed(title="help clem 3eme du nom" , description="-> invit : vous donne un lien pour inviter ce bot\n \n-> infoserveur : donne les informations pricipales de ce serveur\n \n-> bulle : fait dire au bot ce que vous voulez\n  \n-> goulag : vous envoi directement au goulag \n \n-> ungoulag : vous sort du goulag\n \n-> hug : faites un calin a la personne de votre choix \n \n-> pat : faites un pat pat a la personne de votre choix \n \n-> spam: commande spéciale (demander a clem#1777)\n \n-> clemw : vous donne une arme au hasard \n   ou vous pouvez choisir parmis :\n   random ; shooter ; roller ; charger\n   slosher ; splatling ; dualies ; brella \n \n-> stuff affiche votre stuff en emojis\n   voivci les emojis possibles et leur noms :\n   ssu -> <:ssu:799259849732653096> ; rsu -> <:rsu:799259849044262924> ; scu -> <:scu:799259849446916097> ; spu -> <:spu:799259849665019924>\n   ss -> <:ss:799259849404973077> ; qsj -> <:qsj:799259849442983966> ; qr -> <:Qr:799259849249914901> ; os -> <:os:799259849326067775> \n   mpu -> <:mpu:799259849484402705> ; iss -> <:iss:799259849803825183> ; ism -> <:ism:799259849409298433> ; bdu -> <:bdu:799259849128804353> \n   cbk -> <:Cbk:799259849362767912> ; ir -> <:ir:799259849517957152> ; iru -> <:iru:799259849471819806> ; dr -> <:dr:799259849690054696> \n   lde -> <:lde:799259849359097896> ; sbpu -> <:sbpu:799259849422536754> ; tnty -> <:tnty:799259849501573170> ; hnt -> <:DeathMarking:799259849468805120> \n   ns -> <:ns:799259849857826827> ; thi -> <:thi:799259849799106560> ; rsp -> <:rp:799259849384001546> ; sj -> <:sl:799259849425813535> \n   og -> <:og:799259849786785832> ; ab -> <:ad:852154177869709363> ; uk ou ?-> <:__:852153879650893935>  \n \n-> scrim : sur des maps aléatoires\n   bo3 : vous fait jouer sur les 3 premiers modes <:sz:853656465423990807> ; <:rm:853656465725456424> ; <:tc:853656463846146068>   \n   bo5 : vous fait jouer sur tous les modes et sur une autre zone \n   bo7 vous fait jouer 2 fois sur chaque modes sauf clam \n   bo9 vous fait jouer 2 fois sur chaque modes et une autre dz" , color=0x33CAFF)
    embed_help_2 = Embed(title = "help clem 3eme du nom" , description = "-> citation : ajoute une citation et la personne qui l'a pronnoncée (sous la forme $citation 'message' membre)\n \n-> anniv : ajoutez votre anniversaire en faisant la commande $anniv 'jour' 'mois' (ATTENTION vous ne pouvez l'éxecuter qu'une seule fois)\n \n-> tableau : vous montre les anniversaires des personnes ayant renseigné leur anniversaire\n \n-> role/unrole : ajoute ou enlève un role ($role @personne 'nom exact du role')\n \n-> voc : vous indique un fichier sur les calls de splatoon2\n \n-> pp : montre votre photo de profil (sans ping) ou celle de vos amis (avec ping)\n \n-> info : montre les informations d'un profil \n \n-> add : ajoute votre code amis \n \n-> code : montre votre code amis (sans ping) ou celui de vos amis (avec ping) \n \n-> Si vous avez besoin de plus d'aide veuillez contacter clem#1777 sur discord" , color = 0x33CAFF)
    embed_help_3 = Embed(title = "help clem 3eme du nom" , description = f"-> Si vous avez besoin de plus d'aide veuillez contacter clem#1777 sur discord" , color = 0x33CAFF)

    embed_help_1.set_footer(text= f"1/3")
    embed_help_2.set_footer(text= f"2/3")    
    embed_help_3.set_footer(text= f"3/3")

    await membre.send (embed = embed_help_1)
    await membre.send (embed = embed_help_2)
    await membre.send (embed = embed_help_3)

@bot.command()
async def help(ctx) :
    if not "Direct Message" in str(ctx.channel) :
        membre = ctx.author
        embed_help_1 = Embed(title = "help clem 3eme du nom" , description = f"-> invit : vous donne un lien pour inviter ce bot\n \n-> infoserveur : donne les informations pricipales de ce serveur\n \n-> bulle : fait dire au bot ce que vous voulez\n  \n-> goulag : vous envoi directement au goulag \n \n-> ungoulag : vous sort du goulag\n \n-> hug : faites un calin a la personne de votre choix \n \n-> pat : faites un pat pat a la personne de votre choix \n \n-> spam: commande spéciale (demander a clem#1777)\n \n-> clemw : vous donne une arme au hasard \n   ou vous pouvez choisir parmis :\n   random ; shooter ; roller ; charger\n   slosher ; splatling ; dualies ; brella \n \n-> stuff : affiche votre stuff en emojis\n   voici les emojis possibles et leur noms :\n   ssu -> <:ssu:799259849732653096> ; rsu -> <:rsu:799259849044262924> ; scu -> <:scu:799259849446916097> ; spu -> <:spu:799259849665019924>\n   ss -> <:ss:799259849404973077> ; qsj -> <:qsj:799259849442983966> ; qr -> <:Qr:799259849249914901> ; os -> <:os:799259849326067775> \n   mpu -> <:mpu:799259849484402705> ; iss -> <:iss:799259849803825183> ; ism -> <:ism:799259849409298433> ; bdu -> <:bdu:799259849128804353> \n   cbk -> <:Cbk:799259849362767912> ; ir -> <:ir:799259849517957152> ; iru -> <:iru:799259849471819806> ; dr -> <:dr:799259849690054696> \n   lde -> <:lde:799259849359097896> ; sbpu -> <:sbpu:799259849422536754> ; tnty -> <:tnty:799259849501573170> ; hnt -> <:DeathMarking:799259849468805120> \n   ns -> <:ns:799259849857826827> ; thi -> <:thi:799259849799106560> ; rsp -> <:rp:799259849384001546> ; sj -> <:sl:799259849425813535> \n   og -> <:og:799259849786785832> ; ab -> <:ad:852154177869709363> ; uk ou ?-> <:__:852153879650893935>  \n \n-> scrim : sur des maps aléatoires\n   bo3 : vous fait jouer sur les 3 premiers modes <:sz:853656465423990807> ; <:rm:853656465725456424> ; <:tc:853656463846146068>   \n   bo5 : vous fait jouer sur tous les modes et sur une autre zone \n   bo7 vous fait jouer 2 fois sur chaque modes sauf clam \n   bo9 vous fait jouer 2 fois sur chaque modes et une autre dz" , color=0x33CAFF)
        embed_help_2 = Embed(title = "help clem 3eme du nom" , description = f"-> citation : ajoute une citation et la personne qui l'a pronnoncée (sous la forme $citation 'message' membre)\n \n-> anniv : ajoutez votre anniversaire en faisant la commande $anniv 'jour' 'mois' (ATTENTION vous ne pouvez l'éxecuter qu'une seule fois)\n \n-> tableau : vous montre les anniversaires des personnes ayant renseigné leur anniversaire\n \n-> role/unrole : ajoute ou enlève un role ($role @personne 'nom exact du role')\n \n-> voc : vous indique un fichier sur les calls de splatoon2\n \n-> pp : montre votre photo de profil (sans ping) ou celle de vos amis (avec ping)\n \n-> info : montre les informations d'un profil \n \n-> add : ajoute votre code amis \n \n-> code : montre votre code amis (sans ping) ou celui de vos amis (avec ping) \n \n-> delete 'nombre de messages' : (à noter qu'il faur certaines permissions)\n \n-> syracuse 'nombre' : vous renvoi le maximum atteint et le nombre de tours\n \n-> data : vous envoi le nom exact des armes nécesaire à la commande match\n \n-> match '8 armes' : renvoi des compositions équitables\n \n-> matchr : renvoi des compositions équitables aléatoire\n \n-> set_role 'nom du role' un emoji quelconque : (nécessite un salon role) permet d'obtenir un role" , color = 0x33CAFF)
        embed_help_3 = Embed(title = "help clem 3eme du nom" , description = f"-> Si vous avez besoin de plus d'aide veuillez contacter clem#1777 sur discord" , color = 0x33CAFF)

        embed_help_1.set_footer(text= f"1/3")
        embed_help_2.set_footer(text= f"2/3")    
        embed_help_3.set_footer(text= f"3/3")

        message = await ctx.send(embed = embed_help_1)
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
    


        def checkEmoji(reaction, user):
    	    return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "◀️" or str(reaction.emoji) == "▶️" )

        embed_valid = Embed(description = f"votre code amis  est bien enregistré" , color = 0x33CAFF)
        embed_annul = Embed(description = f"votre code amis n'a pas été enregistré" , color = 0x33CAFF)
    
        a=True
        cpt=1
    
        while a == True :
            reaction, user = await bot.wait_for("reaction_add", timeout = None, check = checkEmoji)
        
            if reaction.emoji == "▶️" :  

                if cpt==1 :
                    cpt+=1 
                    await message.edit(embed = embed_help_2)
                    await message.remove_reaction(emoji = "▶️" , member = membre)
                elif cpt==2 :
                    cpt += 1
                    await message.edit(embed = embed_help_3)
                    await message.remove_reaction(emoji = "▶️" , member = membre)

                    
            
        
            elif reaction.emoji == "◀️" :   
                if cpt==2 :
                    cpt -= 1 
                    await message.edit(embed = embed_help_1)
                    await message.remove_reaction(emoji = "◀️" , member = membre)
                elif cpt==3 :
                    cpt -= 1
                    await message.edit(embed = embed_help_2)
                    await message.remove_reaction(emoji = "◀️" , member = membre)
    else :
        await thelp(ctx)
        
    
@bot.command(name="delete", pass_context=True)
@commands.has_permissions(administrator=True)
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for message in messages:
        await message.delete()
    
    await ctx.send(f"{number} messages ont été supprimés")




@bot.command(name="set_role", pass_context=True)
@commands.has_permissions(administrator=True)
async def set_role(ctx , role , react) :

    print(role)

    channel = ""
    s = False
    for salon in ctx.guild.text_channels :
        if salon.name == "role" or salon.name == "rôle" or salon.name == "roles" or salon.name == "rôles":
            channel = salon
            s = True
            break
    
    role_add =""
    r=False
    for roles in ctx.guild.roles :
        
        if str(roles.id) in role :
            role_add = roles
            r = True
            break

    a=""

    if s==False :    
        await ctx.send("vous devez créer un salon role")


    else :
        for i in str(role) :
            if i == "@" :
        
                a = str(role).replace("@","")
            else :
                a = role
        print(a)
        role_add = await ctx.guild.create_role(name = a)
    
        embed_mess = Embed(description = f"Ajoutez la réaction {react} si vous voulez le role {a}" , color = 0x33CAFF)
        message = await bot.get_channel(channel.id).send(embed = embed_mess)
        await message.add_reaction(react)

        def checkEmoji(reaction, user):
    	    return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == react  )

        
        reaction, user = await bot.wait_for("reaction_add", timeout = None, check = checkEmoji)
        liste = []
        if reaction.emoji == react :
                    
                
            async for user in reaction.users():
                liste.append(user)
                    
            personne = liste[1]
            print(liste)

            await personne.add_roles(role_add)

            liste.pop(1)
            print(liste)

@bot.command()
async def syracuse(ctx,nombre : int) :
    a=nombre
    max = nombre
    cpt = 0
    verif = False
    while verif == False :
        if nombre == 1 :
            verif = True
        if int(nombre)%2 == 0 :
            nombre = nombre / 2
            cpt+=1
        else :
            nombre = int(nombre)*3  +1
            cpt+=1
        if nombre > max : 
            max = nombre

    embed = Embed(description = f"le maximum du problème de syracuse pour {a} est : {max} \n {a} s'arrête pour la valeur : {cpt} " , color = 0x33CAFF)
    await ctx.send(embed = embed)
        



data = {
    ".52-Gal" : 133,
    ".96-Gal" : 180,
    "Aerospray" : 110,
    "Jet-Squelcher" : 225,
    "N-Zap" : 125,
    "Splash-o-matic" : 117,
    "Splattershot" : 125,
    "Splattershot Jr" : 110,
    "Splattershot Pro" : 170,
    "Sploosh-o-matic" : 80,
    "L-3" : 135,
    "H-3" : 170,
    "Dapple-Dualies" : 95,
    "Splat-Dualies" : 125,
    "Glooga-Dualies" : 160,
    "Dualie-Squelchers" : 170,
    "Tetra-Dualies" : 140,
    "Squiffer" : 182,
    "Splat-Charger" : 260,
    "Splatterscope" : 280,
    "E-litre" : 310,
    "E-Litre-Scope" : 330,
    "Baboozler 14" : 210,
    "Goo-Tuber" : 210,
    "Mini-Splatling" : 150,
    "Heavy-Splatling" : 210,
    "Hydra-Splatling" : 245,
    "Ballpoint-Splatling" : 245,
    "Nautilus" : 180,
    "Luna-Blaster" : 110,
    "Blaster" : 133,
    "Range-Blaster" : 170,
    "Clash-Blaster" : 110,
    "Rapid-Blaster" : 169,
    "Rapid-Blaster-Pro" : 192,
    "Slosher" : 145,
    "Tri-Slosher" : 110,
    "Sloshing-Machine" : 147,
    "Bloblober" : 150,
    "Explosher" : 207,
    "Splat-Brella" : 125,
    "Tenta-Brella" : 150,
    "Undercover-Brella" : 118,
    "Carbon-Roller" : 95,
    "Splat-Roller" : 118,
    "Dynamo-Roller" : 185,
    "Flingza-Roller" : 140,
    "Inkbrush" : 70,
    "Octobrush" : 105,
}


async def erreur(ctx) :
    embed_message = Embed(description = f"ll doit y avoir une erreur\n Voulez vous que je vous envoi le nom de chaque arme?" , color = 0x33CAFF)

    message = await ctx.send(embed = embed_message)
    await message.add_reaction("✅")
    await message.add_reaction("❌")


    def checkEmoji(reaction, user):
    	return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    embed_valid = Embed(description = f"Je vous l'envoi" , color = 0x33CAFF)
    embed_annul = Embed(description = f"D'accord, dans ce cas veuilez réessayer en vérifiant le nom des armes." , color = 0x33CAFF)
    embed_times_up = Embed(description = f"désolé le temps est écoulé 🙁" , color = 0x33CAFF)

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 5, check = checkEmoji)
        if reaction.emoji == "✅" :
                
            await ctx.send(embed = embed_valid) and await ctx.message.author.send(f"```py\n{data}\n```")
        else :
            await message.edit(embed = embed_annul)
            
        
    except:
        await message.remove_reaction(emoji = "✅" , member = message.author)
        await message.remove_reaction(emoji = "❌" , member = message.author)
        await message.edit(embed = embed_times_up)
	    

from itertools import combinations

async def combi(ctx,liste,tout) :
    temp=combinations(liste,len(liste)//2)
    try :
        for combinaisons in list(temp) :
            somme = 0
            for e in liste:
                somme += data[e]
            m=somme/len(liste)
            tout[combinaisons] = m
    except :
        await erreur(ctx)            


def find(armes,liste_tri) :
    try :
        mid=len(liste_tri)//2
        e1=liste_tri[mid-1]
        e2=liste_tri[mid]
        return e1,e2
    except :
        pass

def tri(tout,tout_liste) :
    for k, v in sorted(tout.items(), key=lambda x: x[1]):
        tout_liste.append([k,v])
    return tout_liste

def verif_armes(armes,l1,l2) :
    temp=[]
    for i in range(len(armes)) :

        if armes[i] in l1[0] or armes[i] in l2[0] :
            temp.append(armes[i])

    if len(temp)==len(armes) :
        
        return True
    else :
        
        return False


async def mm(ctx,armes : list , dico :dict = data) :
    tout = {}
    tout_liste=[]
    await combi(ctx,armes,tout)
    liste_tri=tri(tout,tout_liste)

    equipe1,equipe2=find(armes,liste_tri)

    if verif_armes(armes,equipe1,equipe2) == True :
        
        return (armes,equipe1,equipe2)
    else :
        print("recursivité")
        return await mm(ctx,random_comp())

@bot.command()
async def match(ctx,*args) :

    try :
        tout = {}
        tout_liste=[]
        armes=[]
        for i in args :
            armes.append(i)

        await combi(ctx,armes,tout)
        liste_tri=tri(tout,tout_liste)

        equipe1,equipe2=find(armes,liste_tri)
            
        if verif_armes(armes,equipe1,equipe2) == True :
            power_1=equipe1[-1]
            power_2=equipe2[-1]
            equipe1.pop(-1)
            equipe2.pop(-1)
            armes=str(armes).replace("[","").replace("]","").replace("'","").replace(","," ")
            equipe1=str(equipe1).replace("(","").replace(")","").replace("'","").replace(","," ").replace("[","").replace("]","")
            equipe2=str(equipe2).replace("(","").replace(")","").replace("'","").replace(","," ").replace("[","").replace("]","")
            embed=Embed(description=f"Avec les armes :\n{str(armes)}\n des équipes équitables seraient : \n \néquipe1 : {equipe1} avec un power moyen de {power_1}\néquipe2 : {equipe2} avec un power moyen de {power_2}",color=0x33CAFF)
            await ctx.send(embed=embed)
        else :
            a,equipe1,equipe2=await mm(ctx,random_comp())
            power_1=equipe1[-1]
            power_2=equipe2[-1]
            equipe1.pop(-1)
            equipe2.pop(-1)
            a=str(a).replace("[","").replace("]","").replace("'","").replace(","," ")
            equipe1=str(equipe1).replace("(","").replace(")","").replace("'","").replace(","," ").replace("[","").replace("]","")
            equipe2=str(equipe2).replace("(","").replace(")","").replace("'","").replace(","," ").replace("[","").replace("]","")
            embed=Embed(description=f"Avec les armes :\n{str(a)}\n des équipes équitables seraient : \n \néquipe1 : {equipe1} avec un power moyen de {power_1}\néquipe2 : {equipe2} avec un power moyen de {power_2}",color=0x33CAFF)
            await ctx.send(embed=embed)

    except :
        pass


@bot.command()
async def matchr(ctx) :
    try :
        armes,equipe1,equipe2=await mm(ctx,random_comp())
        if armes==None :
            armes,equipe1,equipe2=await mm(ctx,random_comp())
        else :
            power_1=equipe1[-1]
            power_2=equipe2[-1]
            equipe1.pop(-1)
            equipe2.pop(-1)
            armes=str(armes).replace("[","").replace("]","").replace("'","").replace(","," ")
            equipe1=str(equipe1).replace("(","").replace(")","").replace("'","").replace(","," ").replace("[","").replace("]","")
            equipe2=str(equipe2).replace("(","").replace(")","").replace("'","").replace(","," ").replace("[","").replace("]","")
            embed=Embed(description=f"Avec les armes :\n{str(armes)}\n des équipes équitables seraient : \n \néquipe1 : {equipe1} avec un power moyen de {power_1}\néquipe2 : {equipe2} avec un power moyen de {power_2}",color=0x33CAFF)
            await ctx.send(embed=embed)
    except :
        pass


from random import *

def random_comp(n=8):
    """Crée une liste d'armes de longueur n."""
    liste = []
    for i in range(n):
        v = randint(1, len(data) - 1)
        liste.append(list(data.keys())[v])
    return liste



import youtube_dl
import asyncio
from discord import FFmpegPCMAudio

musics = {}
dico = {}
ytdl = youtube_dl.YoutubeDL()


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]
       

@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []

@bot.command()
async def dc(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []


@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()
        await ctx.send("je reprend la lecture")


@bot.command()
async def pause(ctx , url = None):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()
        await ctx.send("pause")
    
    else :
        await resume(ctx)
    


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()
    await ctx.send("je change de son")


def play_song(client, queue, song):
    source = PCMVolumeTransformer(FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        try :
            if len(queue) > 0:
                new_song = queue[0]
                del queue[0]
                play_song(client, queue, new_song)
            else:
                asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)
        except :
            pass

    client.play(source, after=next)


@bot.command()
async def play(ctx, *args):
    a=[]
    for i in args :
        a.append(i)
    url = str(a).replace("[","").replace("]","").replace("'","").replace(","," ")
    
    try :
        client = ctx.guild.voice_client

        if client and client.channel:
            video = Video(url)
            musics[ctx.guild].append(video)
            
        else:
            await ctx.send("J'arrive, je traite votre demande")
            channel = ctx.author.voice.channel
            video = Video(url)
            musics[ctx.guild] = []
            client = await channel.connect()
            play_song(client, musics[ctx.guild], video)  
            embed_musique = Embed(title = f"Musique" , description = f"je lance la musique : ")
            embed_musique.url(url=video.url)
            await ctx.send(embed = embed_musique)
            
    except :
        await ctx.send("il y a eu une erreur")

@bot.command()
async def queue(ctx) :
    f
    if len(musics[ctx.guild])>=1 :
        await ctx.send(musics[ctx.guild])
    else :
        await ctx.send("il n'y a pas d'autres videos")
    

                            
token = os.environ['token']
token1 = os.environ['token1']


bot.run(token1)