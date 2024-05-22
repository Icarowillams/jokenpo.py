def jogarJokenpo():
  jogador1 = input("Jogador 1, escolha entre pedra, papel ou tesoura: ")
  jogador2 = input("Jogador 2, escolha entre pedra, papel ou tesoura: ")

  if jogador1 == jogador2:
      print("Empate!")
  elif jogador1 == "pedra":
      if jogador2 == "tesoura":
          print("Jogador 1 ganha!")
      else:
          print("Jogador 2 ganha!")
  elif jogador1 == "papel":
      if jogador2 == "pedra":
          print("Jogador 1 ganha!")
      else:
          print("Jogador 2 ganha!")
  elif jogador1 == "tesoura":
      if jogador2 == "papel":
          print("Jogador 1 ganha!")
      else:
          print("Jogador 2 ganha!")
  else:
      print("Escolha inválida. Certifique-se de digitar 'pedra', 'papel' ou 'tesoura'.")

while True:
  jogarJokenpo()
  jogar_novamente = input("Desejam jogar novamente? (s/n): ")
  if jogar_novamente != "s":
      break