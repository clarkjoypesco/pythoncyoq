# cyoq = Code Your Own Quiz by Clark Joy Pesco
# Game has 3 or 4 levels
# Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard

# track lives
lives = 3

# track score
score = 0

# list for difficulty which is used for comparing with user input to select a difficulty
difficulty_list = ['easy', 'medium', 'hard']

# list of questions and at the moment there are 3 category questions and each category have 3 questions
questions_list = [['What is one plus one in math?', 'Who killed Magellan?', 'Who is the current president of the philippines?'],
                  ['If each apple cost 3 pesos How much would 5 apples cost in total?',
                   'In Science, What is H2O?',
                   'Sa wikang filipino ano ang tagalog ng slippers?'],
                  ['What programming language has logo of cup of coffee?',
                      'Extension file of Hypertext Markup Language?', 'First Name of Miss Universe Wurtzbach?']
                  ]

# list of answers that corresponds to the questions_list by using its index in the list
answers_list = [['2', 'lapulapu', 'duterte'],
                ['15', 'water', 'tsinelas'],
                ['java', 'html', 'pia']]


# prompts the user to input their name
name_input = raw_input('What is your name? \n')

# prints Welcome Screen
print 'Hello ' + name_input + ' Welcome to Brainy Quiz!'

# prompts the user to select difficulty
user_input = raw_input('Select Difficulty: \n easy \n medium \n hard \n')
print 'You selected: ' + user_input + ' Difficulty'
print 'Loading level at the moment....'

# prints the lives of the user in the game
print 'You have ' + str(lives) + ' lives left'

# search difficulty list if user input difficulty exist
# if not it returns a value of 0 which corresponds difficulty easy
def level_in_pos(difficulty, difficulty_list):
    index = 0
    while index < len(difficulty_list):
        if difficulty == difficulty_list[index]:
            return index
        index += 1
    print 'difficulty not exist! You will be redirected to easy level'
    return 0

# calls the function level in pos and gets the value
# and assign the value to level
level = level_in_pos(user_input, difficulty_list)


# this variable is myflag so when i is greater than or equal to 1
# the game is finished
i = 0

# making the game in infinite loop
# inside it is the main logic of the game
while i < 1:
    # tracks the index of questions and answers list
    index = 0
    # gets a specific category in the questions liss
    question_list = questions_list[index]

    # gets a specific category in the answers list
    answer_list = answers_list[index]

    # looping to every question in a specific category
    while index < len(question_list):
        
        # prompts the user a question form a specific category and then
        # gets the answer to process
        answer_input = raw_input(questions_list[level][index] + '\n')

        # checks the the value of answer_input 
        if answer_input == answers_list[level][index]:

            # shows the answer is correct in the screen
            print 'Your Answer: ' + str(answer_input) + ' is correct!'

            # added a value of 1 to index in order for the question to go next
            index += 1

            # added a value of 1 to score 
            score += 1

            # shows the current score in the screen
            print 'Score: ' + str(score) 

            # checks if score is equal to 3
            if score == 3:
                # shows the Congratulatory message in the screen
                print 'Congratulations!! You have completed Level ' + \
                    str(level+1)
                # resets the score back to 0 when a level is finished
                score = 0

                # increments the value of level by 1 
                level += 1

                # checks if current level is equal to 3 and if it does
                if level == 3:

                   # shows a prompt to user if he/she want to to try again or not
                    level_input = raw_input('Do You want to try Again? yes or no\n')
                    
                    # chekcs the user input if its no it quits the game
                    if level_input == 'no':
                        i += 1
                    #checks the user input if its yes it restarts the game
                    if level_input == 'yes':
                        score = 0
                        level = 0
                        lives = 3

        # if user inputs a incorrect answer
        else:
            # shows an incorrect message to ther user
            print 'Your Answer: ' + str(answer_input) + ' is incorrect!'
            print 'Please try again!'
            # lives subtracted by 1 for an incorrect answer
            lives -= 1

            # checks if lives is equal or less than 0
            if lives <= 0:

                # shows a game over message
                print 'Game Over!'
                # prompts the user to try again or not
                level_input = raw_input('Do You want to try Again? yes or no\n')
                
                 
                # chekcs the user input if its no it quits the game
                if level_input == 'no':
                        i += 1
                        break

                #checks the user input if its yes it restarts the game
                if level_input == 'yes':
                        score = 0
                        level = 0
                        lives = 3
                else:
                     # quits the game
                    print 'Exit Game'
                    print 'Thank you for playing Brainy Quiz'
                    i += 1
                    break
             
            # shows the lives of user in the game
            print 'You have ' + str(lives) + ' lives left'
