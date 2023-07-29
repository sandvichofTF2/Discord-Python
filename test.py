import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
# from webserver import webserver

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

skill_issue_det = [
  "i suck", "i fucking suck", "fucked up", "cant", "ah fuck", "WHY"
]

skill_issue_rep = [
  "Skill Issue", "Bloody skill issue ya dumbass!",
  "Is that skill issue I'm hearing?", "skill issue, git gud"
]


@client.event
async def on_ready():
  print(f'Logged in as {client.user}')


@bot.command(pass_context=True)
async def d20(ctx):
  embed = discord.Embed(title="Your Roll is: ",description=(random.randint(1, 20)),color=(0xF85252))
  await ctx.send(embed=embed)


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('$ImRusty'):
    await message.channel.send('No You suck')

  if any(word in msg for word in skill_issue_det):
    await message.channel.send(random.choice(skill_issue_rep))


# webserver()
client.run(os.getenv("TOKEN"))
