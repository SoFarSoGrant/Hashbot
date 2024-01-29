#! /usr/bin/python3

__author__ = "v0yager"
__license__ = "GPL3"
__version__ = "1.0.0"
__description__ = """
                This bot will return the hashes obtained using discohash
                for a specified number of access points as a txt file.
                Message the bot with !dumphash [NUMBER].
                """

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 1. Create a bot in the Discord developer portal
# 2. Grant it the required permissions (message_content)
# 3. Obtain a token and the channel ID
# 4. Add these to a .env file containted in the same directory

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('GUILD_CHANNEL')


bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.command(name="dump")
async def on_message(ctx, num_hashes=int(100)):
    try:
        await ctx.message.delete()
        with open('hashdump.hc22000', 'w') as f:
            channel = bot.get_channel(int(CHANNEL))
            message = channel.history(limit=200)  # Retrieve more messages initially
            hash_count = 0
            async for msg in message:
                if msg.embeds:
                    print(f"Embeds found: {msg.embeds}")  # Debugging
                    try:
                        hash_dict = msg.embeds[0].to_dict()
                        hash = hash_dict['fields'][0]['value']
                        f.write(hash[1:-1] + '\n')
                        hash_count += 1
                        if hash_count >= num_hashes:
                            break
                    except IndexError as ie:
                        print(f"IndexError: {ie}")  # Debugging
                        continue
                else:
                    continue
        with open('hashdump.hc22000', 'r') as f:
            await ctx.send(file=discord.File(f, 'hashdump.hc22000'))
    except Exception as e:
        print(f"An error occurred: {e}")  # Debugging
        await ctx.send(f"An error occurred: {e}")

#/dumpssid [SSID-NAME] will output a file with hash only from specified SSID.
@bot.command(name="dumpssid")
async def on_message(ctx, ssid: str):
    try:
        await ctx.message.delete()
        channel = bot.get_channel(int(CHANNEL))
        message = channel.history(limit=200)
        found = False
        async for msg in message:
            if msg.embeds:
                embed = msg.embeds[0].to_dict()
                hash_analysis = next((field['value'] for field in embed['fields'] if field['name'] == 'Hash Analysis:'), '')
                if f"SSID.......: {ssid}" in hash_analysis:
                    hash_info = next((field['value'] for field in embed['fields'] if field['name'] == 'Hash:'), None)
                    if hash_info:
                        filename = f"{ssid}.hc22000"
                        with open(filename, 'w') as f:
                            f.write(hash_info.strip('`'))
                        await ctx.send(file=discord.File(filename))
                        found = True
                        break
        if not found:
            await ctx.send(f"No hash found for SSID {ssid}.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


bot.run(TOKEN)
