from __future__ import annotations

from typing import Literal

import discord
from discord.ext import commands

from allay.bot import Allay


class Admin(commands.Cog):
    def __init__(self, bot: Allay) -> None:
        self.bot = bot

    async def cog_check(self, ctx: commands.Context[Allay]) -> bool:
        return await self.bot.is_owner(ctx.author)

    @commands.command()
    @commands.guild_only()
    async def sync(
        self,
        ctx: commands.Context[Allay],
        guilds: commands.Greedy[discord.Object],
        spec: Literal["~", "*", "^"] | None = None,
    ) -> None:
        """Sync the application command tree.

        sync        global sync, propagates to clients within the hour
        sync ~      sync commands registered to this guild only
        sync *      copy the global commands to this guild and sync, instant
        sync ^      clear this guild's commands and sync
        sync <ids>  sync the given guild IDs
        """
        if guilds:
            synced = 0
            for guild in guilds:
                try:
                    await self.bot.tree.sync(guild=guild)
                except discord.HTTPException:
                    continue
                synced += 1

            await ctx.send(f"Synced the tree to {synced}/{len(guilds)} guilds.")
            return

        if spec == "~":
            synced = await self.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            self.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await self.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            self.bot.tree.clear_commands(guild=ctx.guild)
            await self.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await self.bot.tree.sync()

        scope = "globally" if spec is None else "to the current guild"
        await ctx.send(f"Synced {len(synced)} commands {scope}.")

    @commands.command()
    async def load(self, ctx: commands.Context[Allay], *, extension: str) -> None:
        """Load an extension."""
        try:
            await self.bot.load_extension(extension)
        except commands.ExtensionError as error:
            await ctx.send(f"{error.__class__.__name__}: {error}")
        else:
            await ctx.send(f"Loaded `{extension}`.")

    @commands.command()
    async def unload(self, ctx: commands.Context[Allay], *, extension: str) -> None:
        """Unload an extension."""
        try:
            await self.bot.unload_extension(extension)
        except commands.ExtensionError as error:
            await ctx.send(f"{error.__class__.__name__}: {error}")
        else:
            await ctx.send(f"Unloaded `{extension}`.")

    @commands.command()
    async def reload(self, ctx: commands.Context[Allay], *, extension: str) -> None:
        """Reload an extension, picking up code changes without a restart."""
        try:
            await self.bot.reload_extension(extension)
        except commands.ExtensionError as error:
            await ctx.send(f"{error.__class__.__name__}: {error}")
        else:
            await ctx.send(f"Reloaded `{extension}`.")


async def setup(bot: Allay) -> None:
    await bot.add_cog(Admin(bot))
