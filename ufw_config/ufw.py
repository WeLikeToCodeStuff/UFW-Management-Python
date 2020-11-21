import os
from sys import exit


def main():
    os.system("clear")
    print(
        "\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015"
    )
    print("Thank you for using the UFW configure tool")
    print("Made by NeonDevelopment")
    print("\u00A9 WeLikeToCodeStuff 2020 - Current year")
    print(
        "\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015"
    )

    acceptdeny = input(
        "Would you like to deny or to accept a port? Type deny to deny and accept to accept: "
    )
    if acceptdeny == "accept":
        acceptport = input("What port would you like to accept?: ")
        os.system("ufw allow " + acceptport)
        print(f"Port '{acceptport}' opened!")
        exit()

    elif acceptdeny == "deny":
        denyport = input("What port would you like to deny?: ")
        os.system("ufw deny " + denyport)
        print(f"Port '{denyport}' closed!")
        exit()

    else:
        print("That's not a valid option. Please choose 'accept' or 'deny'")
        exit()
