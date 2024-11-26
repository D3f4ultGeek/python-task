import random
words=["apple","banana","cat","dog"]
chosenword=random.choice(words)
shuffled =list(chosenword)
random.shuffle(shuffled)
shuffled=''.join(shuffled)
print(f"shuffled word is : {shuffled}")
attempts=5
while attempts>0:
    attempts-=1
    guess=input("Enter your guess :")
    if guess == chosenword:
        print(f"congratulations! the word is right")
        exit()
    else:
        print(f"You are wrong ,you have {attempts} remaining attempts")
        
print(f"you are out of attempts. the correct word is {chosenword}")