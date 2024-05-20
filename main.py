import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style, Back
import asyncio
import colorama
import pypresence
import re, http.client, ctypes, sys, threading, json, random, sys, re, threading, time, os, datetime
from pypresence import Presence

def center_text(text):
    columns = os.get_terminal_size().columns
    return text.center(columns)

def loading_animation():
    final_text = 'Discord Presence by DevRaske ★ | https://github.com/DevRaske'
    text = ''
    for character in final_text:
        ctypes.windll.kernel32.SetConsoleTitleW(text)
        text += character
        time.sleep(0.05)

    ctypes.windll.kernel32.SetConsoleTitleW(final_text)

def loading_print(final_text):
    text = ''
    for character in final_text:
        sys.stdout.write(character)
        time.sleep(0.025)

threading.Thread(target=loading_animation).start()

def back():
    mainlogo()
    menu()

def cya():
    print(center_text(Fore.LIGHTRED_EX + "  /$$$$$$  /$$     /$$ /$$$$$$"))
    print(center_text(Fore.LIGHTRED_EX + " /$$__  $$|  $$   /$$//$$__  $$"))
    print(center_text(Fore.LIGHTRED_EX + "| $$  \__/ \  $$ /$$/| $$  \ $$"))
    print(center_text(Fore.LIGHTRED_EX +"| $$        \  $$$$/ | $$$$$$$$"))
    print(center_text(Fore.LIGHTRED_EX + "| $$         \  $$/  | $$__  $$"))
    print(center_text(Fore.LIGHTRED_EX + "|  $$$$$$/    | $$   | $$  | $$"))
    print(center_text(Fore.LIGHTRED_EX + " \______/     |__/   |__/  |__/"))                                           
    print("")
    print("")

def mainlogo():
    print(center_text(Fore.LIGHTRED_EX + " /$$$$$$$  /$$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$"))
    print(center_text(Fore.LIGHTYELLOW_EX + " | $$__  $$| $$__  $$| $$_____/ /$$__  $$| $$_____/| $$$ | $$ /$$__  $$| $$_____/"))
    print(center_text(Fore.LIGHTRED_EX + " | $$  \ $$| $$  \ $$| $$      | $$  \__/| $$      | $$$$| $$| $$  \__/| $$  "))
    print(center_text(Fore.LIGHTYELLOW_EX +"| $$$$$$$/| $$$$$$$/| $$$$$   |  $$$$$$ | $$$$$   | $$ $$ $$| $$      | $$$$$ "))
    print(center_text(Fore.LIGHTRED_EX + " | $$____/ | $$__  $$| $$__/    \____  $$| $$__/   | $$  $$$$| $$      | $$__/   "))
    print(center_text(Fore.LIGHTYELLOW_EX + " | $$      | $$  \ $$| $$       /$$  \ $$| $$      | $$\  $$$| $$    $$| $$   "))
    print(center_text(Fore.LIGHTRED_EX + " | $$      | $$  | $$| $$$$$$$$|  $$$$$$/| $$$$$$$$| $$ \  $$|  $$$$$$/| $$$$$$$$"))
    print(center_text(Fore.LIGHTYELLOW_EX + " |__/      |__/  |__/|________/ \______/ |________/|__/  \__/ \______/ |________/  "))                                             
    print("")
    print("")

def kate():
    print((Fore.LIGHTCYAN_EX + "                                               ******       ******"))
    print((Fore.LIGHTCYAN_EX + "                                             **********   **********"))
    print((Fore.LIGHTCYAN_EX + "                                           ************* *************"))
    print((Fore.LIGHTCYAN_EX +"                                          *****************************"))
    print((Fore.LIGHTCYAN_EX + "                                          *****************************"))
    print((Fore.LIGHTCYAN_EX + "                                          *****************************"))
    print((Fore.LIGHTCYAN_EX + "                                           ***************************"))    
    print((Fore.LIGHTCYAN_EX + "                                             ***********************"))   
    print((Fore.LIGHTCYAN_EX + "                                               *******************"))   
    print((Fore.LIGHTCYAN_EX + "                                                 ***************"))   
    print((Fore.LIGHTCYAN_EX + "                                                   ***********"))        
    print((Fore.LIGHTCYAN_EX + "                                                     *******"))      
    print((Fore.LIGHTCYAN_EX + "                                                       ***"))      
    print((Fore.LIGHTCYAN_EX + "                                                        *"))                                        
    print("")
    print("")

mainlogo()


client_id = ()
RPC = Presence(client_id)

def menu():
    print(center_text(Fore.LIGHTRED_EX + "[1] Set Custom Presence"))
    print(center_text(Fore.WHITE + "-"))
    print(center_text(Fore.LIGHTYELLOW_EX + "[2] Credits"))
    print(center_text(Fore.WHITE + "-"))
    print(center_text(Fore.LIGHTRED_EX + "[3] Quit"))

