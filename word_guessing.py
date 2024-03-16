import random

def main():
    word = random.choice(["RECURSION", "ITERATION", 'CONDITIONS', 'PROGRAMMING', 'VARIABLES'])
    unknown = len(word) * '_'  #TO PRINT THE  WORD TO BE GUESSES IN THIS FORMAT __
    points = 12
    print("Word Prediction Game")
    print(unknown)
    print('\nThe word has', len(word), 'letters.')
    print('You have', points, 'points in total to start with.')
    print('You can buy a letter at a cost of 2 points.')
    print('You can buy 4 letters at max.')
    print('You can make a guess at max 3 times.')
    print('Each wrong guess results in 2 point loss.')

    guess_count = 3
    word_count = 4
    previous_letters = []
    
    while points > 0:
        answer = userAnswer(points)
        if answer == '1' and guess_count > 0:
            guess = input('Make a guess: ')
            guess_count -= 1
            if word != guess:
                print('Incorrect guess!')
                print(unknown)
                points -= 2                
            else:
                print('Correct!')
                print(f'The word is "{word}"')
                print('The game has ended.')
                break
        elif answer == "2" and word_count > 0:
            random_letter = random.randrange(0, len(word))
            points -= 2
            word_count -= 1
            
            while random_letter in previous_letters:
                random_letter = random.randrange(0, len(word)) 
            unknown = unknown[:random_letter] + word[random_letter] + unknown[random_letter+1:]
            previous_letters.append(random_letter)
            print(f'The letter purchased is {word[random_letter]}\n')
            print(unknown)
        elif word_count == 0:
            print('You cannot buy a letter anymore.')
            print(unknown)
        else:
            print('You cannot buy a letter anymore.')
            print(f'The answer is "{word}"')
            break
    else:
        print('No points left or you finished guessing.')
        print(f'The answer is "{word}"')
        print('The game has ended.')

        
def userAnswer(pointLast):
    print(f'**Remaining Points: {pointLast}**')
    print('\n 1. Make a guess')
    print('2. Buy a letter \n')
    user_input =  input('What to do: ')
    return user_input
    

if __name__ == '__main__':
    main()
