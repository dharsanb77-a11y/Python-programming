import random
num=random.randint(1,100)
attempt=0
while True:
    guess=int(input("Guess the Number between 1 and 100: "))
    attempt=attempt+1
    if(guess==num):
        print("Success!You've guessed correct number")
        print("Attempt: ",attempt)
        break
    else:
        n=lambda num:"Number is Even" if num%2==0 else "Number is Odd"
        v=lambda guess,num:f"Number higher than {guess}" if num>guess else f"Number is less than {guess}"
        print("Try Again! Clue: ",n(num),"and ",v(guess,num))
