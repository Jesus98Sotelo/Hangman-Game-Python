import random
from os import system
import hanged as h
hh = h.HANGMAN_IMAGES

def play(word , underscord):
  wordList = list(word)
  underscordList = list(underscord)
  lyric = ''

  while wordList != underscordList or lyric == '  ':
    lyric = input('Tu primer intento : ')


    for i in range(0, len(wordList)):
      if wordList[i] == lyric:
        underscordList[i] = wordList[i]
      else:
        system('clear')
    print(' '.join(underscordList).upper())

  print('Ganaste!!!')

def normalize(s):
  replacements = (
    ("á", "a"),
    ("é", "e"),
    ("í", "i"),
    ("ó", "o"),
    ("ú", "u"),
  )
  for a, b in replacements:
    s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def read():
  with open('./docs/data.txt', 'r', encoding='utf-8') as f:
    words = [i.replace('\n', '') for i in f]
    random_word = random.randint(0, len(words))
    word = words[random_word]

  return word

def run():

  print("""
  ____    _                                         _       _                                      
  |  _ \  (_)                                       (_)     | |                                     
  | |_) |  _    ___   _ __   __   __   ___   _ __    _    __| |   ___       __ _                    
  |  _ <  | |  / _ \ | '_ \  \ \ / /  / _ \ | '_ \  | |  / _` |  / _ \     / _` |                   
  | |_) | | | |  __/ | | | |  \ V /  |  __/ | | | | | | | (_| | | (_) |   | (_| |                   
  |____/  |_|  \___| |_| |_|   \_/    \___| |_| |_| |_|  \__,_|  \___/     \__,_|                   
                                                                                                  
  _    _                                                     
  | |  | |                                                    
  | |__| |   __ _   _ __     __ _   _ __ ___     __ _   _ __  
  |  __  |  / _` | | '_ \   / _` | | '_ ` _ \   / _` | | '_ \ 
  | |  | | | (_| | | | | | | (_| | | | | | | | | (_| | | | | |
  |_|  |_|  \__,_| |_| |_|  \__, | |_| |_| |_|  \__,_| |_| |_|
                            __/  |                            
                            |___/                             
  
  No te ahorques y adivina la parabra antes,solo contaras con 6 oportunidades.

  Instrucciones:
  1.- Solo puedes teclear una letra.
  2.- Ganas si adivinas la palabra
  3.- Pierdes si completas el ahorcado (Cuentas con 6 intestentos)

  
   _____    ____    __  __   ______   _   _   ______  ______   __  __    ____     _____ 
  / ____|  / __ \  |  \/  | |  ____| | \ | | |___  / |  ____| |  \/  |  / __ \   / ____|
  | |     | |  | | | \  / | | |__    |  \| |    / /  | |__    | \  / | | |  | | | (___  
  | |     | |  | | | |\/| | |  __|   | . ` |   / /   |  __|   | |\/| | | |  | |  \___ \ 
  | |____ | |__| | | |  | | | |____  | |\  |  / /__  | |____  | |  | | | |__| |  ____) |
  \_____|  \____/  |_|  |_| |______| |_| \_| /_____| |______| |_|  |_|  \____/  |_____/ 
  """)
  print(hh[0])
  word = read()
  wordNormalize = normalize(word)
  underscord = '_' * (len(word))
  print(' '.join(underscord))
  

  play(word, underscord)

if __name__ == '__main__':
  run()