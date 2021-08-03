import discord


class CozyTechClient(discord.Client):
    async def on_ready(self):
        print("Bot is ready")


    async def on_message(self,message):
        if message.author.bot:
            return
        if message.content == "salam":
            await message.channel.send("salam")
        if message.content.startswith("sum"):
            args = message.content.split(" ")
            num1 = int(args[1])
            num2 = int(args[2])
            await message.channel.send(num1 + num2)


    async def on_member_join(self,member):
        print("salam")
        await member.guild.system_channel.send("salam khosh oomadi " + member.mention)
