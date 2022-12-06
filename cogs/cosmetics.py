import datetime
import discord
from discord import app_commands
from discord.ext import commands

COLOUR_BURPLE = discord.Color.from_rgb(91, 32, 154)


class Cosmetics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, user):
        await user.add_roles(discord.utils.get(user.guild.roles, name="<roles>"))
        await user.add_roles(discord.utils.get(user.guild.roles, name="</roles>"))

    @commands.hybrid_command(
        name="whois", description="Displays different infomation about a given member!"
    )
    @app_commands.guilds(discord.Object(id=1048701639537729619))
    async def whois(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.message.author

        embed = discord.Embed(
            title=f"✵ /whois {user} ✵",
            description=f"➪ Displays all publically known infomation about the user, {user.name}.",
            color=COLOUR_BURPLE,
            url=f"https://discord.id/?prefill={user.id}",
            timestamp=datetime.datetime.now(),
        )
        embed.add_field(
            name="⤑ Username and Nickname:",
            value=f"➪ Username: {user.name}#{user.discriminator}\n➪ Server Nick: {user.display_name}",
            inline=False,
        )
        embed.add_field(
            name="⤑ Unique Account Identifier:",
            value=f"➪ {user.id}",
            inline=False,
        )
        embed.add_field(
            name="⤑ User Customisation:",
            value=f"➪ [Profile Picture Hyperlink]({user.display_avatar.url}).",
            inline=False,
        )
        embed.add_field(
            name="⤑ Significant Account Dates:",
            value=f"➪ Created At: {user.created_at.date()},\n➪ Joined {ctx.message.guild.name} At: {user.joined_at.date()}",
            inline=False,
        )
        embed.set_thumbnail(url=user.display_avatar)

        if user.system is True:
            embed.add_field(
                name="⤑ Miscellaneous Details:",
                value=f"➪ User is an official Discord System Account.",
                inline=False,
            )

        elif user.bot is True:
            embed.add_field(
                name="⤑ Miscellaneous Details:",
                value=f"➪ User is a Discord Bot.",
                inline=False,
            )

        embed.set_footer(
            text=f"✵ Data requested by: {ctx.message.author.display_name}. ✵",
            icon_url=ctx.message.author.display_avatar,
        )
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Cosmetics(bot))
