import sys

d={'1':' ','2':' ','3':' ',
   '4':' ','5':' ','6':' ',
   '7':' ','8':' ','9':' '}

def printboard():
    print(d['1']+' | '+d['2']+' | '+d['3'])
    print(d['4']+' | '+d['5']+' | '+d['6'])
    print(d['7']+' | '+d['8']+' | '+d['9'])

def play():
    l=[]
    print("user1 starts with x")
    item='x'
    for i in range(15):
        print("Where do you want to place the item(1 to 9)")
        move=input()
        if move not in l:
            l.append(move)
        else:
            print("Entered place is already occupied")
            print("Enter a valid position")
            continue
        d[move]=item
        if item=='x':
            item='o'
        else:
            item='x'

        if d['1'] == 'x' and d['2'] == 'x' and d['3'] == 'x':
            print("Winner")
            sys.exit()
        elif d['1'] == 'o' and d['2'] == 'o' and d['3'] == 'o':
            print("Winner")
            sys.exit()
        elif d['4'] == 'x' and d['5'] == 'x' and d['6'] == 'x':
            print("Winner")
            sys.exit()
        elif d['4'] == 'o' and d['5'] == 'o' and d['6'] == 'o':
            print("Winner")
            sys.exit()
        elif d['7'] == 'x' and d['8'] == 'x' and d['9'] == 'x':
            print("Winner")
            sys.exit()
        elif d['7'] == 'o' and d['8'] == 'o' and d['9'] == 'o':
            print("Winner")
            sys.exit()
        elif d['1'] == 'x' and d['4'] == 'x' and d['7'] == 'x':
            print("Winner")
            sys.exit()
        elif d['1'] == 'o' and d['4'] == 'o' and d['7'] == 'o':
            print("Winner")
            sys.exit()
        elif d['2'] == 'x' and d['5'] == 'x' and d['8'] == 'x':
            print("Winner")
            sys.exit()
        elif d['2'] == 'o' and d['5'] == 'o' and d['8'] == 'o':
            print("Winner")
            sys.exit()
        elif d['3'] == 'x' and d['6'] == 'x' and d['9'] == 'x':
            print("winner")
            sys.exit()
        elif d['3'] == 'o' and d['6'] == 'o' and d['9'] == 'o':
            print("Winner")
            sys.exit()
        elif d['1'] == 'x' and d['5'] == 'x' and d['9'] == 'x':
            print("Winner")
            sys.exit()
        elif d['1'] == 'o' and d['5'] == 'o' and d['9'] == 'o':
            print("Winner")
            sys.exit()
        elif d['7'] == 'x' and d['5'] == 'x' and d['3'] == 'x':
            print("Winner")
            sys.exit()
        elif d['7'] == 'o' and d['5'] == 'o' and d['3'] == 'o':
            print("Winner")
            sys.exit()
        printboard()


printboard()
play()
