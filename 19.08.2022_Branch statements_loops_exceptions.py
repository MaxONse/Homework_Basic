import random

J = 10
Q = 10
K = 10
A = 11
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A] * 4
random.shuffle(cards)
print("Let's Play, diletant!!!")
count = 0
bot = 0

while True:
    choice2 = input("Maybe play, y/n\n")
    if choice2 == 'y':
        print("Let's play")
        while True:
            current = cards.pop()
            bot += current
            if 18 > bot:
                bot += current
                print("bot had a", bot)
                if 21 >= bot >= 18:
                    print("bot had a1", bot)
                    break
                elif bot > 21:
                    print("PEREBOR, he has a", bot)
                    break
            elif 18 <= bot <=21:
                print("Bot take a", bot)
                break
            elif bot > 21:
                print("PEREBOR, he had a",bot)
                break
            elif 18 <= bot <= 21:
                print("Bot has a", bot, "you turn")
        while True:
            if bot > 21:
                print("you WIN")
                break
            else:
                choice = input("Take Card, y/n\n")
                if choice == 'y':
                    current = cards.pop()
                    print("you hit a", current)
                    count += current
                    if count > 21:
                        print("You loose")
                        break
                    elif count == 21:
                        print("You WIN")
                        break
                    else:
                        print("You have", current, "and had a", count)
                elif choice == 'n':
                    print("Count is", count)
                    break
        while True:
            if count > 21:
                print("Bot WIN")
                break
            elif bot > 21:
                print("Yuo WIN")
                break
            elif count > bot:
                print("You WIN")
                break
            elif bot > count:
                print("Bot WIN")
                break
            else:
                print("Friendship is win")
                break
        continue
    else:
        print("BYE")
        break

