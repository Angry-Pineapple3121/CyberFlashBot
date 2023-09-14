import discord

AUTH_TOKEN = open('access', 'r').read()

cogs_list = [
    'quiz'
]

bot = discord.Bot()

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='IT Department Rage'))
    print('■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■')
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Bot is ready to use!')
    print('■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■')

@bot.command(description="Sends the bot's latency.")
async def latency(ctx):
    botLatency = round(bot.latency, 2)
    botLatencyMs = round(bot.latency * 1000, 2)
    await ctx.respond(f":hourglass: Pong! Latency is **{botLatency}** seconds (**{botLatencyMs}** ms)")


bot.run(AUTH_TOKEN)