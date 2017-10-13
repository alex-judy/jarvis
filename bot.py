import discord
import asyncio
import random
import json
import os

# Add token to client run
token = ""
token_file = open('token_file.txt', 'r')
token = token_file.read()

client = discord.Client()



@client.event
async def on_ready():
    print('\n-----')
    print('Logged in as: ' + client.user.name)
    print('\nClientID: ' + client.user.id)
    print('Token: ' + token)
    print('-----')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.', message.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!hello'):
        await client.send_message(message.channel, 'Hi!')
    elif message.content.startswith('!flip'):
        flip = random.choice(['Heads', 'Tails'])
        await client.send_message(message.channel, flip)
    elif message.content.startswith('!addquote'):
        if not os.path.isfile("quote_file.txt"):
            quote_list = []
        else:
            with open("quote_file.txt", "rb") as quote_file:
                quote_list = json.load(quote_file)
        quote_list.append(message.content[9:])
        with open("quote_file.txt", "wb") as quote_file:
            json.dump(quote_list, quote_file)
            print('Successful run.')
client.run(token)
