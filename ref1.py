with open('referat.txt', 'r', encoding='utf-8') as f, open('referat2.txt', 'w', encoding='utf-8') as k:
    content = f.read()

    # Список знаков, разделяющих слова
    check_array = ['\n', ' ']
    # Счетчик слов
    word_count = 0
    # Определяет, относится к слову элемент строки или нет. False - нет, True - да
    flag = False

    for i in content:
        # Если элемент строки не пробел или не перенос каретки и перед ним других букв не было
        if i not in check_array and flag is False:
            # Добавляем слово
            word_count += 1
            # Элемент строки относится к слову
            flag = True
        # Если элемент строки к слову не относится, меняем значение флага
        elif i in check_array:
            flag = False

    k.write(content.replace('.', '!'))
    print('Длина строки:', len(content))
    print('Количество слов:', word_count)


