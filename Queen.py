def printBoard(board):
  for row in board:
    print(row); 
  print('--------------------')

def appendPosition(i,j):
  pos = str(i)+str(j)
  if(pos not in unavailable):
    unavailable.append(pos)
   
def markUnavailable(i,j):
    for a in range(n):
        appendPosition(i,a)
        appendPosition(a,j)
    temp = 1
    for b in range(n):
      if(i-temp >=0 and j-temp>=0):
          appendPosition(i-temp, j-temp)
      if(i-temp >=0 and j+temp<=3):
          appendPosition(i-temp, j+temp)
      if(i+temp <=3 and j-temp>=0):
          appendPosition(i+temp, j-temp)
      if(i+temp <=3 and j+temp<=3):
          appendPosition(i+temp, j+temp)
      temp = temp+1;


def placeQueen():
  for i in range(n):
    for j in range(n):
      pos = str(i)+str(j)
      if(pos not in unavailable):
        board[i][j] = 1
        markUnavailable(i,j)
        return True
  return False    
          
def play():
   global board
   global unavailable
   for i in range(n):
      # loop will run 4 times (in our case)
      # initiall place queen at [0][0], if it doesn't work then [0][1] then [0][2] then [0][3]
      board[0][i] = 1
      markUnavailable(0,i)
      for j in range(n-1):
        # Loop will run 3 times to place the remaining 3 queens
	# placeQueen will always return True for 2nd and 3rd queen, but for
	# 3rd it can be True or False, indicating if it was placed successfully or not
        final = placeQueen();
      if(final):
        # final will store True or False for the last queen, if True then we have found 
        # the solution and so we come out of the function
        return
      else:
	# final is False means that the 4th queen was not placed, so we clear the 
	# board and unavailable and start over again
        board = [[0] * n for _ in range(n)]
        unavailable = []

n = 4
# Creates a 4x4 matrix of all zeros
board = [[0] * n for _ in range(n)]
# A list that will store all the positions where a queen can be attacked  
unavailable = []
     
play();
printBoard(board)
