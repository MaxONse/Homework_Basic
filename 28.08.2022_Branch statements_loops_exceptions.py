import random
print("welcome ro game:\'Rock, paper, scissors, lizard, spock")
print('The game  will go to this computer')
print('Use big letters to select: R, P, SC, SP, L')

user_score = 0
user_choice = 0
bot_score = 0
bot_choice = 0

print('-------game starting-------')
while True:
    choice2 = input("Maybe play, y/n\n")
    if choice2 == 'y':
        print("Let's play")
        for i in range(5):
            print('----Round #', str(i+1), '----')
            bot_choice = random.choice(['R', 'SC', 'P', 'L', 'SP'])
            user_choice = input("Your choice")
            print('You choice:', user_choice, 'bot choice:', bot_choice)
            if user_choice == bot_choice:
                print("Draw")
            elif user_choice == 'R':
                if bot_choice == 'SC' and 'L':
                    user_score = user_score + 1
                    print('player won this round')
                else:
                    bot_score = bot_score + 1
                    print('bot won round')
            elif user_choice == 'SC':
                if bot_choice == 'P' and 'L':
                    user_score = user_score + 1
                    print('player won this round')
                else:
                    bot_score = bot_score + 1
                    print('bot won round')
            elif user_choice == 'P':
                if bot_choice == 'R' and 'SP':
                    user_score = user_score + 1
                    print('player won this round')
                else:
                    bot_score = bot_score + 1
                    print('bot won round')
            elif user_choice == 'L':
                if bot_choice == 'P' and 'SP':
                    user_score = user_score + 1
                    print('player won this round')
                else:
                    bot_score = bot_score + 1
                    print('bot won round')
            elif user_choice == 'SP':
                if bot_choice == 'R' and 'SC':
                    user_score = user_score + 1
                    print('player won this round')
                else:
                    bot_score = bot_score + 1
                    print('bot won round')
            else:
                print('Error')
                continue

        if user_score > bot_score:
            print("You Won with total score:", user_score, "VS", bot_score)
        elif user_score < bot_score:
            print("Bot Winner, he win with total score:", bot_score, "VS", user_score, " HA HA HA")
        else:
            print("There is no winner", user_score, "=", bot_score)
    else:
        print("BYE")
        break