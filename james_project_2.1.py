
parts_of_speech1 = ["WORD1","WORD2","WORD3","WORD4"]

easy_string = "You have brians in your WORD1. You have WORD2 in your shoes. You can WORD3 yourself in any direction you choose. You're on your own, and WORD4 know what you know. And you are the guy who'll decide where to go."
easy_string_finished = "You have brians in your head. You have feet in your shoes. You can move yourself in any direction you choose. You're on your own, and you know what you know. And you are the guy who'll decide where to go."
easy_solutions = ["head", "feet", "move", "you"]

medium_string = "The more that you read, the WORD1 things you will know. The more that you WORD2, the more WORD3 you'll WORD4."
medium_solutions = ["more", "learn", "places", "go"]
medium_string_finished = "The more that you read, the more things you will know. The more that you learn, the more places you'll go."

hard_string = "Chicks with bricks WORD1. WORD2 with blocks come. Chicks with bricks and blocks and clocks come. Look, sir. Look, WORD3. Mr. Knox, sir. Let's do tricks with bricks and WORD4, sir."
hard_string_finished = "Chicks with bricks come. Chicks with blocks come. Chicks with bricks and blocks and clocks come. Look, sir. Look, sir. Mr. Knox, sir. Let's do tricks with bricks and blocks, sir."
hard_solutions = ["come", "Chicks", "sir", "blocks"]





def play_game_with_difficulty_setting():
    '''prompts for difficulty setting using if statement: either easy, medium, or hard. Returns the game under difficulty chosen'''
    print "welcome to my game! please select difficulty setting!"
    print "please choose difficulty level, either: easy, medium, or hard"
    difficulty = raw_input().upper()
    if difficulty == 'EASY':
        print "you have selected easy!"
        print easy_string
        return play_game_instances(easy_string, easy_solutions, parts_of_speech1, easy_string_finished)
        
    if difficulty == 'MEDIUM':
        print "you have selected MEDIUM!"
        print medium_string
        return play_game_instances(medium_string, medium_solutions, parts_of_speech1, medium_string_finished)
        
    else:
        ml_string = hard_string
        solutions = hard_solutions
        print "you have selected HARD!"
        print hard_string
        return play_game_instances(hard_string, hard_solutions, parts_of_speech1, hard_string_finished)
               
def word_in_pos(word, parts_of_speech1):
    '''checks each instance of word in string and returns the part of speach when arrived upon'''
    for item in parts_of_speech1:
        if item in word:
            return item
    return None

def replace_the_blanks(mode, solutions, parts_of_speech1):
    '''the actual game mode that plays until everything is answered correctly'''
    replaced = []
    mode = mode.split()
    i = 0
    for word in mode:
        replacement = word_in_pos(word, parts_of_speech1)
        if replacement != None:
            user_input = raw_input("Type in: " + replacement + " ")
            word = word.replace(replacement, user_input)
            while user_input != solutions[i]:
                user_input = raw_input("Sorry! Pick another word! Type in a: " + replacement + " ")
            i = i+1
            replaced.append(solutions[i - 1])
            print " ".join(replaced)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
   
    
        
  
def play_game_instances(mode, solutions, parts_of_speech1, finish):
    '''finishes the game to say correct, and print the final solutions'''
    replace_the_blanks(mode, solutions, parts_of_speech1)
    print "correct!"
    print finish
    

    
print play_game_with_difficulty_setting()




