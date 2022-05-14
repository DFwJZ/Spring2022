

def word():
    f = open('a.txt', 'r')
    words = [word for word in f.read().split() if len(word) <= 3 and word[1] == 'm']
    print(len(words))

    f2 = open('b.txt', 'w')
    for i in range(len(words)):
        f2.write(words[i] + '\n')
    f.close()
    f2.close()

    print(str(words))


word()


