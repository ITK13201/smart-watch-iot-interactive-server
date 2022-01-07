import discord
from typing import List

DISCORD_MESSAGE_COLOR_CODES = {"info": 0x00FF00, "error": 0xFF0000}


class ErrorStruct:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


async def send_error_message(ctx, errors: List[ErrorStruct]):
    embed = discord.Embed(
        title="[ERROR]",
        description="error messages are here.",
        colour=DISCORD_MESSAGE_COLOR_CODES["error"],
    )
    for err in errors:
        embed.add_field(name=err.key, value=err.value, inline=False)
    await ctx.channel.send(embed=embed)


async def send_info_message(ctx, description: str):
    embed = discord.Embed(
        title="[INFO]",
        description=description,
        colour=DISCORD_MESSAGE_COLOR_CODES["info"],
    )
    await ctx.channel.send(embed=embed)
