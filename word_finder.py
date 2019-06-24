from funcs import *

def main():
    letters = input()
    words = input().split()
    rows = get_rows(letters) #rows is basically the puzzle
    columns = get_columns(letters)
    backwards = ''.join([row[::-1] for row in rows])
    upwards = ''.join([column[::-1] for column in columns])
    print('Puzzle: ')
    print()
    for row in rows:
        print(row)
    print()
    #diagonal = check_diagonal(rows, columns, word)
    for word in words:
        forward = check_forward(rows, word)
        backward = check_backward(rows, word)
        downward = check_downward(columns, word)
        upward = check_upward(columns, word)
        diagonal = check_diagonal(rows, word)
        if check_forward(rows, word) != False:
            print('%s: (%s) row: %s column: %s ' % (word,forward[1],letters.find(word)//10,forward[0]))
        elif check_backward(rows, word) != False:
            print('%s: (%s) row: %s column: %s ' % (word,backward[1],backwards.find(word)//10,9-backward[0]))
        elif check_downward(columns, word) != False:
            print('%s: (%s) row: %s column: %s ' % (word,downward[1],downward[0],''.join(columns).find(word)//10))
        elif check_upward(columns, word) != False:
            print('%s: (%s) row: %s column: %s' % (word,upward[1],9-upward[0],upwards.find(word)//10))
        elif check_diagonal(rows, word) != False:
            print('%s: (%s) row: %s column: %s' % (word,diagonal[2],diagonal[0],diagonal[1]))
        else:
            print('%s: word not found' % (word))

if __name__ == '__main__':
    main()
