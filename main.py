# Main interface that runs other scripts

still_running = True

while still_running == True:
    print("Which script would you like to run?\nLeg: 1\nConfirm: 2")
    to_run = input()

    if to_run == "1":
        exec(open("./scripts/leg.py").read())
    elif to_run == "2":
        exec(open("./scripts/confirm.py").read())
    else:
        print("An error occurred")

    if input("Run again? ") != "y":
        still_running = False