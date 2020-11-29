# filename = 'files/text_files/shaverma.txt'

# with open(filename, 'a') as file_object:
#     file_object.write("I love shaverma!\n")

filename_guest = 'files/text_files/guest_book.txt'

with open (filename_guest, 'r') as file_id_count:
    lines_id = file_id_count.readlines()
    counter_id = len(lines_id)

polling_active = True
guest_book = []
guest_id = counter_id
while polling_active:
    with open(filename_guest, 'a') as file_guest:
        guest = input("Представтесь, пожалуйста: ")
        guest_id += 1
        print (f'Здравствуйте, {guest}!')
        file_guest.write(f'{str(guest_id)} Здравствуйте, {guest}!\n')
    guest_book.append(guest) 
    repeat = input("Есть ли ещё гости? (Y/N): ").lower()
    if repeat == 'n':
        polling_active = False
print(guest_book)