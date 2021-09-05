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

      # 以下田園都市線以外に拡張したい場合に
      COMMAND: denentoshi
      DESCRIPTION: ボイスチャンネルの名前をランダムな田園都市線の駅名に変更します。
      STATIONS: 渋谷,池尻大橋,三軒茶屋,駒沢大学,桜新町,用賀,二子玉川,二子新地,高津,溝の口,梶が谷,宮崎台,宮前平,鷲沼,たまプラーザ,あざみ野,江田,市が尾,藤が丘,青葉台,田奈,長津田,つくし野,すずかけ台,南町田グランベリーパーク,つきみ野,中央林間

```
