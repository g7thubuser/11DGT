questions = ["When was geometry dash released?\n A: 2014\n B: 2013\n C: 2012\n D: 2011",
             "Which gamemode has the most potential for difficulty?\n A: Ball\n B: Ship\n C: Wave\n D: Robot",
             "Which level is currently placed at 7 on the demonlist?\n A: Spectre\n B: Acheron\n C: Silent Clubstep \n D: Avernus",
             "Geometry dash runs at how many physics ticks per second?\n A: 60\n B: 120\n C: 240\n D: 360",
             "Which creator published the most popular medium demon in geometry dash?\n A: Motleyorc\n B: Xendergame\n C: Serponge\n D: Voxicat",
             "Which level was the first to be rated legendary?\n A: Coaster mountain\n B: And ever\n C: What?\n D: White space", 
             "Which of these list demons sat at #1 on the list for the majority of 2019?\n A: Sonic wave\n B: The golden\n C: Zodiac\n D: Yatagarasu",
             "Which of these list demons is currently at #1 on the list? \n A: Slaughterhouse\n B: Tidal wave\n C: Boobawamba\n D: Amethyst"]
answers = ["b","c","d","c","a","a","c","b"]  # This is a list of every question and the possible answers
question_number = 0 # This variable tracks which question the player is up to.
score = 0 # This variable tracks the player's score
MINAGE = 15
MAXAGE = 18
age = input("How old are you?\n< ")
while age.isnumeric() == False:
    age = input(" INVALID INPUT\nEnter an integer\nHow old are you?\n< ") # Getting the user's age
if int(age) < MINAGE or int(age) > MAXAGE:   # Checks if the user inputed a number
    print("Only people of ages "+ str(MINAGE) +"—"+ str(MAXAGE) +" can play.")
    exit()
else: 
    print("You're the correct age for this quiz.")

name = input("What is your name? \n< ") # Getting the user's name.

# Main Quiz loop
for i in range (0,len(questions)):
    attempts = 0 #  Resets the attempts when a new question starts
    while attempts < 2:
        user_response = input("\n\nQuestion "+ str(question_number+1) +"\n\nAttempt "+ str(attempts+1) +"\n\nScore "+ str(score) +"\n\n"+ questions[question_number] +"\n< ")
        if user_response.lower() == answers[question_number]:
            print("Correct")
            question_number += 1 # Advance to the next question
            score += (15 / (attempts+1))         # Add to the score
            attempts = 0         # Reset attempts
        elif user_response.lower() in ("a","b","c","d"):
            print("Wrong")
            attempts += 1
        else:
            print("\nInvalid response. Please enter one of the following\n A,B,C,D\n")
    print("Wow "+ name +"! I'm so disapointed in you " + name +".\n The correct answer was " +answers[question_number]+ "\nYou better do a better job with this next question.") # Scold the user
    question_number += 1        # Advance to the next question if the user gets it wrong too many times
if score == 120:
    print("Wow "+ name +" ! \n A perfect score!\nYou're truly a first rate dasher.\n")
elif score >= 70:
    print("Wow "+ score +" Not too bad"+ name +".\n You're getting pretty good.\n")
else:
    print(+ score +" Wow...\nJust... wow.\nYou managed to fumble your way through my Geometry Dash quiz and still flop harder than Geometry Dash World's update schedule.\n\
Were you even trying? Or were you just mashing random keys like a Wave player with lag?\n\
This quiz was meant to be a two star, but somehow you made it look like Silent Circles.\n\
You had *three* chances per question and still couldn't break 40 points?\n\
Even RobTop is shaking his head right now.\n\
You might want to go back to Stereo Madness and rethink your life choices.\n\
You're not a geometry dasher, you're a geometry crasher'.\n\
Next time, try reading the questions instead of speedrunning failure.\n\
Now go hit the practice mode... you need it.\n")
exit()
