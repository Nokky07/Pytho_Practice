import time
import random
import art
from colours import *
import sys
import replit


def hello_world():
  input(
      f"\n{darken}Press {bright_blue}[{Blue}ENTER{bright_blue}]{reset} {darken}To Start{reset} "
  )


def main_menu():  # Menu Start

  print(Green + "                        " +
        f"\n\n\n\n\n\n\n\n{art.level_heading}")

  print(bright_cyan + art.options)

  user = int(input("Choose an option: "))

  while user not in range(1, 10):

    print(Red + "\n\n      _-_-_-Invalid option-_-_-_      \n\n")

    user = int(input(bright_cyan + "\n\nChoose an option: "))

    if user in range(1, 10):
      break

  print(Red + "\n\nWhile Loop has intially been broken\n\n"
        )  # Developer purposes will be removed later on in implementation.

  if user == 1:
    replit.clear()
    hello_world()


print(bright_magenta + art.header)
print(
    f"\n{darken}{italic}Created by {reset}{Orange}Nokky07{reset}{darken}'s {reset}{bright_yellow}Standard Type{reset}{darken}...{reset}"
)

main_menu()
