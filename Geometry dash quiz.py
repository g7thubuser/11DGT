questions = ["When was geometry dash released?\n A: 2014\n B: 2013\n C: 2012\n D: 2011",
             "Which gamemode has the most potential for difficulty?\n A: Ball\n B: Ship\n C: Wave\n D: Robot",
             "Which level is currently placed at 7 on the demonlist\n A: Spectre\n B: Acheron\n C: Silent Clubstep \n D: Tunnel of dispair",
             " Geometry dash runs at how many physics ticks per second?",
             "Which creator published the most popular medium demon in geometry dash?",
             "Which level was the first to be rated legendary?", 
             "Which of these list demons sat at #1 on the list for the majority of 2019?"]
# This is a list of every question and the possible answers
answers = ["b","c","d","c","d","a","a"]  # This list shows what the correct answer is for each question.
question_number = 0 # This variable tracks which question the user is up to.
name = input("What is your name? \n< ") # Getting the user's name.
print("Welcome to Leo's geometry dash quiz " + name + ". It's quite a hard quiz so you might feel like you're being hit by a Tidal Wave, being sucked into \nAndromeda or falling into an Abyss Of Darkness.\n\
Good luck " + name + "!\nLet the quiz begin!")
while question_number < len(questions):
    attempts = 0 # Resets the attempts when a new question starts
    while attempts < 3:
        user_response = input("Question #"+ str(question_number+1) +"\n"+ questions[question_number] +"\n Attempt "+ str(attempts+1) +"\n< ")
        if user_response.lower() == answers[question_number]:
            print("Correct")
            question_number += 1
            attempts = 0
        elif user_response.lower() == ("a","b","c","d"):
            print("Wrong")
            attempts += 1
        else:
            print("Invalid answer")