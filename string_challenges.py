# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв а в слове
word = 'Архангельск'
# ???
count_a = 0
for i in word:
    if i == 'а' or i == 'А':
        count_a += 1
print(count_a)


# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
count_vowel = 0
for i in word:
    if i.lower() in 'ауоыиэяюёе':
        count_vowel += 1
print(count_vowel)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
s = 0
while 0 <= s < len(sentence.split()):
    print(sentence.split()[s][0])
    s += 1

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???
d = 0
while 0 <= d < len(sentence.split()):
    d += len(sentence.split()[d])
print(len(sentence.split()))

