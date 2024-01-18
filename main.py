import time
import random
import art
import colours
import sys


def hello_world():
  print("chese")


def main_menu():  # Menu Start

  print(colours.Green + "                        " +
        f"\n\n\n\n\n\n\n\n{art.level_heading}")

  print(colours.bright_cyan + art.options)

  user = int(input("Choose an option: "))

  while user not in range(1, 10):

    print(colours.Red + "\n\n      _-_-_-Invalid option-_-_-_      \n\n")

    user = int(input(colours.bright_cyan + "\n\nChoose an option: "))

    if user in range(1, 10):
      break

  if user == 1:
    hello_world()

  print(colours.Red + "\n\nWhile Loop has intially been broken\n\n"
        )  # Developer purposes will be removed later on in implementation.


print(colours.bright_magenta + art.header)
print(
    f"\n{colours.darken}{colours.italic}Created by {colours.reset}{colours.Orange}Nokky07{colours.reset}{colours.darken}'s {colours.reset}{colours.bright_yellow}Standard Type{colours.reset}{colours.darken}...{colours.reset}"
)

main_menu()
hello_world()
