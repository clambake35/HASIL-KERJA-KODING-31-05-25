import discord
from discord.ext import commands
import os
from Ai import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

SAVE_DIR = "images"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def greet(ctx, name: str):
    await ctx.send(f'Halo!')


@bot.command(name="saveimg")
async def save_image(ctx):
    if not ctx.message.attachments:
        await ctx.send("Tidak ada gambar yang dikirim.")
        return

    for attachment in ctx.message.attachments:
        if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            save_path = os.path.join(SAVE_DIR, attachment.filename)
            await attachment.save(save_path)
            await ctx.send(f"Gambar disimpan: `{get_class(save_path)}`")
        else:
            await ctx.send(f"{attachment.filename} bukan file gambar yang didukung.")


bot.run("")
