from genericpath import exists
import os
from venv import create
import discord.ui as bt
from discord import *
from discord.ext import commands
from random import *
from csv import *
from discord.utils import get
from csv import *
import fichier_stuff as fs
from oui import *
import test_schedule as test


client = Client()

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="$", description="Bot de clem#1777", intents=intents)

bot.remove_command('help')


@bot.event
async def on_ready():
    print("Ready !")
    activity = Game(name=f"$help\nOn {len(bot.guilds)} servers", type=1)
    await bot.change_presence(status=Status.online, activity=activity)

@bot.command()
async def report(ctx, *args):

    clem = bot.get_user(485851523247505409)

    await clem.send(f"{ctx.author} a éffectué la commande dans '{ctx.channel}' dans le serveur '{ctx.guild}'")
    await clem.send(str(args).replace("(","").replace('"',"").replace("'", "").replace(",", "").replace(")", ""))

    files = ctx.message.attachments
    for elt in files:
        temp : File = await elt.to_file()
        await clem.send(file=temp)

    test = await ctx.channel.create_invite()
    await clem.send(test)

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
        try:
            for role in roles :
                if role.name == "membre" or role.name == "Membre" :
                    role_membre = role
            await member.add_roles(role_membre)
        except:
            pass
        
        for salon in salons:
            if salon.name == "bienvenue":
                channel = salon
        embed = Embed(title="Bienvenue",
                    description=f"Bienvenue à {member.mention} sur le serveur \n Nous sommes {Nombre_de_personnes} avec toi <3",
                    color=0x33CAFF)
        
        image = f"{str(member.avatar_url)[:-4]}128" 

        embed.set_thumbnail(url = image)

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

        image = f"{str(member.avatar_url)[:-4]}128" 

        embed.set_thumbnail(url = image)
        
        await channel.send(embed=embed)
    except :
        pass


@bot.command()
async def splatnet(ctx):
    for i in range(6):
        data : test.Stuff = test.get_stuff(indice=i)
        dico = {'fields': [
            {'inline': True, 'name': "New Price", 'value': f"{data.new_price} <:sp_coin:1010654259425062952>"}, 
            {'inline': True, 'name': "New Ability", 'value': data.new_main_emote},
            
            {'inline': True, 'name': "Brand", 'value': data.brand},
            {'inline': True, 'name': "Frequent Bonus", 'value': f"{data.frequent_bonus} {data.frequent_bonus_emote}"},
            
            ], 'color': 3394303, 'type': 'rich', 'description': f"Available until {data.end_time}", "title" : data.name_stuff}
        embed_stuff = Embed.from_dict(dico)
        embed_stuff.set_thumbnail(url=data.gear_url)
        await ctx.send(embed=embed_stuff)


@bot.command()
async def salmon(ctx):
    data = test.get_salmon()
    dico = {'fields': [
            {'inline': True, 'name': 'Maps :', 'value': data.current_map }, 
            {'inline': True, 'name': 'Weapons :', 'value': data.current_weapon_list},
            {'inline': True, 'name': "Date", 'value': f"{data.current_start_time} \nto \n{data.current_end_time}"},
            {'inline': False, 'name': "--------------------", 'value': f"Next Rotation \n**--------------------**"},
            {'inline': True, 'name': 'Next Map :', 'value': data.next_map }, 
            {'inline': True, 'name': 'Next Weapons :', 'value': data.next_weapon_list},
            {'inline': True, 'name': "Date", 'value': f"{data.next_start_time} \nto \n{data.next_end_time}"},
            ], 'color': 3394303, 'type': 'rich', 'description': "", "title" : "Salmon Run"}
    embed_salmon = Embed.from_dict(dico)

    await ctx.send(embed=embed_salmon)

@bot.command()
async def rotation(ctx):
    for key in test.list_mode:
        liste_rota = test.get_data(key)
        data1 = liste_rota[0]
        data2 = liste_rota[1]
        dico = {'fields': [
            {'inline': True, 'name': 'Maps :', 'value': data1.current_maps }, 
            {'inline': True, 'name': 'Next Maps :', 'value': data2.current_maps }, 
            {'inline': False, 'name': 'Mode :', 'value': data1.current_mode},
            {'inline': False, 'name': 'Next Mode :', 'value': data2.current_mode},             
            ], 'color': 3394303, 'type': 'rich', 'description': f"__Available as from {data1.current_start_time} to {data1.current_end_time}__", 'title': data1.type}
        embed = Embed.from_dict(dico)
        
        if key == "regularSchedules":
            embed.set_thumbnail(url="http://splating.ink/turf.png")
        elif key == "xSchedules":
            embed.set_thumbnail(url="http://splating.ink/rank.png")
        elif key == "bankaraSchedules":
            embed.set_thumbnail(url="http://splating.ink/rank.png")
        
        embed.add_field(name="Additional Informations", value=f"[link to splatoon2.ink](https://splatoon2.ink/)")

        await ctx.send(embed=embed)


