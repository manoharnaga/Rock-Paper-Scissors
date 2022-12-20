from rule import *

def print_state(iter,state_mat):
    outputfile = open("output.txt","w+")
    print(iter)
    for row in state_mat:
        line_str = ""
        for val in row:
            if(val):
                line_str+="X"
                print('X',end='')
            else:
                line_str+="O"
                print('O',end='')  
        print()
        line_str+="\n"
        outputfile.write(line_str)
    outputfile.close()


def copy_mat(mat2,mat1,Rows,Cols):
    for i in range(0,Rows):
        for j in range(0,Cols):
            mat2[i][j]=mat1[i][j]
    

def make_neighbours(i,j,Rows,Cols,state_mat):
    neighbours = [int(-1) for i in range(8)]
    if((i-1)>=0 and (j-1)>=0):
        if(state_mat[i-1][j-1]==1):
            neighbours[0]=int(1)
        else:
            neighbours[0]=int(0)
    if((i-1)>=0 and (j+1)<Cols):
        if(state_mat[i-1][j+1]==1):
            neighbours[2]=int(1)
        else:
            neighbours[2]=int(0)
    if((i+1)<Rows and (j-1)>=0):
        if(state_mat[i+1][j-1]==1):
            neighbours[5]=int(1)
        else:
            neighbours[5]=int(0)
    if((i+1)<Rows and (j+1)<Cols):
        if(state_mat[i+1][j+1]==1):
            neighbours[7]=int(1)
        else:
            neighbours[7]=int(0)

    if( (i-1)>=0 ):
        if(state_mat[i-1][j]==1):
            neighbours[1]=int(1)
        else:
            neighbours[1]=int(0)
    if((i+1)<Rows):
        if(state_mat[i+1][j]==1):
            neighbours[6]=int(1)
        else:
            neighbours[6]=int(0)
    if( (j-1)>=0 ):
        if(state_mat[i][j-1]==1):
            neighbours[3]=int(1)
        else:
            neighbours[3]=int(0)
    if((j+1)<Cols):
        if(state_mat[i][j+1]==1):
            neighbours[4]=int(1)
        else:
            neighbours[4]=int(0)

    return neighbours


fileptr = open("config.txt","r")
lines = fileptr.readlines()
Dimensions = lines[0].strip("\n")


#  INITIALISING STATE MATRIX
Dim_list = Dimensions.split()
Rows=int(Dim_list[0])
Cols=int(Dim_list[1])
WhiteCells=int(Dim_list[2])


state_mat = [[0 for i in range(Cols)] for j in range(Rows)]
temp_state_mat = [[0 for i in range(Cols)] for j in range(Rows)]
curr_state_mat = [[0 for i in range(Cols)] for j in range(Rows)]


#  INITIALISING STATE MATRIX
for k in range(1,len(lines)):
    row_list=lines[k].split()
    # print(row_list[0],row_list[1])
    i=int(row_list[0])
    j=int(row_list[1])

    state_mat[i-1][j-1]=1   # MATRIX IS ZERO-INDEXING

print_state(0,state_mat)

# curr_state_mat AND temp_state_mat --> TEMPORARY STORAGE FOR EACH ITERATION
iteration=0
while(1):
    x = int(input("Enter the Iteration Number: "))
    if(x==-1):
        print("Program Terminated!!\n")
        break
    iteration+=x

    copy_mat(temp_state_mat,state_mat,Rows,Cols)
    copy_mat(curr_state_mat,state_mat,Rows,Cols)
    for k in range(0,iteration):
        for i in range(0,Rows):
            for j in range(0,Cols):
                neighbour_list = make_neighbours(i,j,Rows,Cols,temp_state_mat)
                curr_state_mat[i][j]=rule(temp_state_mat[i][j],neighbour_list)
        copy_mat(temp_state_mat,curr_state_mat,Rows,Cols)
    
    print_state(iteration,curr_state_mat)