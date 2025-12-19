import discord

# 1) intents を用意する（メッセージ本文を読むための設定）
intents = discord.Intents.default()
intents.message_content = True  # 本文を読むのに必要

# 2) Botクライアントを作る
client = discord.Client(intents=intents)

# 3) 「ExcelのA列」用データを貯める入れ物（1行=1レコード）
data = []

@client.event
async def on_ready():
    print(f"ログインしました: {client.user}")

@client.event
async def on_message(message):
    # 4) Bot自身の発言を無視（無限ループ防止）
    if message.author == client.user:
        return

    # 5) ユーザーが送った文字列を取得
    text = message.content

    # 6) 1列目として追加（= 1行分のリストとして追加）
    data.append([text])

    # 7) 動作確認のため、コンソールに表示
    print("追加しました:", [text])
    print("現在のdata:", data)

# 8) 自分のBOTトークンを入れる（絶対に公開しない）
client.run("")
