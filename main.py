import os
import discord
import random
from discord.ext import commands
from webserver import webserver

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# I thought it would be funny if i add a function to call out skill issue whenever someone complain
skill_issue_det = [
  "I fucked up", "i fucked up", "cant", "ah fuck", "WHY", "FUCK"
]

skill_issue_rep = [
  "Skill Issue", "Bloody skill issue ya dumbass!",
  "Is that skill issue I'm hearing?", "skill issue, git gud"
]
# Lists for words to trigger the deez nuts joke
dznuts = ["these", "These", "deez"]
sukon = ["suck", "Suck", "sucks", "Sucks", "SUCK", "SUCKS", "sugon", "Sugon", "SUGON","sugoi","Sugoi","SUGOI","Sawcon","sawcon","SAWCON"]
wend = ["wendy's","Wendy's","wendys","Wendys","WENDY'S","WENDYS","when these","When these","WHEN THESE","when These","When These"]

# Print when the bot gets start up
@bot.event
async def on_ready():
  print(f'Ballin as {bot.user}')

# detection whenever someone said st
@bot.event
async def on_message(message):
  print("onmsg")
  if message.author == bot.user:
    return

  msg = message.content
  chan = message.channel

  # skill issue things
  if any(word in msg for word in skill_issue_det):
    await message.channel.send(random.choice(skill_issue_rep))

  # deez nuts things
  if any(word in msg for word in dznuts):
    await chan.send("Deez Nuts!")
  if any(word in msg for word in sukon):
    await chan.send("Suck On Deez Nuts!")
  if any(word in msg for word in wend):
    await chan.send("When These Nuts fit in yo MOUTH!")
  
  await bot.process_commands(message)

# d20 command function to do a cool d20 rolls
@bot.command()
async def d20(ctx):
  print("d20")
  embed = discord.Embed(title="Your Roll is: ",
                        description=(random.randint(1, 20)),
                        color=(0xF85252))
  await ctx.send(embed=embed)


webserver()
bot.run(os.getenv("TOKEN"))
