# Cloud_Report
## Overview
This script uses the Telethon library to interact with the Telegram API and continuously update a CSV file with messages from chats. It retrieves messages, processes them to extract relevant information, and appends this data to telegram_messages_complete.csv.

## Components
Configuration: Loads API credentials from config.data using configparser.
Telegram Client Initialization: Initializes the Telegram client with the loaded credentials.
CSV Update Function: Defines an asynchronous function update_messages_csv to retrieve messages and append them to the CSV file.
Continuous Update Loop: Defines an asynchronous function continuous_update that runs update_messages_csv at regular intervals.
Main Function: Starts the Telegram client and runs the continuous update loop.
## Requirements
Python 3.6+\n
Telethon\n
configparser (Only for storing your personal info)
## Setup
Install Dependencies:\n
```bash
pip install -r requirements.txt
```
Execute the Script:\n
```bash
python your_script.py
```

# For Createing  Configuration File: Create a config.data file in the same directory as the script with the following content:

config.data
```bash
[cred]
id = your_api_id
hash = your_api_hash
phone = youre phone number with country code included
```

## Usage

1. Run the script:
    ```bash
    python bot.py
    ```

2. The script will:
    - Connect to your Telegram account.
    - Retrieve and log messages from individual dialogs into `telegram_messages_complete.csv`.
    - Continu

# Input
![image](https://github.com/Wallet-Hunter/Cloud_Report/assets/113188197/15930a2c-4199-4f7c-89c6-bda4fd373e03)
# output
![image](https://github.com/Wallet-Hunter/Cloud_Report/assets/113188197/79bcead1-cafb-496a-bd2f-d14ab9e7fa2a)
