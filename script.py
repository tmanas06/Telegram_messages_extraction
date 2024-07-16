from dotenv import load_dotenv
import os
import csv
import asyncio
from datetime import datetime
from telethon import TelegramClient, errors

# Set up the Telegram client
load_dotenv()  # Load environment variables from .env file

api_id = os.environ['api_id']
api_hash = os.environ['api_hash']
username = os.environ['username']
client = TelegramClient(username, api_id, api_hash)

async def update_messages_csv():
    with open('telegram_messages_complete.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        async with client:
            dialogs = await client.get_dialogs()
            print(f"Total dialogs found: {len(dialogs)}")
            for dialog in dialogs:
                if not dialog.is_group and not dialog.is_channel:
                    dialog_type = "Individual"
                    async for message in client.iter_messages(dialog.id):
                        try:
                            sender_name = "Unknown"
                            receiver_name = "Unknown"
                            sender = await message.get_sender()
                            receiver = message.to_id
                            sender_name = sender.first_name if sender else "Unknown"
                            receiver_entity = await client.get_entity(receiver)
                            receiver_name = receiver_entity.first_name if receiver_entity else "Unknown"

                            send_time = message.date.strftime("%Y-%m-%d %H:%M:%S")
                            if message.message:
                                message_text = message.message.replace('\n', ' ')
                            else:
                                message_text = "No message content"

                            writer.writerow([dialog.name, dialog.id, dialog_type, sender_name, message.sender_id, receiver_name, message.to_id, message_text, send_time])
                            print(f"Message from {sender_name} ({message.sender_id}) to {receiver_name} ({message.to_id}) at {send_time}: {message_text}")
                        except errors.FloodWaitError as e:
                            print(f"Error: {e} - Waiting for {e.seconds} seconds.")
                            await asyncio.sleep(e.seconds)
                            continue
                        except Exception as e:
                            print(f"Error: {e}")
                            continue

# Continuous loop to update messages every X seconds
async def continuous_update(interval_seconds):
    while True:
        try:
            await update_messages_csv()
            await asyncio.sleep(interval_seconds)
        except Exception as e:
            print(f"Error: {e}")

# Run the continuous update loops
async def main():
    await client.start()
    await continuous_update(interval_seconds=360)  # Update every 2 minutes

# Run the main function
asyncio.run(main())
