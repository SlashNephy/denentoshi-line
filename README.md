# denentoshi-line

Discord のボイスチャンネルの名前をランダムな田園都市線の駅名に変更する Discord Slash Command

[Add bot to your Discord Server](https://discord.com/api/oauth2/authorize?client_id=883995133413060628&permissions=1040&scope=bot%20applications.commands)

## docker-compose (self hosted)

```yml
version: '3.8'

services:
  bot:
    container_name: denentoshi-line
    image: ghcr.io/slashnephy/denentoshi-line
    restart: always
    environment:
      TOKEN: xxx # Discord bot トークン
      VOICE_CHANNEL_ID: 123456790 # 対象のボイスチャンネル ID

```
