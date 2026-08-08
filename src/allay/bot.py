from __future__ import annotations

import discord
from discord.ext import commands


class Allay(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        
        super().__init__(
            commands.when_mentioned,

            help_command=None,
            description=None,
            intents=intents,

        )

    async def setup_hook(self) -> None:
        pass

    async def on_ready(self) -> None:
        pass