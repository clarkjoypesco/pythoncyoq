# Game has 3 or 4 levels
# Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard
lives = 3
score = 0
difficulty = [1, 2, 3]
levels_list = ['Level 1', 'Level 2', 'Level 3', 'Level 4']
sublevel_list = 4
questions_list = [['What is one plus one in math?', 'Who killed Magellan?', 'Who is the current president of the philippines?'],
                  ['If each apple cost 3 pesos How much would 5 apples cost in total?',
                   'In Science, What is H2O?',
                   'Sa wikang filipino ano ang tagalog ng slippers?'],
                  ]
answers_list = [['2', 'lapulapu', 'duterte'],
               ['15', 'water', 'tsinelas']]

name_input = raw_input('What is your name? \n')

print 'Hello ' + name_input + ' Welcome to Genius Quiz!'
user_input = raw_input('Select Difficulty: \n easy \n medium \n hard \n')

print 'You selected: ' + user_input + ' Difficulty'

print 'Loading level at the moment....'
print 'You have ' + str(lives) + ' lives left'


if user_input == 'easy':
    index = 0
    question_list = questions_list[index]
    answer_list = answers_list[index]
    while index <  len(question_list):
        answer_input =  raw_input(questions_list[0][index] + '\n')
       
        if answer_input == answers_list[0][index]:
            
            print 'Your Answer: ' + str(answer_input) + ' is correct!'
            index +=1
            score +=1
            
        else:
            print 'Your Answer: ' + str(answer_input) + ' is incorrect!'
            print 'Please try again!'
            lives -=1
            if lives <= 0:
                print 'Game Over!'
                break
            print 'You have ' + str(lives) + ' lives left'

if user_input == 'medium' or score==3:
    index = 0
    question_list = questions_list[index]
    answer_list = answers_list[index]
    while index <  len(question_list):
        answer_input =  raw_input(questions_list[1][index] + '\n')
       
        if answer_input == answers_list[1][index]:
            
            print 'Your Answer: ' + str(answer_input) + ' is correct!'
            index +=1
            score +=1
        else:
            print 'Your Answer: ' + str(answer_input) + ' is incorrect!'
            print 'Please try again!'
            lives -=1
            if lives <= 0:
                print 'Game Over!'
                break
            print 'You have ' + str(lives) + ' lives left'