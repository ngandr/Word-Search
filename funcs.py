def get_rows(letters):
    rows = []
    row = i = 0
    while row < 10:
        rows.append(letters[i:i+10])
        i += 10
        row += 1
    return rows

def get_columns(letters):
    rows = []
    tempColumns = []
    columns = []
    row = i = j = 0
    while row < 10:
        rows.append(letters[i:i+10])
        i += 10
        row += 1
    for i in range(10):
       for row in rows:
           tempColumns.append(row[j])
       j += 1
    for i in range(0,100,10):
        columns.append(tempColumns[i:i+10])
    return [''.join(column) for column in columns]
    
def check_forward(rows, word): #rows = get_rows(letters)
    for row in rows:
        if row.find(word) >= 0:
            return (row.find(word),'FORWARD') 
    return False
        
def check_backward(rows, word):
    backwardList = []
    for string in rows:
        backwardList.append(string[::-1])
    for row in backwardList:
        if row.find(word) >= 0:
            return (row.find(word),'BACKWARD')
    return False

def check_downward(columns, word):
    for column in columns:
        if column.find(word) >= 0:
            return (column.find(word), 'DOWN')
    return False
    
def check_upward(columns, word):
    upwardList = []
    for string in columns:
        upwardList.append(string[::-1])
    for col in upwardList:
        if col.find(word) >= 0:
            return (col.find(word), 'UP')
    return False

def check_diagonal(rows, word): #follow notes on pseudocode
    i = r = c = 0
    while c + i < 10:
        if word[i] == rows[r+i][c+i]:
            i += 1
            if i == len(word): #print row number if index matches word
                return (r, c, 'DIAGONAL')
        else:
            r += 1
            i = 0 #reset everything
        if r + i >= 10: #during reset, move a column, reset rows when rows = 9
            c += 1
            i = r = 0
    return False
