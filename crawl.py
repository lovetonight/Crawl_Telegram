from telethon import TelegramClient
import asyncio

async def main():
    client = TelegramClient('./session_3.session', api_id=1, api_hash='api_hash')

    #
    channel_username = 'WatcherGuru'
    limit = 10

    try:
        await client.start()
        channel = await client.get_entity(channel_username)  
        messages = await client.get_messages(channel, limit=limit)
        for message in messages:
            print(message.text)
    except Exception as e:
        print("Error:", e)
    finally:
        await client.disconnect()

asyncio.run(main())