def credits():
    os.system('cls')
    print(center_text(Fore.LIGHTRED_EX + "C o d e d  b y"))
    print(center_text(Fore.LIGHTYELLOW_EX + "D e v R a s k e"))
    print(center_text(Fore.WHITE + "github.com/DevRaske"))
    print (f'''
    {Fore.LIGHTYELLOW_EX}
                                                 oooo$$$$$$$$$$$$oooo
                                             oo$$$$$$$$$$$$$$$$$$$$$$$$o
                                          oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
                          o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
                       oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
                       "$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
                         $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
                         $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
                          "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
                           $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
                          o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
                         $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
                         o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
                         $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
                        """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
                                   "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
                                     $$$o          "$$""$$$$$$""""           o$$$
                                      $$$$o                                o$$$"
                                       "$$$$o      o$$$$$$o"$$$$o        o$$$$
                                         "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                                            ""$$$$$oooo  "$$$o$$$$$$$$$"""
                                               ""$$$$$$$oo $$$$$$$$$$
           ''')
    choice = input(Fore.LIGHTRED_EX + "If you want to menu write > back: ")
    os.system('cls')
    mainlogo()
    main()

def mainpart():
    def input_client_id():
        while True:
            client_id = input(("Client ID: ")).strip()
            try:
                int(client_id)
                return client_id
            except ValueError:
                print(("Invalid Client ID try again."))

    client_id = input_client_id()
    RPC = Presence(client_id)
    RPC.connect()

    def update_presence(state, details, large_image, small_image, start_time=None, buttons=None):
        presence_data = {
            "state": state,
            "details": details,
            "large_image": large_image,
            "small_image": small_image,
            "instance": False
        }
        if start_time:
            presence_data["start"] = int(start_time.timestamp())
        if buttons:
            presence_data["buttons"] = buttons
        RPC.update(**presence_data)

    def load_all_presences():
        file_path = os.path.join(os.path.dirname(__file__), "presence.txt")
        presences = []
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    state, details, large_image, small_image = data[:4]
                    start_time = datetime.datetime.fromisoformat(data[4]) if data[4] != "None" else None
                    buttons = []
                    if len(data) > 5:
                        for i in range(5, len(data), 2):
                            if i + 1 < len(data):
                                buttons.append({"label": data[i], "url": data[i + 1]})
                    presences.append((state, details, large_image, small_image, start_time, buttons))
        except FileNotFoundError:
            print(("I couldn't find any file with saved presence."))
        return presences

    def select_presence(presences):
        if not presences:
            print(("I couldn't find any file with saved presence."))
            return None
        print(("Choose your Presence"))
        print(("-"))
        for i, presence in enumerate(presences):
            state, details, large_image, small_image, _, _ = presence
            print((f"{i + 1}. {state} - {details}"))
        selection = int(input(("Choose your saved presence. [TO CREATE NEW WRITE 0]: "))) - 1
        if 0 <= selection < len(presences):
            return presences[selection]
        else:
            print((""))
            return None

    def save_presence(state, details, large_image, small_image, start_time=None, buttons=None):
        file_path = os.path.join(os.path.dirname(__file__), "presence.txt")
        with open(file_path, "a") as file:
            file.write(f"{state},{details},{large_image},{small_image},")
            if start_time:
                file.write(f"{start_time.isoformat()},")
            else:
                file.write("None,")
            if buttons:
                for button in buttons:
                    file.write(f"{button['label']},{button['url']},")
            file.write("\n")

    presences = load_all_presences()
    if presences:
        selected_presence = select_presence(presences)
        if selected_presence:
            state, details, large_image, small_image, start_time, buttons = selected_presence
            update_presence(state, details, large_image, small_image, start_time, buttons)
            print(("Presence has been updated."))
            os.system('cls')
            mainlogo()
            main()
        else:
            print((""))
    else:
        selected_presence = None

    if not selected_presence:
        state = input(("Write state: "))
        details = input(("Write details: "))
        large_image = input(("Name of large image: "))
        small_image = input(("Name of small image: "))
        start_time_choice = input(("Do you want to set own time? (yes/no): ")).lower()
        start_time = None
        if start_time_choice == 'yes':
            start_time_str = input(("Write your own time (HH:MM): "))
            start_hours, start_minutes = map(int, start_time_str.split(':'))
            current_time = datetime.datetime.now()
            start_time = current_time.replace(hour=start_hours, minute=start_minutes, second=0, microsecond=0)
        buttons_choice = input(("Would you like to set own buttons with links? (yes/no): ")).lower()
        buttons = []
        if buttons_choice == 'yes':
            buttons_count = int(input(("Number of buttons (max. 2): ")))
            for i in range(buttons_count):
                label = input((f"Write description of button {i + 1}: "))
                url = input((f"Write URL for button {i + 1}: "))
                buttons.append({"label": label, "url": url})
        update_presence(state, details, large_image, small_image, start_time, buttons)
        print(("Rich Presence has been updated."))

        save_choice = input(("Would you like to save this Presence? (yes/no): ")).lower()
        if save_choice == 'yes':
            save_presence(state, details, large_image, small_image, start_time, buttons)
            print(("Presence has been saved."))
        os.system('cls')
        mainlogo()
        main()

def main():
    while True:
        menu()
        choice = input(Fore.LIGHTRED_EX + "Write your option: ")
        if choice == '1':
            os.system('cls')
            mainpart()
        elif choice == '2':
            credits()
        elif choice == '3':
            os.system('cls')
            cya()
            time.sleep(3)
            exit()
        elif choice == 'kate':
            os.system('cls')
            kate()
            time.sleep(5)
            exit()
        else:
            os.system('cls')
            mainlogo()

if __name__ == "__main__":
    main()
