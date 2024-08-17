#function to check if the current board is valid

#function to print the board that we have inputted, while also formatting it to look like a grid.
def print_board(b):
    for i in range(len(b)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - -") #for horizontal division
        for j in range(len(b[0])):
            if j%3==0 and j!=0:
                print(" | ", end="") #for vertical division
            if j == 8: 
                print(b[i][j]) #to go to the next line
            else:
                print(str(b[i][j]) + " ", end="")

#function to find the empty spaces in the grid. In this case, that would be zero.
def find_empty_space(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]==0:
                return (i,j)

