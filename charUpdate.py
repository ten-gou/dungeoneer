import json
from verify import numConvert, verify
import random
import math

def createCharacter(data):
    with open('character.json') as character:
        characterData = json.load(character)
        characterData.append(data)

    file = open('character.json', 'w')
    json.dump(characterData, file)
    file.close()

def characterCheck(input):
    with open('character.json') as saveJSON:
        saveData = json.load(saveJSON)
        i = 0
        for save in saveData:
            if input == save['id'] or input == save['name']:
                if save['status'] == 'alive':
                    print(f"{save['name']}, a level {save['level']} {save['gender']} {save['class']}, has answered your call.")
                    return save
                else:
                    print(f"Unfortunately, {save['name']} is not longer alive...")
                    break
            elif i == len(saveData):
                print('Unfortunately, no one answered your call...')
                break
            i+=1

def updateCharacter(data):
    oldSave = characterCheck(data['name'])
    print(oldSave)
    print(data)

def levelUp(save):
    save['level'] += 1
    save['hp'] = save['hp'] + save['hpscale'] + math.ceil((save['con']-10)/2)
    save['str'] += random.randint(0 , 1)
    save['con'] += random.randint(0 , 1)
    save['dex'] += random.randint(0 , 1)
    save['int'] += random.randint(0 , 1)
    save['wis'] += random.randint(0 , 1)
    save['cha'] += random.randint(0 , 1)
    
    print("Which stat would you like to focus on?")
    print("[A] Strength\n[B] Constitution\n[C] Dexterity\n[D] Intelligence\n[E] Wisdom\n[F] Charisma")
    choice = verify(6)

    match choice:
        case 'a':
            save['str'] += random.randint(1, 5)
        case 'b':
            save['con'] += random.randint(1, 5)
        case 'c':
            save['dex'] += random.randint(1, 5)
        case 'd':
            save['int'] += random.randint(1, 5)
        case 'e':
            save['wis'] += random.randint(1, 5)
        case 'f':
            save['cha'] += random.randint(1, 5)

    print(save)
    updateCharacter(save)

