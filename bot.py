import discord
command_go = "!"

class MyClient(discord.Client):
	async def on_ready(self):
		print("Bot: ON")

	async def on_message(self, message):
		# don't respond to ourselves
		print(message.content)
		if message.content[0] == command_go:
			if message.content[1:len(message.content)] == "bonjour":
				await message.channel.send("Bonjour " + str(message.author.mention) + ".")

client = MyClient()
client.run('NTU2NTUzOTkzMjA0MTM3OTg0.D27c5g.ATRmPVfv66b6SvPjkSY9L1e8nRA')