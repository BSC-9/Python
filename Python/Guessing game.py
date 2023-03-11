import random
n=3
number=random.randint(0,100)
while(n!=0):
    print(f"You have {n} Attempts left")
    Guess_number=int(input("Enter the number you want to guess: "))
    n=n-1
    if(Guess_number<number):
        print("Guess number is smaller than the number\n")
    elif(Guess_number>number):
        print("Guess number is greater than the number\n")
    else:
        print("Congragulations! You won")
        break
if(n==0):
    print(f"Guess number : {number}")