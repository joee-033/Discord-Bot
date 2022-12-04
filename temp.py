@commands.hybrid_command(
        name="nick", description="Change, or view someones nickname!"
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    @app_commands.choices(
        action=[
            app_commands.Choice(name="change", value="change"),
            app_commands.Choice(name="view", value="view"),
        ]
    )
    async def nick(self, ctx, action, user: discord.Member = None, nick: str = None):
        if user is None:
            user = ctx.message.author

        match action:
            case "change":
                await user.edit(
                    nick=nick,
                    reason=f"Changed by, {ctx.message.author.id}, at {time.time()}.",
                )
                embed = discord.Embed(
                    title=f"Changed {user.name}#{user.discriminator}'s nickname!",
                    description=f"Nick changed for {user.name}#{user.discriminator}, from {user.display_name}.",
                    color=COLOUR_BURPLE,
                )

                await ctx.send(embed=embed)

            case "view":
                embed = discord.Embed(
                    title=f"{user.name}#{user.discriminator}'s nickname is:",
                    description=f"{user.display_name}",
                    color=COLOUR_BURPLE,
                )

                await ctx.send(embed=embed)

    @commands.hybrid_command(
        name="pfp", description="Displays your own, or a given user's profile picture."
    )
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def pfp(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.message.author

        embed = discord.Embed(
            title=f"{user.display_name}'s Discord Profile Picutre.",
            description=f"{user.name}#{user.discriminator} (UID: {user.id})",
            color=COLOUR_BURPLE,
        )

        if user.avatar is None:
            embed.set_image(
                url="https://ia803204.us.archive.org/4/items/discordprofilepictures/discordblue.png"
            )
        else:
            embed.set_image(url=user.avatar)

        await ctx.send(embed=embed)
