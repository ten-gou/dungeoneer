import json
from pprint import pprint
from venv import create
from rand import randChara, selectChara
from verify import verify
from charUpdate import characterCheck, createCharacter, levelUp

#randKey() creates a random key for new characters
#verify() is a multiple choice input verification for a proper input

print('Welcome to the Dungeoneers Gambit!')
print('Now then, do you wish to:')
print('[A] Continue your journey with a previous bond?')
print('[B] Forge a bond with a new traveler?')
start = verify(2)

if start == 'a' or start == 'A':
    print('Call upon the key that binds you to your traveler:')
    key = input()
    char = characterCheck(key)
else:
    print('Would you like to:')
    print('[A] search for a specific person?')
    print('[B] leave fate to be your guide?')
    newChara = verify(2)
    if newChara == 'a' or newChara == 'A':
        print('Very well, then.')
        key = selectChara()
        createCharacter(key)
        char = characterCheck(key['id'])
    else:
        print('May luck guide you to the character you desire')
        key = randChara()
        createCharacter(key)
        char = characterCheck(key['id'])

print("would you like to level up?\n[A] yes\n[B] no")
newlevel = verify(2)

if newlevel == 'a' or newlevel == 'A':
    print("level up!")
    levelUp(char)
else:
    print("no level up")