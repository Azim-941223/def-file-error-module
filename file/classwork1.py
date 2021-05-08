# 1
f = open('directories.txt', 'w')
f.write(f'a/' 'hi/' 'snap/''Загрузки/' 'Общедоступные/'
 'Desktop/' 'python/' 'Видео/' 'Изображения/' "'Рабочий стол'/"
 'dream/' 'repaTest/' 'Документы/' 'Музыка/' 'Шаблоны/')
f.close()

with open('directories.txt', 'r') as f:
    print(f.read())