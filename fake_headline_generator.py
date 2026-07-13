#import random module
import random

subjects = ["Scientists", "Politicians", "Celebrities", "Aliens", "Robots"]
actions = ["discover", "invent", "steal", "destroy", "save"]
objects = ["a new planet", "a cure for a disease", "a secret formula", "a hidden treasure", "a powerful weapon"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    
    headline = f"{subject} {action} {obj}!"
    print(headline)
    
    cont = input("Generate another headline? (y/n): ").lower()
    if cont != 'y':
        print("Goodbye!")
        break

    