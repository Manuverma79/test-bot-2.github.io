import discord


client = discord.Client()


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    with open("data.txt") as file:
        data = file.read()
        yuibite, lorbite = data.split()
        yuibite = int(yuibite)
        lorbite = int(lorbite)

    if message.author == client.user:
        return
    if message.content.startswith('$cutest'):
        await message.channel.send("cutest? offcourse its Yuichi's girlfriend lormy")
    if message.content.startswith('$lorbite'):
        lorbite = lorbite + 1
        await message.channel.send(f'lormy bite count = {lorbite}')
        with open("data.txt", "w") as file:
            x = str(yuibite) + " " + str(lorbite)
            file.write(x)
    if message.content.startswith('$yuibite'):
        yuibite = yuibite + 1
        await message.channel.send(f'yuichi bite count = {yuibite}')
        with open("data.txt", "w") as file:
            x = str(yuibite) + " " + str(lorbite)
            file.write(x)


client.run("OTU0MDE0NzI4NjkzMzU4Njcy.YjM9dA.5-0uTNKpcIM3YnbAssDk4Y_8b98")