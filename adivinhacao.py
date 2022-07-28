import random


def play():
    print("#########################")
    print("welcome to the game bitch")
    print("#########################")

    # secret_number = round(random.random() * 100)

    boom = "On the target, congrats!!!"
    wrong = "try again"
    max = 100
    difficult = 0
    score = 1000
    sub = 0

    print("You can choose 3 levels to play the game ")
    print("easy   [1]")
    print("medium [2]")
    print("hard   [3]")

    level = int(input("level?: "))

    if level == 1:
        difficult = 10
        sub = 100
    elif level == 2:
        difficult = 26
        sub = 70
    else:
        difficult = 50
        sub = 40
    secret_number = random.randrange(1, difficult)

    for test in range(1, max + 1):
        print("shoot number ", test)
        print("Your score $$${}$$$".format(score))
        shoot = int(input("Guess a number: "))

        if secret_number == shoot:
            print(boom)
            print("Your total score $$$$$$$$${}$$$$$$$$$".format(score))
            break
        else:
            if shoot < secret_number:
                print("Wrong, maybe a little more")
                print("-------------------")
                score = score - sub
            else:
                print("Wrong, maybe less")
                print("----------")
                score = score - sub

        if shoot > 100 or shoot < 1:
            print("The number must be between (0 and 100)")
            continue


if __name__ == "__main__":
    play()
