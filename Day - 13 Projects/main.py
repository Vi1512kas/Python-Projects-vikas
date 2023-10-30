import art
import game_data
import random
from replit import clear
def fun():
  p = random.choice(game_data.data)
  return f"Compare A:{p['name']}, a {p['description']}, from {p['country']}." ,p
print(art.logo)
score = 0
game_on = True
while game_on:
  par_1,d = fun()
  print(par_1)
  print(art.vs)
  par_2,e = fun()
  print(par_2)
  choice = input("Which has more followers? Type 'A' or 'B':")
  clear()
  if choice == 'A':
    if d['follower_count'] > e['follower_count']:
      score += 1
      print(f"You're right! Current score: {score}.")
      clear()
    else:
      game_on = False
      print(f"Sorry, that's wrong. Your final score {score}")
  else:
    if d['follower_count'] < e['follower_count']:
      score+=1
      print(f"You're right! Current score: {score}.")
      clear()
    else:
      game_on = False
      print(f"Sorry, that's wrong. Your final score {score}")