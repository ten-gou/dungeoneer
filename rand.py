from random import randint, random
import json
import pprint
import random
import names

#generate randkey for character
def randKey():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    string = ""
    number = 0
    while number < 16:
        string += alphabet[random.randint(0,25)]
        number += 1
        if number == 4 or number == 8 or number == 12:
            string += "-"
    return string

def randChara():
    #male or female and random name
    mf = random.randint(0,1)
    if mf == 1:
        for i in range(1):
            rand_name = names.get_full_name(gender='male')
            gender = 'male'
    else:
        for i in range(1):
            rand_name = names.get_full_name(gender='female')
            gender = 'female'

    #class
    with open('classData.json') as classJSON:
        classData = json.load(classJSON)
        selectClass = classData['class'][random.randint(0,5)]

    charData = {
        'id': randKey(),
        'name': rand_name,
        'status': 'alive',
        'gender': gender,
        'level': 1,
        'exp': 0,
        'class': selectClass['className'],
        'hp': selectClass['hp'],
        'hpscale': selectClass['hpscale'],
        'str': selectClass['str'],
        'con': selectClass['con'],
        'dex': selectClass['dex'],
        'int': selectClass['int'],
        'wis': selectClass['wis'],
        'cha': selectClass['cha']
    }
    
    return charData
