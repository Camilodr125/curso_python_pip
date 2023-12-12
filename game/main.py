import random

options = ('piedra', 'papel', 'tijera')




def choose_options():
    pc = random.choice(options)
    user = input('Eliga piedra, papel o tijera:')
    user = user.lower()
    return pc, user

def check_rules(pc, user, pc_wins, user_wins):
  
  if user in options:
    if pc == user :
      print('Es un empate')
    elif user == 'piedra':
      if pc == 'tijera':
        print('Ganaste!!')
        user_wins +=1
      else:
        print('Perdiste :(')
        pc_wins +=1

    elif user == 'tijera':
      if pc == 'papel':
        print('Ganaste!!')
        user_wins +=1
      else:
        print('Perdiste :(')
        pc_wins +=1


    elif user == 'papel':
      if pc == 'piedra':
        print('Ganaste!!')
        user_wins +=1
      else:
        print('Perdiste :(')
        pc_wins +=1
        
    return pc_wins, user_wins

  else:
    print('Esa opción no es válida')

def run_game():
  user_wins = 0
  pc_wins = 0
  rounds = 0
  while user_wins <= 2 or pc_wins <= 2:
  
    
    print(f'ROUND {rounds}')
    print(f'Victorias del usuario: {user_wins}')
    print(f'Victorias del pc: {pc_wins}')
  
    rounds += 1
  
    pc, user = choose_options()
    pc_wins, user_wins = check_rules(pc,user, pc_wins, user_wins)
    print(f'El ususario escogio {user}')
    print(f'El pc escogio {pc}')
  
  
    if user_wins == 2:
      print(f'Después de {rounds} rondas, el ganador fue el usurio con {user_wins} rondas ganadas')
      break
  
    if pc_wins == 2:
      print(f'Después de {rounds} rondas, el ganador fue el pc con {pc_wins} rondas ganadas')
      break

run_game()