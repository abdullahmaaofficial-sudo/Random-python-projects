from datetime import datetime
import time, os

number_map = {
    '0': [" ###### ","##    ##","##    ##","##    ##","##    ##","##    ##"," ###### "],
    '1': ["   ##   "," ####   ","   ##   ","   ##   ","   ##   ","   ##   ","########"],
    '2': ["########","#     ##","      ##","########","##      ","##      ","########"],
    '3': ["########","      ##","      ##","########","      ##","      ##","########"],
    '4': ["##    ##","##    ##","##    ##","########","      ##","      ##","      ##"],
    '5': ["########","##      ","##      ","########","      ##","      ##","########"],
    '6': ["########","##      ","##      ","########","##    ##","##    ##","########"],
    '7': ["########","      ##","      ##","      ##","      ##","      ##","      ##"],
    '8': [" ###### ","##    ##","##    ##"," ###### ","##    ##","##    ##"," ###### "],
    '9': [" #######","##    ##","##    ##"," #######","      ##","      ##","      ##",],
    ':': ["   ##   ","   ##   ","   ##   ","        ","   ##   ","   ##   ","   ##   "]
}

def show_numbers(numbers : str):
    for i in range(7):
        for num in numbers:
            print(number_map.get(num)[i], end = "  ")
        print()

def clear_terminal():
    os.system('cls')
def user_input():
    while True:
        try:
            user_inp = int(input("Set timer (in minutes): ").strip())
        except ValueError:
            print("Input error: not a number.")
            continue
        if user_inp <= 0:
            print("Input error: invalid time.")
            continue
        return user_inp
    
def set_timer():
    minutes = user_input() - 1
    seconds = 60
    
    while minutes >= 0:
        clear_terminal()
        seconds -= 1
        show_numbers(f"{minutes:02d}:{seconds:02d}")

        if not seconds:
            minutes -= 1
            seconds = 60
        time.sleep(1)


def show_time():
    while True:
        clear_terminal()
        current_time = datetime.now().strftime("%H:%M:%S")
        current_time_l = current_time.split(':')
        hours = int(current_time_l[0]) 
        if hours > 12:
            current_time = f"{hours - 12:02d}:{current_time_l[1]}:{current_time_l[2]}"
        show_numbers(current_time)
        time.sleep(1)

print("======== Terminal Watch ========")
print("1- Show time.")
print("2- Set timer.\n")

choice = input("Enter your choice: ").strip()
if not choice in ['1','2']:
    print("Input error: Invalid choice.")

if choice == '1':
    show_time()
elif choice == '2':
    set_timer()