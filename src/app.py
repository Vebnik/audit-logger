import discord


from src.models import Config
from src.cogs import (
    audit_update, ready
)


class App:

    cfg: Config
    client: discord.Bot

    def __init__(self, cfg: Config) -> None:
        try:
            self.client = discord.Bot(intents=discord.Intents.all())
            self.cfg = cfg
            self._init_handlres(self.client)
        except Exception as ex:
            print(ex)

    def _init_handlres(self, client: discord.Bot) -> None:
        cogs = [
            audit_update.Audit,
            ready.Ready
        ]

        for cog in cogs:
            client.add_cog(cog(client))

    def run(self) -> None:
        self.client.run(self.cfg.token)
