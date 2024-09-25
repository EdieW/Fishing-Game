from typing import Final
import os
import discord
from dotenv import load_dotenv
from logic import play_logic
from aiohttp import ClientSession
import certifi
# from api_services import ensure_user

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')


# STEP 1: BOT SETUP
class MyBot(discord.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aiohttp_session = None

    async def setup_hook(self):
        # 在bot启动时初始化ClientSession
        if not self.aiohttp_session or self.aiohttp_session.closed:
            self.aiohttp_session = ClientSession()
        print("ClientSession has been created")

    async def close(self):
        # 在bot关闭时关闭ClientSession
        if self.aiohttp_session and not self.aiohttp_session.closed:
            await self.aiohttp_session.close()
            print("ClientSession has been closed")
        await super().close()

client = MyBot(intents=discord.Intents.all())


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready():
    print(f'{client.user} is now running!')

async def execute_command_logic(ctx, logic_function):
    try:
        # 确保会话有效
        if client.aiohttp_session is None or client.aiohttp_session.closed:
            await client.setup_hook()  # 如果会话关闭了，尝试重新初始化
        # await ensure_user(ctx, client.aiohttp_session)
        await logic_function(ctx, client.aiohttp_session)
    except Exception as e:
        print(f"Error during command execution: {e}")
        # 在这里处理异常，例如发送错误消息给用户
        await ctx.respond("An error occurred while processing your request.")

# add your code here:
@client.slash_command(name="play", description="Start to play")
async def play(ctx):
    await execute_command_logic(ctx, play_logic.play)




# STEP 5: MAIN ENTRY POINT
def main():
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
