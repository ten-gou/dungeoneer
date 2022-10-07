import json
from pprint import pprint
from rand import randKey, randChara
from verify import verify

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
    with open('character.json') as saveJSON:
        saveData = json.load(saveJSON)
        print(saveData[key]['id'])
        if key == saveData[key]['id']:
            if saveData[key]['status'] == 'alive':
                print(f"{saveData[key]['name']}, a level {saveData[key]['level']} {saveData[key]['gender']} {saveData[key]['class']}, has once again answered your call.")
            else:
                print("Unfortunately, this traveler has met their end...")
        else:
            print('Unfortunately, no one answered your call...')
else:
    print('Would you like to:')
    print('[A] search for a specific person?')
    print('[B] leave fate to be your guide?')
    newChara = verify(2)
    if newChara == 'a' or newChara == 'A':
        print('Very well, then.')
    else:
        print('May luck guide you to the character you desire')
        randChara()