import discord
import asyncio
import random
import json
import os

# Add token to client run
token_file = open('token_file.txt', 'r')
token = token_file.read()
client = discord.Client()

command_list = ['!test', '!sleep', '!hello', '!flip', '!addquote', '!quote']

@client.event
async def on_ready():
    print('\n-----')
    print('Logged in as: ' + client.user.name)
    print('\nClientID: ' + client.user.id)
    print('Token: ' + token)
    print('-----')
    # await client.get_channel(client, "developers")


@client.event
async def on_message(message):
    if message.content.startswith(command_list[0]):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.', message.format(counter))

    elif message.content.startswith(command_list[1]):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith(command_list[2]):
        await client.send_message(message.channel, 'Hi!')

    elif message.content.startswith(command_list[3]):
        flip = random.choice(['Heads', 'Tails'])
        await client.send_message(message.channel, flip)

    elif message.content.startswith(command_list[4]):
        if not os.path.isfile("quote_file.json"):
            quote_list = []
        else:
            with open("quote_file.json", "r") as quote_file:
                quote_list = json.load(quote_file)
            quote_list.append(message.content[9:])
        with open("quote_file.json", "w") as quote_file:
            json.dump(quote_list, quote_file)
            await client.send_message(message.channel, 'Quote saved successfully!')

    elif message.content.startswith(command_list[5]):
        with open("quote_file.json", "r") as quote_file:
            quote_list = json.load(quote_file)
        await client.send_message(message.channel, random.choice(quote_list))

    elif message.content.startswith("http") and message.channel.name == "general":
        await client.delete_message(message)
        await client.send_message(message.channel, "Message deleted. Please post links in the **media-links** channel.")

client.run(token)
