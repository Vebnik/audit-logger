from discord.ext import commands
from discord import Member, Bot
from os import getenv

class Audit(commands.Cog):

    bot: Bot

    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_member_update(self, before: Member, after: Member) -> None:
        if before.roles != after.roles:
            try:
                channel = self.bot.get_channel(int(getenv('LOG_CHANNEL')))

                async for entry in after.guild.audit_logs(limit=1):
                    await channel.send(f'{entry.user} change roles to {entry.target}')
            except Exception as ex:
                print(ex)


