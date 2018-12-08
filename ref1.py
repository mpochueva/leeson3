with open('referat.txt', 'r', encoding='utf-8') as f, open('referat2.txt', 'w', encoding='utf-8') as k:
    content = f.read()

    check_array = ['\n', ' ']
    word_count = 0
    # Flag marks if the string element is part of the word or no. False - no, True - yes
    flag = False

    for i in content:
        if i not in check_array and flag is False:
            word_count += 1
            flag = True
        elif i in check_array:
            flag = False

    k.write(content.replace('.', '!'))
    print('Длина строки:', len(content))
    print('Количество слов:', word_count)


