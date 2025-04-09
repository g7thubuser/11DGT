print("Welcome to Leo's Geometry dash quiz")
name = input("What is your name? \n< ") # Getting the user's name.
print("Nice to meet you"+ name + "!")
# These are lists of every question along with every possible 
gdq = ["#1 When was geometry dash released?", 
             "#2 Which gamemode has the most potential for difficulty",
             "#3 Which level is currently placed at 7 on the demon list?",
             "#4 After the physics revamp, the physics on every frame rate now match the physics previously seen on which frame rate?",
             "#5 Which creator published the most popular medium demon in geometry dash?",
             "#6 Which level was the first to be rated legendary?", 
             "#7 Which of these list demons sat at #1 on the list for the majority of 2019?"]
possibleanswers = ["1: 2014,2: 2013, 3: 2012, 4: 2011", 
                   "1: Ball,2: Ship,3: wave, 4: Robot", 
                   "1: Spectre, 2: Acheron, 3: Tunnel of Despair, 4: Silent Clubstep",
                   "1: 60fps, :2 120fps, 3: 240fps, 4: 360fps",
                   "1: ScorchVX, 2: Bli, 3: Serponge, 4: Motleyorc",
                   "1: Coaster Mountain, 2: And Ever, 3: Rage Quit, 4: WHAT",
                   "1: Zodiac, 2: Tartarus, 3: Yatagarasu, 4: Bloodlust"]
correctanswers = [2,3,4,3,4,1,1] # This list shows what the correct answer is for each question.
questionnumber = 0 # This variable tracks which question the user is up to.
#Setup over, time to start the quiz
print("Welcome to this geometry dash quiz " + name + ", I've made it very hard so it might feel like you're in a slaughterhouse or being hit by a tidal wave.")
input = (gdq[questionnumber],"\n<")