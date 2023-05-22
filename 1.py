song = str(input("Введите песню: "))
sng = song.lower()
print (song)

def ritm(str):
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    splitsong = str.split(" ")
    print(splitsong)
    lst = list()
    for i in splitsong:
        count = 0
        for j in i:
            if j in vowels:
                count += 1
        lst.append(count)
    print(set(lst))
    if len(set(lst)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'
    
print (ritm(song))


