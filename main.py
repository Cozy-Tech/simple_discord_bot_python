from CozyClient import CozyTechClient
import discord

TOKEN = 'YOUR_BOT_TOKEN'


intents = discord.Intents.default()
intents.members = True
client = CozyTechClient(intents = intents)

client.run(TOKEN)
