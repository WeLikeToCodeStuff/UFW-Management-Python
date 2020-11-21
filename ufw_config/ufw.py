import os

os.system("clear")
print(u'\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015')
print("Thank you for using the UFW configure tool")
print("Made by NeonDevelopment")
print(u'\u00A9 WeLikeToCodeStuff 2020 - Current year')
print(u'\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015\u2015')

acceptdeny = input("Would you like to deny or to accept a port?\n If you would like to accept or deny a port range, please type portrange.: ")
if acceptdeny == "accept":
    acceptport = input("What port would you like to accept?: ")
    os.system("sudo ufw allow " + acceptport)
    print(f"Port '{acceptport}' opened!")
    exit()

elif acceptdeny == "deny":
    denyport = input("What port would you like to deny?: ")
    os.system("sudo ufw deny " + denyport)
    print(f"Port '{denyport}' closed!")
    exit()
elif acceptdeny == "portrange":
    rangelist = input("What is the portrange you would like to allow/deny?\n (Please seperate the range with a ':'. Example: '100:200': ")
    rangestatus = input("Would you like to accept or deny this port range?: ")
    rangetype = input("What type of port would you like to deny? (tcp or udp (Please only use lowercase!!))")
    if rangestatus == "accept":
        os.system("sudo ufw accept " + rangelist + "/" + rangetype)
        print(f"Port range '{rangelist}' opened!")
    elif rangestatus == "deny":
        os.system("sudo ufw deny " + rangelist + "/" + rangetype)
        print(f"Port range '{rangelist}' closed!")

else:
    print("That's not a valid option. Please choose 'accept', 'deny', or 'portrange'")
    exit()
