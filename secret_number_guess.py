secret_number = 7
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
   Guess = int(input('Guess: '))
   guess_count += 1
   if Guess == secret_number:
      print('^-^ YOU WIN O.o')
      break
else:
    print('YOU\'VE FAILED :(')
