# Game has 3 or 4 levels
# Immediately after running the program, user is prompted to select a difficulty level from easy / medium / hard


lives = 3
score = 0
difficulty_list = ['easy', 'medium', 'hard']
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

def level_in_pos(difficulty, difficulty_list):
    index = 0
    while index < len(difficulty_list):
        if difficulty == difficulty_list[index]:
            return index
        index += 1
    return index


level = level_in_pos(user_input, difficulty_list)


i = 0
while i < 1:
    index = 0
    question_list = questions_list[index]
    answer_list = answers_list[index]
    while index < len(question_list):
        answer_input = raw_input(questions_list[level][index] + '\n')

        if answer_input == answers_list[level][index]:

            print 'Your Answer: ' + str(answer_input) + ' is correct!'
            index += 1
            score += 1
            if score == 3:
                print 'Congratulations!! You have completed Level ' + str(level+1)
                score = 0
                level+=1
                if level == 2:
                    i+=1

        else:
            print 'Your Answer: ' + str(answer_input) + ' is incorrect!'
            print 'Please try again!'
            lives -= 1
            if lives <= 0:
                print 'Game Over!'
                break
            print 'You have ' + str(lives) + ' lives left'






