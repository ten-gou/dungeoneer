import json

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
                    print(f"{save['name']}, a level {save['level']} {save['gender']} {save['class']}, has once again answered your call.")
                    return save
                else:
                    print(f"Unfortunately, {save['name']} is not longer alive...")
                    break
            elif i == len(save):
                print('Unfortunately, no one answered your call...')
                break
            i+=1