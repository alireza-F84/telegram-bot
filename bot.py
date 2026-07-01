from telethon import TelegramClient
import asyncio
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_username = os.environ["BOT_USERNAME"]

client = TelegramClient("session", api_id, api_hash)

async def main():
    await client.start()

    await client.send_message(bot_username, "سلام")

    await asyncio.sleep(7)

    messages = await client.get_messages(bot_username, limit=1)

    text = messages[0].text if messages else "no response"

    with open("data.txt", "w", encoding="utf-8") as f:
        f.write(text)

    await client.disconnect()

asyncio.run(main())
