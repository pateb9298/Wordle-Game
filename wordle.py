from colorama import Fore
import random
guess = input("Enter a 5 Letter Word: ")

words_list = ["ggggy", "doggy", "ggggg", "ggggg"]
secret_word = random.choice(words_list)	
      
num_of_guesses = 0
while num_of_guesses < 4:
  for i in words_list:
    if secret_word == guess:
      print("Your guess is correct")
      break
    elif i != guess:
      a=list(set(guess)&set(secret_word))
      print(Fore.YELLOW + "The common letters are:" + Fore.RESET)
      for i in a:
        f=i
        print(Fore.YELLOW + f + Fore.RESET)
        if guess.index(f) == secret_word.index(f):
          print(f, "Green")
        else:
          pass
      print(guess)
      guess = input("Please enter your guess: ")
    num_of_guesses +=1
  break

