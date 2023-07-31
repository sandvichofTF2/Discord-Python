import os
import discord
import random
from discord.ext import commands
from webserver import webserver

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

skill_issue_det = [
  "i suck", "i fucking suck", "fucked up", "cant", "ah fuck", "WHY", "FUCK"
]

skill_issue_rep = [
  "Skill Issue", "Bloody skill issue ya dumbass!",
  "Is that skill issue I'm hearing?", "skill issue, git gud"
]

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message):
  print("onmsg")
  if message.author == bot.user:
    return

  msg = message.content

  if any(word in msg for word in skill_issue_det):
    await message.channel.send(random.choice(skill_issue_rep))

  await bot.process_commands(message)


@bot.command()
async def d20(ctx):
  print("d20")
  embed = discord.Embed(title="Your Roll is: ",
                        description=(random.randint(1, 20)),
                        color=(0xF85252))
  await ctx.send(embed=embed)


webserver()
bot.run(os.getenv("TOKEN"))
