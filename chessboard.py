import matplotlib.pyplot as mtpl
import numpy as np

board = np.tile(np.eye(2)[0],(8,4))
for i in range(board.shape[0]):
    board[i] = np.roll(board[i],i)
mtpl.gray()
mtpl.matshow(board)
mtpl.show()
