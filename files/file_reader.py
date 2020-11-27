file_path = '/home/ka/CODE/book_learning_python/files/text_files/pi_digits.txt' 
with open(file_path) as file_object:
    #contents = file_object.read()
    #print (contents)
    lines = file_object.readlines()
    lines_bez_n = [i.rstrip() for i in lines]  # Обрезь переносов строки (\n)
    for line in lines:    
        print (line)
    print(lines)
    print(lines_bez_n)

    pi_string = ''
    for line in lines:
        pi_string += line.strip()  # Без энтеров, пробелов и пропусков
    print(pi_string, type(pi_string))
    pi_float = float(pi_string)
    print (pi_float, type(pi_float))
    print ('Пользователь GIT')
