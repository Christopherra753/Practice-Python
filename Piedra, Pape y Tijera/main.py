import request
import random
import winner

def run():
  computer_option = random.choice(request.options)
  user_option = request.requestOption()
  print(f"Computer option: {computer_option}")
  print(f"User option: {user_option}")
  win = winner.get_winner(computer_option,user_option)
  print(f"The winner is: {win}")

while True:
  run()
  salir = input("If you want to end the program press 'X' otherwise press 'ENTER'").lower()
  if salir=="x": break