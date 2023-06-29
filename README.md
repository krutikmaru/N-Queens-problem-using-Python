# N-Queens-problem-using-Python

Problem statement: 
In 4 Queen’s problem, 4 Queen’s have to be placed on a 4x4 chessboard in such a way that no queen can attack any other queen, which means that if we consider any queen then there should be no queen on it’s row, column, and diagonal.
This problem extends to N Queen’s problem where N can be any number, if it is 8 then we’ll have to do the same for 8 queen’s on an 8x8 chess board.

Logic:
The technique I am using here goes like, one queen will always be in the first row (Can be in any column).
So first I place the queen at `[0][0]` and then mark all the position that come on it’s row, column, and diagonal as unavailable, because if we place another queen over there then that queen can be attacked.
Now for the second queen, I check for the first ever location that is available and place the 2nd queen over there, then mark all the positions that come on it’s row, column. and diagonal as unavailable.
Same for 3rd queen
Now for the 4th queen, using this approach, if everything was right then exactly one cell would have been left available for 4th queen, we can place the queen over there and our solution is ready, however if there are no positions available then we will have to start over again. ***We need to clear the entire board and mark all the 16 locations as available***. 
Now we place the 1st queen at `[0][1]` and perform the process once again.
If again not then we start over again with 1st queen at `[0][2]` then `[0][3]`
However we will definitely get a solution from any one out of these 4 tries. It is impossible to not get a solution.
