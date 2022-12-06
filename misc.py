import discord
from discord import app_commands
from discord.ext import commands

COLOUR_BURPLE = discord.Color.from_rgb(91, 32, 154)


class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="latency",
        description="Displays the bots current latency, in milli-seconds.",
    )
    @app_commands.guilds(discord.Object(id=1048701639537729619))
    @app_commands.choices(
        unit=[
            app_commands.Choice(name="seconds", value="s"),
            app_commands.Choice(name="milliseconds", value="ms"),
        ]
    )
    async def latency(self, ctx, unit: str = None):
        match unit:
            case "s":
                latency = round(self.bot.latency * 1)
                if latency == 0:
                    description = f"⏰ The current bots latency is **under one second**! Wow, thats fast! ⏰"

                else:
                    description = (
                        f"⏰ The current bots latency is **{latency} second(s)**. ⏰"
                    )

            case "ms":
                latency = round(self.bot.latency * 1000)
                description = (
                    f"⏰ The current bots latency is **{latency} milliseconds**. ⏰"
                )

        embed = discord.Embed(
            title="⌛ Bot Latency... ⌛",
            description=f"\n{description}",
            color=COLOUR_BURPLE,
        )
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Misc(bot))
