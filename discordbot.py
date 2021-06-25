# bot.py
import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

questionnumber = 0
cluenumber = 0

listofquestions=[
    {"picture": "https://i.imgur.com/0fnAgZH.jpg",
    "question": "Question 1:  Near the entrance. Find the Sugar Maple tree planted by Boutros Boutros-Ghali (Secretary General of the United Nations). What year was it planted?",
    "answer": "1995",
    "clue": "what3words:"},
    {"picture": "https://i.imgur.com/0fnAgZH.jpg",
    "question": "Question 2: Find the White Birch tree planted by Mauno Koivisto (President of Finland). What year was it planted?",
    "answer": "1990",
    "clue": "what3words: "},
    {"picture": "https://i.imgur.com/Uzufjy3.jpg",
    "question": "Question 3: Find this statue. What is the name of it?",
    "answer": "osmosis",
    "clue": "what3words: "},
    {"picture": "https://academickids.com/encyclopedia/images/2/2a/ROT13.png",
    "question": "Question 4: ROT13. a becomes n, b becomes m, n becomes a, m, becomes b, etc. decode this word: puneyrf. What is the word? ",
    "answer": "charles",
    "clue": "p becomes c and f becomes s"},
    {"picture": "https://academickids.com/encyclopedia/images/2/2a/ROT13.png",
    "question": "Question 5: Great. Now walk to Charles and McKay, and start walking along Charles st. What number house has this outside?",
    "answer": "5",
    "clue": "It's between 1 charles and 10 charles"}
    ]
    


@client.event
async def on_message(message):
    global questionnumber
    global cluenumber
    if message.author == client.user:
        return
        
    if message.content.lower().startswith(listofquestions[questionnumber]["answer"].lower()):
        if questionnumber<len(listofquestions)-1:
            questionnumber+=1
            e = discord.Embed()
            e.set_image(url=listofquestions[questionnumber]["picture"])
            await message.channel.send(embed=e) 
            await message.channel.send(listofquestions[questionnumber]["question"])
        else:
            e = discord.Embed()
            e.set_image(url="https://www.pikpng.com/pngl/m/149-1496837_you-win-game-over-pixel-transparent-you-win.png")
            await message.channel.send(embed=e)
            e.set_image(url="https://www.pngitem.com/pimgs/m/172-1725252_transparent-you-win-png-transparent-you-win-text.png")
            await message.channel.send(embed=e) 
            e.set_image(url="https://kickinradgames.com/games/boom/images/logo.png")
            await message.channel.send(embed=e)

    elif message.content.startswith("CLUE"):
        if cluenumber<3:
            await message.channel.send(listofquestions[questionnumber]["clue"])
            cluenumber+=1
        await message.channel.send("Don't say CLUE more than once per question because there's only one clue available, but it'll still deduct a clue, even though it gives you the same clue. Clues remaining: " + str(cluenumber))


@client.event
async def on_ready():
    channel_id=0
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
        
    )
    for channel in guild.channels:
            if channel.name=="general":
                channel_id=channel.id

    channel = client.get_channel(channel_id)
    await channel.purge(limit=200)
    await channel.send("Hello. I am GeocacheBot. I'll ask a question, and you can type type answer here. Don't guess, because you can only type one message every two minutes! If you need a clue, you can say CLUE. But be careful, you only have a total of 3 clues for the whole geocache.")
    e = discord.Embed()
    e.set_image(url=listofquestions[0]["picture"])
    await channel.send(embed=e) 
    await channel.send(listofquestions[0]["question"])


client.run(TOKEN)