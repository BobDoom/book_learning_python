import json

filename = 'files/json_files/numbers.json'
numbers = [3, 5, 7, 11, 13]

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


filename = 'files/json_files/numbers.json'

with open(filename) as f_obj:
    numbers_1 = json.load(f_obj)
print (numbers_1)