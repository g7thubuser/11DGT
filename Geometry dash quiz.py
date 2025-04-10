print("Welcome to Leo's Geometry dash quiz")
name = input("What is your name? \n< ") # Getting the user's name.
print("Nice to meet you"+ name + "!")
# These are lists of every question along with every possible 
gdq = ["When was geometry dash released?", 
             "Which gamemode has the most potential for difficulty",
             "Which level is currently placed at 7 on the demon list?",
             "After the physics revamp, the physics on every frame rate now match the physics previously seen on which frame rate?",
             "Which creator published the most popular medium demon in geometry dash?",
             "Which level was the first to be rated legendary?", 
             "Which of these list demons sat at #1 on the list for the majority of 2019?"]
possibleanswers = ["A: 2014,B: 2013, C: 2012, D: 2011", 
                   "A: Ball,B: Ship, C: wave, D: Robot", 
                   "A: Spectre, B: Acheron, C: Tunnel of Despair, D: Silent Clubstep",
                   "A: 60fps, :B 120fps, C: 240fps, D: 360fps",
                   "A: ScorchVX, B: Bli, C: Serponge, D: Motleyorc",
                   "A: Coaster Mountain, C: And Ever, D: Rage Quit, 4: WHAT",]
correctanswers = [2,3,4,3,4,1,1] # This list shows what the correct answer is for each question.
questionnumber = 0 # This variable tracks which question the user is up to.
#Setup over, time to start the quiz
print("Welcome to this geometry dash quiz " + name + ". I've made it very hard so it might feel like you're in a slaughterhouse or being hit by a tidal wave.\n\
Good luck" + name + "!\n\
    let the quiz begin!")
response = input("Question #"+ str(questionnumber+1) +"\n"+ gdq[questionnumber])