@bot.command()
async def map(ctx):
    await rotation(ctx)

# @bot.command()
# async def last(ctx, number=0):
#     await ctx.send(f"collecting data, it might take some time")

#     config = Config("../token/config.json")
#     splatnet = Splatnet2(config)
#     results = splatnet.results()
#     ilisible = splatnet.result(results.results[int(number)].battle_number)
#     my_team, ennemy_team, game_stats = splatnet.get_results(ilisible)

#     res_my_team = ""
#     for mess in my_team:
#         res_my_team = res_my_team + mess
#     embed_my_team = Embed(title="My Team", description=res_my_team, color=0x33CAFF)

#     res_ennemy = ""
#     for mess in ennemy_team:
#         res_ennemy = res_ennemy + mess
#     embed_ennemy = Embed(title="Ennemy Team", description=res_ennemy, color=0x33CAFF)

#     embed_game = Embed(title="Game Infos", description=game_stats, color=0x33CAFF)
#     await ctx.send(embed=embed_my_team)
#     await ctx.send(embed=embed_ennemy)
#     await ctx.send(embed=embed_game)


# @bot.command()
# async def stats(ctx, number):
#     if 1<=number<=50 :
#         await last(ctx, number-1)
#     else:
#         await ctx.send("le numéro de la partie doit être compris en 1 et 50")

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

    liste_slosher = ["https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_H.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_01.png"]

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
        "https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Strong_H.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Diffusion_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Launcher_02.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Bathtub_01.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_00.png","https://leanny.github.io/splat2/weapons/Wst_Slosher_Washtub_01.png",

        #splatling
        "https://leanny.github.io/splat2/weapons/Wst_Spinner_Quick_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Quick_01.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Quick_02.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Standard_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Standard_01.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Standard_02.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Standard_H.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Hyper_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Hyper_01.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Downpour_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Downpour_01.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Serein_00.png","https://leanny.github.io/splat2/weapons/Wst_Spinner_Serein_01.png",
    
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
    embed = Embed(title="Documentation",
                  description=f"voici les sites utilisés pour le bot ainsi que les personnes m'ayant aidées :\n \n inkpedia -> [inkpedia](https://splatoonwiki.org/wiki/Main_Page) \n \n pour les armes -> [site de spike](https://leanny.github.io/splat2new/database.html) \n  \n Pour les informations de splatnet ->  [splatoon.ink](https://splatoon2.ink) \n \n Mon IDE pour coder le bot -> Visual Studio Code \n \n la documentation de discord.py -> [discord.py](https://discordpy.readthedocs.io/en/latest/api.html) \n \n cocopw qui m'a aidé pour le code \n mishy et la overtime (RIP) et beacoup d'autres pour les idées \n Bot codé par clem#1777 (discord) @clem_spl (twitter) \n  \n-> Bot hébergé sur Alwaisdata.net (gratuit)",
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
        addincsv(f"citations/citation_{serveur}.csv",message)
        embed = Embed(title="citations", description=f"voici la citations ajoutées \n{message}", color=0x33CAFF)
        await ctx.send(embed=embed)
    
@bot.command()
async def show(ctx):
    serveur = str(ctx.guild.name)
    fichier = [File(str(f"citations/citation_{serveur}")+'.csv')]
    
    embed = Embed(title="citations", description="voici les citations\n " , File = fichier  , color=0x33CAFF)
    await ctx.send(embed=embed)
    await ctx.send(files = fichier)




def verif(auteur) :
    fichier = reader(open("personne.csv"))
    
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
            
                addincsv("personne.csv",auteur.id)
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
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_fevrier)) :
        a=noms_fevrier[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_mars)) :
        a=noms_mars[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_avril)) :
        a=noms_avril[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_mai)) :
        a=noms_mai[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_juin)) :
        a=noms_juin[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_juillet)) :
        a=noms_juillet[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_aout)) :
        a=noms_aout[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_septembre)) :
        a=noms_septembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_octobre)) :
        a=noms_octobre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    
    for i in range(len(noms_novembre)) :
        a=noms_novembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    
    for i in range(len(noms_decembre)) :
        a=noms_decembre[i].replace("'", "").replace("[", "").replace("]", "").replace('"',"").replace(",","")
        personne = f"<@{a}>"
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
    fs.clear()
    if args == () :
        embed = Embed(description=f"Il faut mettre des bonus \n vous pouvez les trouver dans la commande help", color = 0x33CAFF)
        await ctx.send(embed = embed)

    else :

        embed_message = Embed(description = f" sous quelle forme voulez vous votre stuff? ⏺ : emoji ou ⏹ : image\nNote : l'image peut prendre du temps à s'afficher \nVous pouvez également sauvgegarder ce stuff si vous choississez l'image" , color = 0x33CAFF)

        message = await ctx.send(embed = embed_message)
        await message.add_reaction("⏺")
        await message.add_reaction("⏹")


        def checkEmoji(reaction, user):
            return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "⏺" or str(reaction.emoji) == "⏹")

        try:
            reaction, user = await bot.wait_for("reaction_add", timeout = 45, check = checkEmoji)

            if reaction.emoji == "⏺" :
                stuf = []
                liste = []
                for n in args :
                    liste.append(n)
                
                for i in range(12-len(args)) :
                    liste.append("uk") 

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

                for i in range(12-len(args)) :
                    liste.append("uk") 

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

                    embed = Embed(title="stuff", description=f"voici le stuff en image", color=0x33CAFF)

                    await ctx.send(embed=embed)

                    await ctx.send(file=File(r"images_bot/emote_stuff/blanc_resultat.png"))

                    embed_message = Embed(description=f"Voulez vous sauvegarder ce stuff?", color=0x33CAFF)

                    message = await ctx.send(embed=embed_message)
                    await message.add_reaction("✅")
                    await message.add_reaction("❌")

                    try :

                        def checkEmoji(reaction, user):
                            return ctx.message.author == user and message.id == reaction.message.id and (
                                    str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

                        reaction, user = await bot.wait_for("reaction_add", timeout=20, check=checkEmoji)
                        

                        if reaction.emoji == "✅":
                            
                            try :
                                def checkMessage(message):
                                    return message.author == ctx.message.author and ctx.message.channel == message.channel
                                
                                await ctx.send("choississez un nom pour votre stuff")
                                nom_stuff = await bot.wait_for("message", timeout=45 , check = checkMessage)
                                nom_stuff = nom_stuff.content
                                nom_stuff = str(nom_stuff).replace(" ","_").replace("+","_")
                                id = ctx.author.id

                                if not exists(f"stuffs/{id}") :
                                    
                                    os.mkdir(f"stuffs/{id}")
                                    fs.save(id,nom_stuff)
                                    with open(f"stuffs/{id}/{id}","wb") as csvfile:
                                        filewriter = writer(csvfile, delimiter=',', quotechar='|', quoting=QUOTE_MINIMAL)

                                    addincsv(f"stuffs/{id}/{id}.csv",nom_stuff)
                                    await ctx.send(f"sauvegarde éffectuée")
                                    fs.clear()


                                else :
                                    
                                    if not verif_stuff(id,nom_stuff) :
                                        message = await ctx.send(f"Ce nom de stuff existe déjà \nVoulez vous remplacer l'image du stuff {nom_stuff}")
                                        await message.add_reaction("✅")
                                        await message.add_reaction("❌")

                                        try :
                                            def checkEmoji(reaction, user):
                                                return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

                                            reaction, user = await bot.wait_for("reaction_add", timeout=20, check=checkEmoji)

                                            if reaction.emoji == "✅":
                                                await ctx.send("Stuff sauvegardé")
                                                fs.save(id,nom_stuff)
                                            
                                            elif reaction.emoji == "❌" :
                                                await ctx.send("D'accord j'annule la sauvegarde")
                                                fs.clear()
                                        
                                        except :
                                            embed = Embed(description = f"Les 30 secondes sont passées")
                                            await ctx.send(embed = embed)
                                    
                                    else :
                                        fs.save(id,nom_stuff)
                                        addincsv(f"stuffs/{id}/{id}.csv",nom_stuff)
                                        await ctx.send(f"sauvegarde éffectuée")
                                        fs.clear()
                            except :
                                pass

                        elif reaction.emoji == "❌" :
                            await message.delete()
                    
                        else :
                            pass

                    except :
                        embed = Embed(description = f"Les 30 secondes sont passées")
                        await ctx.send(embed = embed)


                else:
                    embed = Embed(title="bonus inconnu", description='le bonus n°' + str(i+1) + ' est introuvable',
                                  color=0x33CAFF)
                    await ctx.send(embed=embed)

                    fs.clear()
        except :
            embed = Embed(description = f"Les 45 secondes sont passées")
            await ctx.send(embed = embed)

def verif_stuff(nom,nom_stuff) :
    fichier = reader(open(f"stuffs/{nom}/{nom}.csv"))
    
    for ligne in fichier:
        a = str(ligne[0]).replace("[", "")
        if nom_stuff == a:
            return False
    return True


@bot.command()
async def mes_stuffs(ctx) :
    id = ctx.author.id
    membre = ctx.author
    try :
        fichier = reader(open(f"stuffs/{id}/{id}.csv"))
        
        await ctx.send(f"le reste se passe en mp")

        for ligne in fichier:
            a = str(ligne[0])
            url = f"stuffs/{id}/{a}"
            await membre.send(f"votre stuff {a}")
            await membre.send(file = File(rf"stuffs/{id}/{a}.png"))

    except :
        await ctx.send(f"il faut enregistrer vos stuffs avec la commande $stuff")

@bot.command()
async def mes_stuff(ctx) :
    id = ctx.author.id
    membre = ctx.author
    try :
        fichier = reader(open(f"stuffs/{id}/{id}.csv"))
        
        await ctx.send(f"le reste se passe en mp")

        for ligne in fichier:
            a = str(ligne[0])
            url = f"stuffs/{id}/{a}"
            await membre.send(f"votre stuff {a}")
            await membre.send(file = File(rf"stuffs/{id}/{a}.png"))

    except :
        await ctx.send(f"il faut enregistrer vos stuffs avec la commande $stuff")

@bot.command()
async def rename(ctx) :
    await ctx.send(f"la suite se passe en mp pour ne pas flood")
    
    membre = ctx.author
    id = ctx.author.id
    
    await membre.send(f"Entrez le nom du stuff voulez vous renomer\n(Faites la commande $mes_stuffs pour tous les voir)")
    
    def checkMessage(message):
	    return message.author == ctx.message.author and ctx.message.channel == message.channel

    nom_stuff = await bot.wait_for("message", timeout=60 ,check = checkMessage)
    nom_stuff = nom_stuff.content
    nom_stuff = str(nom_stuff).replace(" ","_").replace("+","_")

    fichier = reader(open(f"stuffs/{id}/{id}.csv"))
    i=0
    for ligne in fichier :
        if str(ligne[0]) == str(nom_stuff) :
            message = await membre.send(f"vous voules renomer ce stuff : {ligne[0]}")
            await message.add_reaction("✅")
            await message.add_reaction("❌")
            try :
                def checkEmoji(reaction, user):
                    return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")                        
                        
                reaction, user = await bot.wait_for("reaction_add", timeout=30, check=checkEmoji)
                        
                if reaction.emoji == "✅":
                    vieux = ligne[0]

                    await membre.send("Entrez le nouveau nom")
                    nouveau_nom = await bot.wait_for("message", timeout=60 ,check = checkMessage)
                    nouveau_nom = nouveau_nom.content
                    nouveau_nom = str(nouveau_nom).replace(" ","_").replace("+","_")
                    
                    if not verif_stuff(id,nouveau_nom) :
                        message = await ctx.send(f"Ce nom de stuff existe déjà \nVoulez vous remplacer l'image du stuff {nouveau_nom} par {nom_stuff}")
                        await message.add_reaction("✅")
                        await message.add_reaction("❌")

                        try :
                            def checkEmoji(reaction, user):
                                return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

                            reaction, user = await bot.wait_for("reaction_add", timeout=30, check=checkEmoji)

                            if reaction.emoji == "✅":
                                os.remove(f"stuffs/{id}/{vieux}.png")
                                await ctx.send(f"Votre stuff {vieux} a été renommé en {nouveau_nom} et l'autre supprimé")
                                
                                        
                            elif reaction.emoji == "❌" :
                                await ctx.send("D'accord j'annule la sauvegarde")
                                break
                        except :
                            embed = Embed(description = f"Les 30 secondes sont passées")
                            await membre.send(embed = embed)
                        
                    else :
                        ancien = rf"stuffs/{id}/{vieux}.png"
                        new_name = rf"stuffs/{id}/{nouveau_nom}.png"
                        os.rename(ancien,new_name)
                        suprligne(f"stuffs/{id}/{id}.csv",i)
                        addincsv(f"stuffs/{id}/{id}.csv",nouveau_nom)
                        await membre.send(f"changement de {vieux} à {nouveau_nom} éffecué")
                        break
            
                elif reaction.emoji == "❌" :
                    await membre.send(f"D'accord, il doit y avoir une erreur")
            except :
                embed = Embed(description = f"Les 30 secondes sont passées")
                await membre.send(embed = embed)

        i+=1


@bot.command()
async def access(ctx,stuff) :
    membre = ctx.author
    id = ctx.author.id
    await ctx.send(f"ça se passe en mp")
    try :
        await membre.send(f"Voici votre stuff  : {stuff}")
        await membre.send(file = File(rf"stuffs/{id}/{stuff}.png"))
    
    except :
        embed_erreur = Embed(description = f"Il y a eu une erreur, veuillez vérifier le nom du stuff que vous vouliez voir via la commande mus_stuffs")
        await membre.send(embed = embed_erreur)


@bot.command()
async def suppr(ctx,stuff) :
    id = ctx.author.id
    membre = ctx.author
    try :
        res = False
        fichier = reader(open(f"stuffs/{id}/{id}.csv"))
        for ligne in fichier :
            if str(ligne[0])==str(stuff) :
                suprligne(f"stuffs/{id}/{id}.csv",fichier.line_num-1)
                os.remove(f"stuffs/{id}/{stuff}.png")
                await membre.send(f"J'ai bien supprimé le stuff {stuff}")
                res = True
        
        for ligne in fichier :
            await membre.send("Vous avez supprimé votre dernier stuff")

        if not res :
            await membre.send(f"veuillez vérifier vos stuffs via la commande 'mes_stuffs'")  


    except :
        await membre.send(f"veuillez vérifier vos stuffs via la commande 'mes_stuffs'")  


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
        nom = ctx.author.name
        ping = ctx.author.mention
        ID = ctx.author.id
        crea = ctx.author.created_at

    else :
        nom = membre.name
        ping = membre.mention
        ID = membre.id
        crea = membre.created_at

    embed = Embed(description = f"voici les informations sur {ping} : \n" , color = 0x33CAFF)

    embed.set_author(name=nom )

    embed.add_field(name="ID", value=ID, inline=False)

    embed.add_field(name="date de création du compte", value=crea, inline=False)

    embed.add_field(name=f"photo de profil", value=f"voici la photo de profil de {nom}", inline=True)

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
    fichier = reader(open("code_amis.csv"))
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
            
                    await ctx.send(embed = embed_valid) and addincsv("code_amis.csv" , ajout)
            
        
            except:
	            await ctx.send(embed = embed_annul)
    
        else :
            embed_invalid = Embed(description = f"votre code amis n'a pas été enregistré car il ne semble pas valide" , color = 0x33CAFF)
            await ctx.send(embed = embed_invalid)
    else :
        
        fichier = reader(open("code_amis.csv"))
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
                            
                                
                                suprligne("code_amis.csv",cpt_lignes-1) 
                                addincsv("code_amis.csv" , ajout) 
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



    fichier = reader(open("code_amis.csv"))

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
        
        
    
@bot.command(name="delete", pass_context=True)
@commands.has_permissions(administrator=True)
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    
    for message in messages:
        await message.delete()
    
    await ctx.send(f"{number} messages ont été supprimés")
       



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


@bot.command()
async def get_data(ctx) :
    res = "```py\n"
    for k,v in data.items() :
        res = res + f"""
{k,v}
"""
    res = res + "```"

    embed = Embed(title = "nom et poids des armes" , description = res , color = 0x33CAFF)

    await ctx.send(embed = embed)


import youtube_dl
import asyncio
from discord import FFmpegPCMAudio

from discord import FFmpegPCMAudio
import youtube_dl
import asyncio
ytdl = youtube_dl.YoutubeDL()

class Bot_music:
    def __init__(self) -> None:
        self.music_guild = {}
        self.queue_guild = {}
        self.current_song = None
        self.message_embed = None

    async def setup_music(self, ctx, channel_music):
        with open(f"stuffs/{id}/{id}","wb") as csvfile:
            filewriter = writer(csvfile, delimiter=',', quotechar='|', quoting=QUOTE_MINIMAL)

        channel_music = str(channel_music).replace("<","").replace(">","").replace("#","")
        addincsv(f"musique/{ctx.guild.id}.csv", channel_music)
    
    async def update_embed(self, ctx, message_embed, pause=False):
        res=""
        for musique in self.queue_guild[ctx.guild]:
            res = res + f"\n{musique}"
        if pause:
            emote = "⏸"
        else:
            emote = "▶"
        new_embed = Embed(title="Music", description=f"Song State : {emote}\n\nCurrent song : {self.current_song}\n \nQueue : {res}", color=0x33CAFF)
        
        async def callback_pause(interaction):
            if interaction.user.id == ctx.author.id:
                await self.pause(ctx=ctx)

        async def callback_skip(interaction):
            if interaction.user.id == ctx.author.id:
                await self.skip(ctx=ctx)

        button_pause = bt.Button(label="pause/play", style=ButtonStyle.primary, emoji="▶")
        button_pause.callback = callback_pause

        button_skip = bt.Button(label="skip", style=ButtonStyle.primary, emoji="⏭")
        button_skip.callback = callback_skip

        view = bt.View()
        view.add_item(button_pause)
        view.add_item(button_skip)
        
        
        await message_embed.edit(view=view, embed=new_embed)

    async def resume(self, ctx):
        client = ctx.guild.voice_client
        if client.is_paused():
            client.resume()

    async def pause(self, ctx):
        client = ctx.guild.voice_client
        if not client.is_paused():
            client.pause()
            await self.update_embed(ctx=ctx, message_embed=self.message_embed, pause=True)
        
        else :
            await self.resume(ctx)
            await self.update_embed(ctx=ctx, message_embed=self.message_embed, pause=False)

    async def skip(self, ctx):
        client = ctx.guild.voice_client
        client.stop()
        await ctx.send("je change de son")

    async def play_song(self, ctx, url_stream, client_bot, message_embed : Message):
        try:
            source = PCMVolumeTransformer(FFmpegPCMAudio(url_stream, before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

            def next(_):
                try :
                    if len(self.music_guild[ctx.guild]) > 0:
                        new_song = self.music_guild[ctx.guild][0]
                        del self.music_guild[ctx.guild][0]
                        del self.queue_guild[ctx.guild][0]
                        self.current_song = new_song
                        self.play_song(ctx, new_song, client_bot=client_bot)
                    else:
                        asyncio.run_coroutine_threadsafe(client_bot.disconnect(), bot.loop)
                except :
                    pass
        except:
            pass
        
        client_bot.play(source, after=next)
        await self.update_embed(ctx=ctx, message_embed=message_embed)

    async def play(self, ctx, url):
        
        fichier = reader(open(f"musique/{ctx.guild.id}.csv"))
        id_channel = None
        for ligne in fichier :
            id_channel = str(ligne).replace("[","").replace("]","").replace("'","").replace(","," ")

        channel_embed = bot.get_channel(int(id_channel)) 

        client_bot : VoiceClient = ctx.guild.voice_client
        
        if not client_bot == None:
            video = ytdl.extract_info(url, download=False)
            url_stream = video["formats"][0]["url"]
            self.music_guild[ctx.guild].append(url_stream)
            title_song = video["title"]
            self.queue_guild[ctx.guild].append(title_song)

            await self.update_embed(ctx=ctx, message_embed=self.message_embed)

        else:
            if ctx.author.voice == None:
                await ctx.send("you must be in a voice channel to play music")
            else:
                messages = await channel_embed.history(limit=50).flatten()
    
                for message in messages:
                    await message.delete()

                self.music_guild[ctx.guild] = []
                self.queue_guild[ctx.guild] = []
                channel_vc = ctx.author.voice.channel
                await channel_vc.connect()    

                client_bot : VoiceClient = ctx.guild.voice_client

                video = ytdl.extract_info(url, download=False)
                title_song = video["title"]
                self.queue_guild[ctx.guild].append(title_song)

                url_stream = video["formats"][0]["url"]
                a = str(self.queue_guild[ctx.guild]).replace("[","").replace("]","").replace("'","").replace(","," ")
                message_embed  = Embed(title="Music", description=f"Current song : {title_song}\nQueue : {a}", color=0x33CAFF)
                self.message_embed = await channel_embed.send(embed=message_embed)
                self.current_song = title_song

                await self.play_song(ctx, url_stream=url_stream, client_bot=client_bot, message_embed=self.message_embed)

bots_music_dict = {}

@bot.command()
async def play(ctx, url):
    if bots_music_dict.get(ctx.guild) == None:
        bot_music = Bot_music()
        bots_music_dict[ctx.guild] = bot_music
        await bots_music_dict[ctx.guild].play(ctx=ctx, url=url)
    else:
        await bots_music_dict[ctx.guild].play(ctx=ctx, url=url)

@bot.command()
async def setup_music(ctx, channel):
    await bots_music_dict[ctx.guild].setup_music(ctx=ctx, channel_music=channel)
            
@bot.command()
async def pause(ctx):
    await bots_music_dict[ctx.guild].pause(ctx=ctx)

@bot.command()
async def resume(ctx):
    await bots_music_dict[ctx.guild].resume(ctx=ctx)

@bot.command()
async def skip(ctx):
    await bots_music_dict[ctx.guild].skip(ctx=ctx)
    

@bot.command()
async def help(ctx) :

    message_commande = ctx.message

    membre = ctx.author

    embed_help_1 = Embed(title = "help clem 3eme du nom" , description = f"-> invit : vous donne un lien pour inviter ce bot\n \n-> infoserveur : donne les informations pricipales de ce serveur\n \n-> bulle : fait dire au bot ce que vous voulez\n  \n-> goulag : vous envoi directement au goulag \n \n-> ungoulag : vous sort du goulag\n \n-> hug : faites un calin a la personne de votre choix \n \n-> pat : faites un pat pat a la personne de votre choix \n \n-> spam: commande spéciale (demander a clem#1777)\n \n-> clemw : vous donne une arme au hasard \n   ou vous pouvez choisir parmis :\n   random ; shooter ; roller ; charger\n   slosher ; splatling ; dualies ; brella \n \n-> stuff : affiche votre stuff en emojis ou en image que vous pouvez sauvegarder\n   voici les emojis possibles et leur noms :\n   ssu -> <:ssu:799259849732653096> ; rsu -> <:rsu:799259849044262924> ; scu -> <:scu:799259849446916097> ; spu -> <:spu:799259849665019924>\n   ss -> <:ss:799259849404973077> ; qsj -> <:qsj:799259849442983966> ; qr -> <:Qr:799259849249914901> ; os -> <:os:799259849326067775> \n   mpu -> <:mpu:799259849484402705> ; iss -> <:iss:799259849803825183> ; ism -> <:ism:799259849409298433> ; bdu -> <:bdu:799259849128804353> \n   cbk -> <:Cbk:799259849362767912> ; ir -> <:ir:799259849517957152> ; iru -> <:iru:799259849471819806> ; dr -> <:dr:799259849690054696> \n   lde -> <:lde:799259849359097896> ; sbpu -> <:sbpu:799259849422536754> ; tnty -> <:tnty:799259849501573170> ; hnt -> <:DeathMarking:799259849468805120> \n   ns -> <:ns:799259849857826827> ; thi -> <:thi:799259849799106560> ; rsp -> <:rp:799259849384001546> ; sj -> <:sl:799259849425813535> \n   og -> <:og:799259849786785832> ; ab -> <:ad:852154177869709363> ; uk ou ?-> <:__:852153879650893935>  \n \n-> scrim : sur des maps aléatoires\n   bo3 : vous fait jouer sur les 3 premiers modes <:sz:853656465423990807> ; <:rm:853656465725456424> ; <:tc:853656463846146068>   \n   bo5 : vous fait jouer sur tous les modes et sur une autre zone \n   bo7 vous fait jouer 2 fois sur chaque modes sauf clam \n   bo9 vous fait jouer 2 fois sur chaque modes et une autre dz" , color=0x33CAFF)
    embed_help_2 = Embed(title = "help clem 3eme du nom" , description = f"-> citation : ajoute une citation et la personne qui l'a pronnoncée (sous la forme $citation 'message' membre)\n \n-> anniv : ajoutez votre anniversaire en faisant la commande $anniv 'jour' 'mois' (ATTENTION vous ne pouvez l'éxecuter qu'une seule fois)\n \n-> tableau : vous montre les anniversaires des personnes ayant renseigné leur anniversaire\n \n-> role/unrole : ajoute ou enlève un role ($role @personne 'nom exact du role')\n \n-> voc : vous indique un fichier sur les calls de splatoon2\n \n-> pp : montre votre photo de profil (sans ping) ou celle de vos amis (avec ping)\n \n-> info : montre les informations d'un profil \n \n-> add : ajoute votre code amis \n \n-> code : montre votre code amis (sans ping) ou celui de vos amis (avec ping) \n \n-> delete 'nombre de messages' : (à noter qu'il faur certaines permissions)\n \n-> syracuse 'nombre' : vous renvoi le maximum atteint et le nombre de tours\n \n-> get_data : vous envoi le nom exact des armes nécesaire à la commande match\n \n-> match '8 armes' : renvoi des compositions équitables\n \n-> matchr : renvoi des compositions équitables aléatoire\n \n-> set_role 'nom du role' un emoji quelconque : (nécessite un salon role) permet d'obtenir un role" , color = 0x33CAFF)
    embed_help_3 = Embed(title = "help clem 3eme du nom" , description = f"->Suite des commandes pour les stuffs :\n  -mes_stuffs : vous montre tous vos stuffs \n  -rename : permet de renomer un stuff\n  -access 'stuff' : vous montre ce stuff\n(je vous conseille de copier coller le nom de la commande mes_stuffs pour éviter les bugs) \n  -suppr 'stuff' : supprime ce stuff\n(même conseil que pour la commande access)\n  \n-> rotation : Vous montre quelles sont les rotations actuelles \n  \n-> salmon : Vous montre la rotation actuelle en Salmon Run \n  \n-> splatnet : Vous montre quels équipements sont disponibles sur l'application" , color = 0x33CAFF)
    embed_help_musique = Embed(title="Help Musique", description="-> setup_music *channel* : choississez l'endroit où le bot va indiquer les musiques en cour ou en liste d'attente (à faire une seule fois pour l'instant)\n \n-> play *url* : joue le son ou l'ajoute à la file d'attente \n \n-> pause : pause la musique ou reprend la lecture \n \n-> skip : passe au son suivant", color=0x33CAFF)
    embed_docu = Embed(title="Documentation",
                  description=f"voici les sites utilisés pour le bot ainsi que les personnes m'ayant aidées :\n \n inkpedia -> [inkpedia](https://splatoonwiki.org/wiki/Main_Page) \n \n pour les armes -> [site de spike](https://leanny.github.io/splat2new/database.html) \n  \n Pour les informations de splatnet ->  [splatoon.ink](https://splatoon2.ink) \n \n Mon IDE pour coder le bot -> Visual Studio Code \n \n la documentation de discord.py -> [discord.py](https://discordpy.readthedocs.io/en/latest/api.html) \n \n cocopw qui m'a aidé pour le code \n mishy et la overtime (RIP) et beacoup d'autres pour les idées \n Bot codé par clem#1777 (discord) @clem_spl (twitter) \n  \n-> Bot hébergé sur Alwaisdata.net (gratuit)",
                  color=0x33CAFF)

    embed_help_1.set_footer(text= f"1/3         Si vous souhaitez me faire parvenir un bug utilisez la commande report *votre problème* (des screens du bug sont suportés)")
    embed_help_2.set_footer(text= f"2/3         Si vous souhaitez me faire parvenir un bug utilisez la commande report *votre problème* (des screens du bug sont suportés)")    
    embed_help_3.set_footer(text= f"3/3         Si vous souhaitez me faire parvenir un bug utilisez la commande report *votre problème* (des screens du bug sont suportés)")


    async def callback_1(interaction):
        if interaction.user.id == membre.id:
            await interaction.message.edit(embed = embed_help_1)

    async def callback_2(interaction):
        if interaction.user.id == membre.id:
            await interaction.message.edit(embed = embed_help_2)

    async def callback_3(interaction):
        if interaction.user.id == membre.id:
            await interaction.message.edit(embed = embed_help_3)

    async def callback_music(interaction):
        if interaction.user.id == membre.id:
            await interaction.message.edit(embed = embed_help_musique)

    async def callback_docu(interaction):
        if interaction.user.id == membre.id:
            await interaction.message.edit(embed = embed_docu)

    async def callback_destroy(interaction):
        if interaction.user.id == membre.id:
            await interaction.message.delete()
            await message_commande.delete()


    button_1 = bt.Button(label=1, style=ButtonStyle.primary)
    button_1.callback = callback_1

    button_2 = bt.Button(label=2, style=ButtonStyle.primary)
    button_2.callback = callback_2

    button_3 = bt.Button(label=3, style=ButtonStyle.primary)
    button_3.callback = callback_3

    button_music = bt.Button(style=ButtonStyle.primary, emoji="🎵")
    button_music.callback = callback_music

    button_docu = bt.Button(label="Documentation",style=ButtonStyle.primary)
    button_docu.callback = callback_docu

    button_destroy = bt.Button(style=ButtonStyle.primary, emoji="❌")
    button_destroy.callback = callback_destroy

    view = bt.View()
    view.add_item(button_1)
    view.add_item(button_2)
    view.add_item(button_3)
    view.add_item(button_music)
    view.add_item(button_destroy)
    view.add_item(button_docu)

    await ctx.send(view=view, embed=embed_help_1)
                    

import sys

try:
    sys.path.append("../token")
    import token_bot
except:
    sys.path.append("/home/cleeem/python/token")
    import token_bot
    
#bot principal
token_run_main = token_bot.tokens["token_bot_principal"]

#2eme bot
token1 = token_bot.tokens["token_bot_test"]

bot.run(token_run_main)


