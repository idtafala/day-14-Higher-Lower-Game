from art import logo
from art import vs
from game_data import data
import random

max = len(data)
score = 0

type = ""
print(logo)

game =True 

while game == True :
  A = random.randint(0,max)
  B = A
  while B== A :
    B = random.randint(0,max)
  print("=======================================================================================================")
  print(f"Compare A : {data[A]['name']} , a {data[A]['description']} , from {data[A]['country']}")
  print(vs)
  print(f"Against : {data[B]['name']} , a {data[B]['description']} , from {data[B]['country']}")
  answer =""
  while not ( answer == 'A' or answer == 'B') :
    answer = input("Who has more followers ? type A or B")
    if answer == 'A' :
      int_answer = data[A]['follower_count']
    else :
      int_answer = data[B]['follower_count']
  
  if data[A]['follower_count'] > data[B]['follower_count'] :
    right_answer = data[A]['follower_count']
  else :
    right_answer = data[B]['follower_count']
  
  if right_answer == int_answer : 
    score +=1
  else :
    print("You lost !")
    print(f"your score : {score}")
    game =False


  

  


