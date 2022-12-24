def get_winner(computer_option,user_option):
  if computer_option == "piedra":
    if user_option == "piedra": return "draw"
    if user_option == "papel": return "user"
    if user_option == "tijera": return "computer"

  if computer_option == "papel":
    if user_option == "piedra": return "computer"
    if user_option == "papel": return "draw"
    if user_option == "tijera": return "user"

  if computer_option == "tijera":
    if user_option == "piedra": return "user"
    if user_option == "papel": return "computer"
    if user_option == "tijera": return "draw"
