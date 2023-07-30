import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Merhaba nasıl yardımcı olabilirim?")
@bot.command()
async def nasilhapicilir(ctx):
    await ctx.send("hapı ağıza attıktan sonra su iç işe yarar.")
@bot.command()
async def ilacsaatleri(ctx):
    await ctx.send("ezanenin söylediği gibi telefon alarmı ayarla olur")
@bot.command()
async def makarnanasilyapilir(ctx):
    await ctx.send("su kaşlanır tuz ve sızı yağ eklenir makarnalar içine konur,8 dk beklenir")
@bot.command
async def akillitelefonlaaramayapma(ctx):
    await ctx.send("telefon uygulamasını aç.orda sayılar var oraya numaraları yaz")
bot.run("write your token")
