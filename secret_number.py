secret = int(3)

guess = int(input("Guess the secret number: "))

if guess == secret:
    print("Congratulations, your answer is correct!")
else:
    print("I'm sorry, you are wrong.")