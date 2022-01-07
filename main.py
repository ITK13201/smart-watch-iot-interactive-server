import logging
from typing import List
import discord

from config.config import DISCORD_BOT_TOKEN
from usecase.utils import ErrorStruct, send_error_message
from processes.process import Process


logger = logging.getLogger(__name__)

discordClient = discord.Client()

# コマンド処理
async def exec_command(ctx, args):
    command = args[1]
    process = Process(ctx)
    if command == "start":
        await process.start()
    elif command == "stop":
        await process.stop()
    elif command == "status":
        await process.status()
    else:
        err = ErrorStruct(key=command, value="command not found")
        errors = [err]
        await send_error_message(ctx, errors)


@discordClient.event
async def on_ready():
    # start server
    logger.info("Starting Server...")


@discordClient.event
async def on_message(ctx):
    def parse_command(content: str) -> List[str]:
        # zenkaku to hankaku and split
        args = content.replace("　", " ").split(" ")
        # if contains empty string, remove it
        while "" in args:
            args.remove("")
        return args

    # exclude Bot's comment
    if ctx.author.bot:
        return
    # parse command
    args = parse_command(ctx.content)
    # use command "/iot"
    if args[0] == "/iot":
        await exec_command(ctx, args)


# 実行
def main():
    discordClient.run(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    main()
