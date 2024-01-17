import time
import random
import menu
import colours

def main_menu():  # Menu Start
    
    print(colours.bright_magenta + menu.header)
    print(colours.bright_cyan + menu.options)

    choose = input("Choose an option: ") 
    
    while choose not in range(1, 10):
        
        print("That is not a valid option.")
        
        choose = input("Choose an option: ")  
        
        if int(choose) in range(1, 10):
            break

main_menu()  
