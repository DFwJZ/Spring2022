def name(a):
    a.lower()
    sum = 0
    for i in range(len(a)):
        sum += ord(a[i].lower()) - 96
    print(sum)

    
def main():
    name('Jump')
    
if __name__ == '__main__':
    main()
