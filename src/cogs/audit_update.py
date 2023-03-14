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
                diff_roles = set(after.roles).symmetric_difference(set(before.roles))
                action = 'add' if len(after.roles) > len(before.roles) else 'delete'

                async for entry in after.guild.audit_logs(limit=1):
                    content = f'```fix\n{entry.user} {action} {" ".join([role.name for role in diff_roles])} roles to {entry.target}\n```'
                    await channel.send(content)
            except Exception as ex:
                print(ex)

