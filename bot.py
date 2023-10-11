import discord
from discord.ext import commands

# Define your intents
intents = discord.Intents.default()
intents.message_content = True  # Allow reading message content

# Initialize the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def send_dm(ctx, user_id: int, *, message: str):
    try:
        # Fetch the user using the user ID
        user = await bot.fetch_user(user_id)

        if user:
            # Send a DM to the user
            await user.send(message)
            await ctx.send(f'Successfully sent a DM to {user.name}.')
        else:
            await ctx.send("User not found.")
    except discord.Forbidden:
        await ctx.send(f'Failed to send a DM. The user may have DMs disabled or have blocked the bot.')


# Run the bot with your token
bot.run('bot id')
