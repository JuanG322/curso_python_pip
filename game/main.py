import random


#           1
def continue_game():
  choice = str(input("\nDeseas volver a jugar (si/no) :")).lower()
  if choice == "no":
    print("Hasta luego")
    jugar = False
  elif choice == "si":
    jugar = True
  else:
    print("\nOPCION INVALIDA")
    print("SALIENDO")
    jugar = False
  return jugar


#           2
def choose_options():
  jugar = True
  options = ("piedra", "papel", "tijera")

  user_option = input("piedra, papel o tijera => ").lower()

  if user_option not in options:
    print("\nOPCION NO VALIDA")
    print("ESCOJA UNA VALIDA")
    jugar = continue_game()

  computer_option = random.choice(options)
  return jugar, user_option, computer_option


#            3
def check_rules(user_option, computer_option, user_wins, computer_wins):

  if user_option == computer_option:
    print("Empate!")

  elif user_option == "piedra":
    if computer_option == "tijera":
      print("\npiedra gana a tijera")
      print("User gano")
      user_wins += 1
    else:
      print("\npapel gana a piedra")
      print("Computer gano")
      computer_wins += 1

  elif user_option == "papel":
    if computer_option == "piedra":
      print("\npapel gana a piedra")
      print("User gano")
      user_wins += 1
    else:
      print("\ntijera gana a papel")
      print("Computer gano")
      computer_wins += 1

  elif user_option == "tijera":
    if computer_option == "papel":
      print("\ntijera gana a papel")
      print("User gano")
      user_wins += 1
    else:
      print("\npiedra gana a tijera")
      print("Computer gano")
      computer_wins += 1
  return user_wins, computer_wins, computer_wins, user_wins


def run_game():
  computer_wins = 0
  user_wins = 0
  jugar = True
  round = 1

  while jugar:
    print("\n")
    print("*" * 10)
    print("ROUND ", round)
    print("*" * 10)

    jugar, user_option, computer_option = choose_options()
    if jugar == False:
      break
    round += 1

    user_wins, computer_wins, computer_wins, user_wins = check_rules(
        user_option, computer_option, computer_wins, user_wins)

    print("\nOpciones escojidas")
    print("User => ", user_option)
    print("Computer => ", computer_option)
    print("\nUser wins => ", user_wins)
    print("Computer wins => ", computer_wins)

    jugar = continue_game()


run_game()