file_text_dict = {}
filename_1 = '1.txt'
filename_2 = '2.txt'
filename_3 = '3.txt'
filename_4 = '4.txt'

# Считываю данные из файла
with open (filename_1, 'r') as f:
    file_text_dict[filename_1] = f.readlines()
with open (filename_2, 'r') as f:
    file_text_dict[filename_2] = f.readlines()
with open(filename_3, 'r') as f:
    file_text_dict[filename_3] = f.readlines()

# Сортирую список
sorted_dict = dict(sorted(file_text_dict.items(), key=lambda item: item[1],  reverse = True))

# Запись в файл
with open (filename_4, 'w') as f_out:
    for key, value in sorted_dict.items():
        f_out.write(key + '\n')
        f_out.write(str(len(value)) + '\n')
        f_out.write(''.join(value) + '\n')

