import random
from os import system

print('*' * 46)
print('Bienvenido a piedra 🤘🏼, papel 🧻 o tijera ✂')
print('*' * 46)

def choose_options(): 
  options = ('piedra', 'papel', 'tijera')
  user_option = input('Piedra, papel o tijera => ').lower()
  if not user_option in options: 
    print('Ingrese una opción válida')
    return None, None
  computer_option = random.choice(options)
  
  print('User option =>', user_option.capitalize())
  print('Computer option =>', computer_option.capitalize())
  
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Ganaste')
      user_wins += 1
    else:
      print('Perdiste')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Ganaste')
      user_wins += 1
    else:
      print('Perdiste')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Ganaste')
      user_wins += 1
    else:
      print('Perdiste')
      computer_wins += 1
  return user_wins, computer_wins
      

def run_game():
  computer_wins = 0
  user_wins = 0
  round = 1
  while True:
    print(f"--- Round {round} ---")
    if computer_wins != 0 or user_wins != 0: 
      print('Score actual:')
      print('Usuario {} - {} Computadora'.format(user_wins, computer_wins))
    user_option, computer_option = choose_options()
    system("clear")
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    round +=1
    

run_game()