from CozyClient import CozyTechClient
import discord

TOKEN = 'ODcxNzc3MDE4MzEwNzAxMDc2.YQgPnQ.7W7NDzkb5ZiG3Ov3omlfe3cYH0M'


intents = discord.Intents.default()
intents.members = True
client = CozyTechClient(intents = intents)

client.run(TOKEN)
