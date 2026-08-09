from __future__ import annotations

import logging

import discord
from discord.ext import commands


log = logging.getLogger(__name__)


COGS: tuple[str, ...] = (
    "admin",
)


class Allay(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()

        super().__init__(
            commands.when_mentioned,

            help_command=None,
            description=None,
            intents=intents,

        )


    async def load_extensions(self) -> None:
        for cog in COGS:
            extension = f"allay.cogs.{cog}"

            try:
                await self.load_extension(extension)
            except commands.ExtensionError:
                log.exception("Failed to load extension %s", cog)
            else:
                log.info("Loaded extension %s", cog)


    async def setup_hook(self) -> None:
        await self.load_extensions()


    async def on_ready(self) -> None:
        log.info("Ready as %s (ID: %s)", self.user, self.user.id)
