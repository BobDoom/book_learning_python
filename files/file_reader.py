# file_path = '/home/bobdoom/CODE/book_learning_python/files/text_files/pi_digits.txt' 
# with open(file_path) as file_object:
#     #contents = file_object.read()
#     #print (contents)
#     lines = file_object.readlines()
#     lines_bez_n = [i.rstrip() for i in lines]  # Обрезь переносов строки (\n)
#     for line in lines:    
#         print (line)
#     print(lines)
#     print(lines_bez_n)

#     pi_string = ''
#     for line in lines:
#         pi_string += line.strip()  # Без энтеров, пробелов и пропусков
#     print(pi_string, type(pi_string))
#     pi_float = float(pi_string)
#     print (pi_float, type(pi_float))
#     print ('Пользователь GIT')


# filename = 'files/text_files/pi_million_digits.txt'
# with open(filename) as file_mill:
#     lines_mill = file_mill.readlines()

#     pi_string_mill = ''
#     for line in lines_mill:
#         pi_string_mill += line.strip()
      
# birthday = input("Введите дату рождения (mmddyy): ")
# if birthday in pi_string_mill:
#     print ("Дата вашего рождения встречается среди первого миллиона знаков Пи после запятой!") 
# else:
#     print ("Даты вашего рождения нет среди первого миллиона знаков Пи.")       


filename_in = 'files/text_files/in_python.txt'
with open(filename_in) as file_in:
    # content_in = file_in.read()
    # print (content_in*3)

    in_python_dict = file_in.readlines()
    for line in in_python_dict:
        print(line)
    print (in_python_dict)

    for line in in_python_dict:
        print (line.replace('Python', "C"))