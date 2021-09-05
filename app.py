import os
import random

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

TOKEN = os.getenv("TOKEN")
VOICE_CHANNEL_ID = os.getenv("VOICE_CHANNEL_ID")
COMMAND = os.getenv("COMMAND", "denentoshi")
DESCRIPTION = os.getenv("DESCRIPTION", "ボイスチャンネルの名前をランダムな田園都市線の駅名に変更します。")
STATIONS = os.getenv("STATIONS", "渋谷,池尻大橋,三軒茶屋,駒沢大学,桜新町,用賀,二子玉川,二子新地,高津,溝の口,梶が谷,宮崎台,宮前平,鷲沼,たまプラーザ,あざみ野,江田,市が尾,藤が丘,青葉台,田奈,長津田,つくし野,すずかけ台,南町田グランベリーパーク,つきみ野,中央林間").split(",")


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

@slash.slash(name=COMMAND, description=DESCRIPTION)
async def on_command(ctx: SlashContext):
    if not ctx.guild:
        return await ctx.send(
            content="このコマンドは DM で使用できません。"
        )

    channel = ctx.guild.get_channel(VOICE_CHANNEL_ID)
    if not channel:
        return await ctx.send(
            content="ボイスチャンネルの取得に失敗しました。 `VOICE_CHANNEL_ID` が間違っている可能性があります。"
        )

    await channel.edit(name=random.choice(STATIONS))

if __name__ == "__main__":
    if not TOKEN or not VOICE_CHANNEL_ID:
        raise Exception("TOKEN または VOICE_CHANNEL_ID が設定されていません。")

    bot.run(TOKEN)
