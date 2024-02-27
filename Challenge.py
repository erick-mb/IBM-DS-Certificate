
def most_frequent(s):
    freq_dict = {}
    s = list(s)
    for char in s:
        if not char.isnumeric():
            if char in freq_dict:
                freq_dict[char] +=1
            else: freq_dict[char] =1
    return max(freq_dict,key=freq_dict.get)

def special_integer(list):
    for x in range(0,100):
        if sum([i>=x for i in list]) == x:
            return x
    return -1

def rever(s):
    s = list(s)
    right_pointer = 0
    left_pointer = len(s)-1
    while right_pointer < left_pointer:
        if not s[left_pointer].isalpha():
            left_pointer -= 1
        elif not s[right_pointer].isalpha():
            right_pointer +=1
        else: 
            temp = s[right_pointer] 
            s[right_pointer] = s[left_pointer]
            s[left_pointer] = temp
            left_pointer -= 1
            right_pointer +=1
    return("".join(s))    

def get_streak(s):
    streaks_dict={}
    streak = ""
    for char in s:
        if char in streak:
            if streak not in streaks_dict:
                streaks_dict[streak] = len(streak)
            streak = "" +char
        else: streak += char
    return max(streaks_dict.values())

class EvenStream:
    def get_next(end):
        value = 0
        counter = 1
        while counter <= end:
            print(value)
            value += 2
            counter += 1
            
def print_from_stream(n,stream=EvenStream):
    stream.get_next(n)

matrix = [
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [0,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,0,0],
    [1,0,0,0,0,1],
]

def removeIslands(matrix):
    matrix_width = len(matrix[0])
    matrix_height = len(matrix)
    islands=[]
    for j in range(0,matrix_width):
        corner = 0
        if matrix[corner][j]==1 and (corner,j) not in islands:
            islands.append((corner,j))
            islands = find_islands_conection(matrix,islands,corner,j)
        corner = matrix_height-1
        if matrix[corner][j]==1 and (corner,j) not in islands:
            islands.append((corner,j))
            islands = find_islands_conection(matrix,islands,corner,j)
    for i in range(0,matrix_height):
        corner = 0
        if matrix[i][corner]==1 and (i,corner) not in islands:
            islands.append((i,corner))
            islands = find_islands_conection(matrix,islands,i,corner)
        corner = matrix_width-1
        if matrix[i][corner]==1 and (i,corner) not in islands:
            islands.append((i,corner))
            islands = find_islands_conection(matrix,islands,i,corner)

    for i in range(1,matrix_height-1):
        for j in range(1,matrix_width-1):
            if matrix[i][j]==1 and (i,j) not in islands:
                matrix[i][j]=0
    print(matrix)

def find_islands_conection(matrix,islands,i,j):
    if i+1<=len(matrix)-1:
       if matrix[i+1][j]==1 and (i+1,j) not in islands:
        islands.append((i+1,j))
        islands = find_islands_conection(matrix,islands,i+1,j)
    if i-1>=0:
       if matrix[i-1][j]==1 and (i-1,j) not in islands:
        islands.append((i-1,j))
        islands = find_islands_conection(matrix,islands,i-1,j)
    if j-1>=0:
       if matrix[i][j-1]==1 and (i,j-1) not in islands:
        islands.append((i,j-1))
        islands = find_islands_conection(matrix,islands,i,j-1)
    if j+1<=len(matrix[0])-1:
       if matrix[i][j+1]==1 and (i,j+1) not in islands:
        islands.append((i,j+1))
        islands = find_islands_conection(matrix,islands,i,j+1)

    return islands

removeIslands(matrix)