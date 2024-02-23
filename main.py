import discord
import os
import random

client = discord.Client(intents=discord.Intents.all())

friday = [
    "I haven't been so excited about Friday since last Friday.",
    "Friday is my second favorite F-word. My first is food, definitely food.",
    "It's Friday! Time to go make stories for Monday.",
    "On Friday, I prefer my espresso in a martini.",
    "Friday called. She's on her way, and she's bringing wine.",
    "Friday is the golden child of the weekdays. The superhero of the workweek. The welcome wagon to the weekend.",
    "If Friday had a face, I would kiss it.",
    "I'm not an early bird or a night owl. I'm some form of permanently exhausted pigeon, especially by Friday.",
    "Friday is the day that magically turns a 45-minute commute into a 20-minute one.",
    "Friday is the day I can wear casual clothes to work, and nobody will notice.",
    "I work mostly during the week, but on Fridays, I make it my mission to nap like it's my job.",
    "Friday is the only day in the office where everyone thinks I'm working hard because they can't see my screen due to all the browser tabs.",
    "Why is Monday so far away from Friday, but Friday is so close to Monday? Life's greater mystery.",
    "My boss asked me why I like Fridays. I told him it's the day when I start my 'Weekend Research' project, which involves finding the best position on the couch.",
    "Friday is like a superhero that always arrives just in time to save me from turning into a pumpkin.",
    "I don't work on Fridays. I make appearances and contribute to the overall well-being of the office morale.",
    "The best thing about Fridays is knowing that after this, I only have two more workdays until I can complain about Monday again.",
    "If Friday had a personality, it would be that awesome friend who always brings snacks to the party.",
    "I like to think of Friday as a free pass to do silly things I regret on Monday.",
    "Friday is the day when the only decision you need to make is bottle or glass.",
    "I've never met a Friday I didn't like.",
    "Friday is the day I remind myself that I survived another week of professional pretending.",
    "I'm not lazy. I'm on energy-saving mode, and Friday is my full-power day."
]

friday_words = ['friday', 'weekend', 'party']  # Add more keywords as needed


@client.event
async def on_ready():
  print('We have logged in as {0.user}')


@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]

  if message.author == client.user:
    return

  if any(word in message.content.lower() for word in friday_words):
    await message.channel.send(username + " " + random.choice(friday))


my_secret = os.environ['DISCORD_TOKEN']
client.run(os.environ['DISCORD_TOKEN'])
