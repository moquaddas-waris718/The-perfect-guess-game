import random

n = random.randint(1, 100)
a = -1
guesses = 0

while(a!=n):
    guesses +=1
    a = int(input("Guess a Number : "))
    if(a>n):
        print("Lower number please...")
    elif(a<n):
        print("Higher number please...")
        

print(f"\nCongratultions you have guessed the correct number in {guesses} attempts!")