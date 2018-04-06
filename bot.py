import discord.ext
from discord.ext import commands
import random, datetime
now = datetime.datetime.now()

bot = commands.Bot("c!")

bypass_list = ["428370014798872586"]
TOKEN = "NDI4MzcwMDE0Nzk4ODcyNTg2.DaVW-w.FblsPqKSyrR575QCFak6pze0yOw"

@bot.event
async def on_message(message):
    if message.content.upper().startswith("C!SAY"):
        ID = message.author.id
        args = message.content.split(" ")
        msg = "%s" % (" ".join(args[1:])).format(args[1])
        usr = "<@%s> said: " % (ID)
        embed=discord.Embed(description=usr + msg, color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!WHISPER"):
        args = message.content.split(" ")
        msg = "%s" % (" ".join(args[1:])).format(args[1])
        embed=discord.Embed(description=msg, color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!DATE"):
        embed=discord.Embed(title="Today is " + str(now.month) + "/" + str(now.day) + "/" + str(now.year) + ".", color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!HELP"):
        embed=discord.Embed(title="Hello! Need help? These are my commands.", description = "**THE COMMAND USAGE WILL BE DISPLAYED.**\n\n**c!help**, which is the command list\n\n*c!help*, as is\n\n**c!date**, which gets the date\n\n*c!date*, as is\n\n**c!link**, which gives an add link\n\n*c!link*, as is\n\n**c!kid**, which generates a random description\n\n*c!kid*, as is\n\n**c!adult**, which generates a random description\n\n*c!adult*, as is\n\n**c!members**, which lists the server members\n\n*c!members*, as is\n\n**c!slap**, which slaps an annoying dude\n\n*c!slap @username*\n\n**c!iam**, which is your Discord identity\n\n*c!iam*, as is\n\n**c!8ball**, which is my spin on a virtual 8 ball\n\n*c!8ball Will the sky fall?*\n\n**c!dice**, which is a dice roll\n\n*c!dice*, as is\n\n**c!opinion**, which asks opinion\n\n*c!opinion Am I smart?*\n\n**c!choice**, which chooses an option\n\n*c!choice Potatoes or carrots?*\n\n**c!coinflip**, which flips a virtual coin\n\n*c!coinflip*, as is\n\n**c!say**, which is public talk through me\n\n*c!say Hello!*\n\n**c!whisper**, which is anonymous talk\n\n*c!whisper Hello!*\n\n**c!command**, which commands a member\n\n*c!command @username [one] [two] [three]*", color=0xF4BC0C) 
        embed.set_footer(text="© Copyright DakuStudios " + str(now.year) + ".")
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!OPINION"):
        answer = ["I believe so.", "Not a chance."]
        embed=discord.Embed(description=random.choice(answer), color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
    if message.content.upper().startswith("C!CHOICE"):
        reply = ["I would pick the latter.", "The first for sure."]
        embed=discord.Embed(description=random.choice(reply), color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
    if message.content.upper().startswith("C!COINFLIP"):
        coin = ["Guess what? It's heads!", "Looks like it's tails."]
        embed=discord.Embed(description=random.choice(coin), color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
    if message.content.upper().startswith("C!DICE"):
        number = ["One it is!", "Guess what? It's a two!", "You rolled a three!", "Looks like a four!", "The dice says five.", "Congrats! You got a six.!"]
        embed=discord.Embed(description=random.choice(number), color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
    if message.content.upper().startswith("C!8BALL"):
        ball =[]
        embed=discord.Embed(description=random.choice([
        "It is certain.", "As I see it, yes.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "Most likely.",
        "Outlook good.", "Yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.",])
        , color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
    if message.content.upper().startswith("C!IAM"):
        ID = message.author.id
        AVATAR = message.author
        embed=discord.Embed(description=message.author.avatar_url + " " + "<@%s>" % (ID) + " " + ID, color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!KID"):
        mood = ["sad", "happy", "bored", "mad", "calm", "kind", "rude", "angry", "agitated", "thoughtful", "shrewd", "clumsy", "faulty", "funny", "crazy", "sleepy", "dumb", "miserable", "disgusted", "trusting", "friendly", "shameful", "piteous", "envious", "jealous", "lovelorn"]
        hobby = ["listening to Big Shaq", "playing ROBLOX", "annoying parents", "collecting coins", "eating sushi", "playing with friends", "collecting stamps", "doing homework", "playing with siblings", "forgetting to drink water", "making cookies", "going to the bakery across the street", "playing video games", "gossiping with friends", "bothering siblings", "going on vacation", "spending quality time with buddies", "going to Chipotle", "eating burritos"]
        gender = ["boy", "girl"]
        hair = ["black", "blonde", "brown", "pink", "purple", "red", "blue", "orange", "green", "neon green", "gray"]
        embed=discord.Embed(description="A " + random.choice(hair) + "-hair colored " + random.choice(gender) + " that likes " + random.choice(hobby) + " is feeling very " + random.choice(mood) + ".", color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!ADULT"):
        mood = ["sad", "happy", "bored", "mad", "calm", "kind", "rude", "angry", "agitated", "thoughtful", "shrewd", "clumsy", "faulty", "funny", "crazy", "sleepy", "dumb", "miserable", "disgusted", "trusting", "friendly", "shameful", "piteous", "envious", "jealous", "lovelorn"]
        hobby = ["going to work", "gambling in Vegas", "teaching manners", "being impossibly strict", "eating pizza", "reading thick and fat legal books", "signing contracts", "begging for money", "attending a corporate meeting", "staring blankly into the mirror", "getting into shape", "subscribing to JustinBieberVEVO on YouTube", "getting fat on hot dogs", "growing extra hair", "paying for a very large lunch order", "going to Wendy's", "going to McDonald's", "going to Subway", "going to KFC"]
        gender = ["man", "woman"]
        hair = ["black", "blonde", "brown", "pink", "purple", "red", "blue", "orange", "green", "neon green", "gray"]
        embed=discord.Embed(description="A " + random.choice(hair) + "-hair colored " + random.choice(gender) + " that likes " + random.choice(hobby) + " is feeling very " + random.choice(mood) + ".", color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!MEMBERS"):
        memberlist = "@" + ", @".join([member.name for member in message.server.members])
        embed=discord.Embed(description=str(memberlist), color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!LINK"):
        embed=discord.Embed(description="https://discordapp.com/oauth2/authorize?client_id=428370014798872586&permissions=2146958583&scope=bot", color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!SLAP"):
        args = message.content.split(" ")
        ID = message.author.id
        embed=discord.Embed(description="Hey, you! Not you, <@%s>, I mean {}! You know I'm talking to you. Please refrain from communication. In other words, shut up. Thanks.".format(args[1]) % (ID), color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)
    if message.content.upper().startswith("C!COMMAND"):
        args = message.content.split(" ")
        ID = message.author.id
        embed=discord.Embed(description="Hello, my friend. Not you, <@%s>, I mean {}.  Please {} {} {}.".format(args[1], args[2], args[3], args[4]) % (ID), color=0xF4BC0C)
        await bot.send_message(message.channel, embed=embed)
        await bot.delete_message(message)

bot.run(TOKEN)
