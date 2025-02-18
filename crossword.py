import random,pandas as pd
df=pd.read_excel('GK_Questions_and_Answers.xlsx')
grid=[['.' for i in range(12)] for i in range(12)]
direction=['up','down','left','right']
d={}
def greedyplace(word,clue,flag):
    word = word.upper()  # Ensure the word is in uppercase
    highscore = 0
    best_direction = None
    r = c = 0  
    for i in range(12):
        for j in range(12):
            for direction in ['up', 'down', 'left', 'right']:
                if can_be_placed(word, direction, i, j):
                    flag=0
                    score = 0
                    for k in range(len(word)):
                        if direction == 'right' and grid[i][j + k] == word[k]:
                            score += 1
                        elif direction == 'left' and grid[i][j - k] == word[k]:
                            score += 1
                        elif direction == 'down' and grid[i + k][j] == word[k]:
                            score += 1
                        elif direction == 'up' and grid[i - k][j] == word[k]:
                            score += 1
                    if score > highscore:
                        highscore = score
                        best_direction = direction
                        r, c = i, j
    if highscore > 0 and best_direction:
        place_word(word,clue, best_direction, r, c)
        return highscore,flag  
    return 0,flag       
def display(grid):
    print(pd.DataFrame(grid))
def can_be_placed(word,direction,row,col):
    if direction=='up':
        if len(word)>row+1:
            return False
        for i in range(len(word)):
            if grid[row-i][col]!='.' and grid[row-i][col]!=word[i]:
                return False
    if direction=='down':
        if len(word)>12-row:
            return False
        for i in range(len(word)):
            if grid[row+i][col]!='.' and grid[row+i][col]!=word[i]:
                return False
    if direction=='left':
        if len(word)>col+1:
            return False
        for i in range(len(word)):
            if grid[row][col-i]!='.' and grid[row][col-i]!=word[i]:
                return False
    if direction=='right':
        if len(word)>12-col:
            return False
        for i in range(len(word)):
            if grid[row][col+i]!='.' and grid[row][col+i]!=word[i]:
                return False
    return True
def main_working(word,clue):
    flag=1
    highscore,flag=greedyplace(word,clue,flag)
    if highscore==0 and flag==1:
        print('Cannot place the word')
    elif highscore==0 and flag==0:
        dir=random.choice(direction)
        row=random.randint(0,11)
        col=random.randint(0,11)
        while(can_be_placed(word,dir,row,col)==False):
            dir=random.choice(direction)
            row=random.randint(0,11)
            col=random.randint(0,11)
        place_word(word,clue,dir,row,col)
def place_word(word,clue,direction,row,col):
    word=word.upper()
    d[word]=[direction,clue,row,col]
    if direction=='up':
        for i in range(len(word)):
           grid[row-i][col]=word[i]    
    if direction=='down':
        for i in range(len(word)):
            grid[row+i][col]=word[i]
    if direction=='right':
        for i in range(len(word)):
            grid[row][col+i]=word[i]
    if direction=='left':
        for i in range(len(word)):
            grid[row][col-i]=word[i]
flag=1
print('1.Generate custom Crossword')
print('2.Generate automatic Crossword')
ch=int(input('Enter your choice'))
if ch==2:
    taken=[]
    while(len(taken)<=8):
        num=random.randint(0,len(df)-1)
        if num not in taken:
            taken.append(num)
    for i in taken:
        word=df.loc[i].Answer
        clue=df.loc[i].Question
        main_working(word,clue)
elif ch==1:
    while(True):
        flag=1
        word=input('Enter your word(enter -1 to stop)')
        if word=='-1':
            break
        while(len(word)>12):
            word=input('TOO LONG.Enter your word again')
        clue=input("Enter clue for this word.")
        main_working(word,clue)
display(grid)
print()
answergrid=[['.' for i in range(12)] for i in range(12)]
for i in range(12):
    for j in range(12):
        if grid[i][j]!='.':
            flag=0
            for x in d:
                if i==d[x][2] and j==d[x][3]:
                    flag=1
                    break
            if flag==1:
                answergrid[i][j]=grid[i][j]
            else:
                answergrid[i][j]='_'
        else:
            answergrid[i][j]='#'
display(answergrid)
for i in d:
    print([d[i][2],d[i][3]], d[i][0], ':', d[i][1])
with open('crossword_output.txt', 'w') as f:
    for row in grid:
        f.write('    '.join(row) + '\n')
    f.write('\nClues:\n')
    for word, details in d.items():
        f.write(f"{word}: {details[1]} ({details[0]} at {details[2]}, {details[3]})\n")
