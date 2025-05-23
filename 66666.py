#TheGreatYourKing
import random
import sys
import time
import os
from colorama import Fore
from time import sleep

def combo(s, color):
    for ASU in s + '\n':
        sys.stdout.write(color + ASU)
        sys.stdout.flush()
        sleep(1. / 1999)

# Define color sequence
colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

# File to store last used color index
color_file = "color_state.txt"

# Check if file exists, otherwise create it with index 0
if os.path.exists(color_file):
    with open(color_file, "r") as f:
        try:
            last_index = int(f.read().strip())
        except ValueError:
            last_index = 0
else:
    last_index = 0

# Get next color index
color_index = (last_index + 1) % len(colors)
current_color = colors[color_index]

# Save new index for next run
with open(color_file, "w") as f:
    f.write(str(color_index))

# ASCII Art
art = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⡄⣠⢄⣴⣠⣶⣠⣾⣤⣀⣴⣠⢄⣠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣄⣀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣷⣿⣿⣿⣿⠏⣿⣿⣿⡿⢏⣽⢋⡟⣹⣿⣿⢿⢿⣿⣿⣿⣿⣿⣷⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠙⣿⡟⣿⠘⣿⣩⣿⣠⣾⣿⣿⣿⣿⣿⣿⣶⣿⡧⠞⣿⣿⣿⣿⣿⣿⣶⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣼⣿⣾⣷⣿⣿⡿⣿⡏⢻⣏⠁⠻⣯⠙⢿⣿⣿⣿⣯⣉⣻⣿⣿⣿⣿⣿⣏⡀⠀⠀⠀⠀⠀
⣀⣠⣀⡀⠀⠀⠀⠀⠀⠀⠀⣰⢿⣿⣿⣿⢿⣿⢿⡿⠉⣿⠀⢻⣇⠀⠙⢆⠀⢻⡄⠘⢿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⡷⠂⠀⠀⠀⠀
⡽⣿⠹⡉⠓⢦⠀⠀⠀⠀⠀⠃⣾⢿⢿⡏⢸⡇⠸⡇⠀⠙⢆⣀⣽⡶⠶⠾⢷⣾⡧⠀⠈⠻⣿⣿⣟⣻⣿⣿⣿⣿⣿⣿⣷⡃⠀⠀⠀⠀
⡖⣿⣇⢣⠀⠘⡄⠀⠀⠀⠀⠀⣯⡼⠈⢇⠈⠻⣤⣽⣦⡶⠟⢋⣁⣀⣀⣀⣠⠞⠀⠀⠀⠀⢿⣿⣯⢷⣾⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀
⠤⠉⣿⡾⢦⣤⡇⠀⠀⠀⠀⠀⠸⣿⠒⠚⢿⠀⠈⠙⠿⣶⣿⣿⠿⠿⠿⠭⠛⠀⠀⠀⠀⠀⢸⣿⣿⣿⢿⣟⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀
⣦⣼⢷⣾⠯⠭⣧⠀⠀⠀⠀⠀⠀⣿⡷⣾⠟⠑⠂⠀⠀⠀⠈⠉⠀⢠⣤⣴⣦⣤⣤⡀⠀⠀⢸⣿⡟⣡⣾⣿⣿⣿⣿⣿⣿⡋⠀⠀⠀⠀
⠈⢻⡿⠁⣀⠤⠼⣆⠀⠀⠀⠀⠀⡎⢰⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣦⠤⠄⠀⠀⠙⠿⢸⡟⠻⣏⡻⣿⣿⣿⡏⠀⠀⠀⠀⠀
⠀⣸⢻⡏⠀⣀⡤⠼⡄⠀⠀⠀⠀⡇⠈⢿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⠛⠓⠒⠀⠀⠀⠀⣺⡗⠚⠋⣡⣿⣿⣿⠆⠀⠀⠀⠀⠀
⠀⡏⢸⢳⣎⡴⠂⠉⢹⡄⠀⠀⠀⢣⠀⣤⠽⠦⠤⣀⠀⠀⠀⠀⠀⠀⠘⣿⣟⠀⠀⠀⠀⠀⠀⢠⡉⠁⣠⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
⠀⣧⠋⣸⢻⣀⠔⠉⠁⠹⡄⠀⠀⢸⠀⢯⠶⠶⣦⣄⠙⠢⠀⠀⠀⠀⠀⠈⣿⠷⠀⠀⠀⠀⠀⡞⢓⡞⠉⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⣶⠃⢠⡇⠀⢷⠖⡽⠋⠉⠹⡄⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡾⠁⢰⡇⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⣽⠀⢸⡇⠀⠈⢟⣇⣀⣠⠤⠽⡄⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⡾⣿⠁⠀⢈⡇⠀⠘⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⢸⡄⠀⠀⠘⣿⣯⠀⠀⠀⠙⣄⣧⣤⣤⣴⣦⣤⣴⣤⣤⣠⣤⣴⣶⣿⣿⣿⠟⠉⢠⠋⠀⠀⢼⡇⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡇⣾⡇⠀⠀⠀⠸⡽⣷⣴⠒⠒⠛⣏⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠟⠋⠀⠀⢀⣽⠃⠀⠀⠘⡇⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣧⠇⠀⠀⠀⠀⠹⣿⣧⡠⠔⠒⠚⢧⠀⠀⠈⣿⣻⠛⣿⣿⡷⠛⠁⠀⠀⠀⢀⣼⡏⠀⠀⠀⠈⢿⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⡄⠀⠀⠀⠀⠀⠹⡛⣦⡀⢀⣀⠬⢧⡀⠀⢸⣿⠖⠛⠁⠀⠀⠀⠀⠀⠀⠘⢻⠃⠀⠀⠀⠀⢸⡀⠀⠀⢣⣀⠤⠖⠒⠒⠒⠢⢤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣸⡗⠉⠀⠀⢀⣱⡄⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⣸⡧⠴⠚⠉⠀⣀⣀⡄⠀⠀⢀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢏⢛⣶⠖⢊⣉⣀⠽⠦⣽⣷⡀⠀⠀⠀⠀⠀⠀⢀⣿⠋⠀⣠⠴⠚⠉⠀⣀⣠⣴⣾⣿⣿⣿⣷⣷⣶⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣾⡿⠞⠉⠓⠲⣶⣿⣿⣿⢧⠀⠀⠀⠀⠀⠀⢀⡿⠖⠋⠁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁
⠀⠀⠀⠀⠀⠀⢀⡤⢺⣿⣿⣟⣫⣴⣶⣤⣤⣀⣀⣙⣿⣿⣬⣤⣤⠤⣤⠴⠚⢉⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⣀⣠⣴⣾"""

# Print the art with the current color
combo(art, current_color)

print(current_color + """▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬
      ⚠ 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗦𝗖𝗥𝗔𝗣𝗘𝗥 𝗕𝗬  ~𝗬𝗼𝘂𝗿𝗞𝗶𝗻𝗴 ⚠
▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬""")

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl import functions
import time

api_id = input("𝗘𝗡𝗧𝗘𝗥 𝗔𝗣𝗜 𝗜𝗗 : ")
api_hash = input('𝗘𝗡𝗧𝗘𝗥 𝗔𝗣𝗜 𝗛𝗔𝗦𝗛 :')

def print_colored(text, color):
    colors = {
        'green': '\033[92m',
        'red': '\033[91m',
        'reset': '\033[0m'
    }
    print(f"{colors[color]}{text}{colors['reset']}")

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    group_to_scrape = input("Enter the username of the group to scrape members from (without @): ")

    group_to_add = input("Enter the username of the group to add members to (without @): ")

    if not await client.is_user_authorized():
        
        phone_number = input("Enter your phone number: ")

        await client.send_code_request(phone_number)

        otp = input("Enter the OTP: ")

        try:
            await client.sign_in(phone_number, otp)
        except SessionPasswordNeededError:
            password = input("Enter your 2FA password: ")
            await client.sign_in(password=password)

        print("Login successful.")
    else:
        print("Already logged in.")

    group_to_scrape = await client.get_entity(group_to_scrape)
    group_to_add = await client.get_entity(group_to_add)

    members = await client.get_participants(group_to_scrape)

    for member in members:
        if member.bot:
            print_colored(f"Skipping bot: {member.username}", "red")
            continue
        if member.username is None:
            print_colored(f"Skipping deleted account: {member.id}", "red")
            continue  

        try:
            
            await client(functions.channels.InviteToChannelRequest(
                group_to_add, [member]
            ))
            print_colored(f"{member.username} added successfully.", "green")
            time.sleep(1)
        except Exception as e:
            print_colored(f"Failed to add {member.username}: {e}", "red")
            time.sleep(1)  

with client:
    client.loop.run_until_complete(main())
    
#CodedBy : @xYourKing
#Shame On You If You're Copying This