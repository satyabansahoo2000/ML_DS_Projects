# -*- coding: utf-8 -*-
"""Number Guessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ROMRdElT1WIWEXFzusOUpNka3-J_j6op
"""

import random

num = random.randint(1,100)
hint_score = 100

def hint(num, hint_score):
  hint_needed = (input("Do you need a hint ?? "))
  if hint_needed == 'Y' or hint_needed == 'y':
    hint_score -= 10
    if num%2==0:
      print("Number is divisible by 2.")
    else:
      print("Number is not divisible by 2.")
    return hint_score
  elif hint_needed == 'N' or hint_needed == 'n':
    print("Hint is not needed.")
    return hint_score

print("WELCOME TO THE GUESSING GAME !!!\n")
print("----------------------------------")
print("Your Score is 0 and Hint Points is deafult set to 100 and it will reduce if you take any hints by 10 points.\n\n")
while(hint_score > 0):
  user = int(input("Enter number : "))
  if user > num:
    print("Nope ! You guessed it wrong!!! Please enter a lesser value.")
    hint_score = hint(num, hint_score)
    print("Your hint score is ",hint_score)
  elif user < num:
    print("Nope ! You guessed it wrong!!! Please enter a larger value.")
    hint_score = hint(num, hint_score)
    print("Your hint score is ",hint_score)
  elif user == num:
    print("Voila!!! You guessed it right. The number is {}.".format(num))
    break