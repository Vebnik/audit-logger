from discord.ext import commands
from datetime import datetime


class Ready(commands.Cog):

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f'App started at {datetime.now()}')
        
