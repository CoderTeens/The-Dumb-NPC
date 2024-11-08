import random

things = ["me", "yes", "no", "not me", "what", "idk", "NPC", "a", "ah"]

print("\033[0;34m Welcome To The Dumb NPC")
print("")
print("\033[0;34m Ask a Question!")

def redo():
    input("\033[0;32m RANDOM: ")
    print("\033[1;33m NPC: " + random.choice(things))
    
while True:
    redo()
