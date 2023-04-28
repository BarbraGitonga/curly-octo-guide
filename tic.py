import tkinter as tk
import numpy as np


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")

        self.board = np.zeros((3,3), dtype=int)
        self.turn = 1

        self.button_list = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text="", width=10, height=5, command=lambda i=i,j=j:self.move(i,j))
                button.grid(row=i, column=j)
                row.append(button)
            self.button_list.append(row)

        self.label = tk.Label(master, text="Player 1's turn")
        self.label.grid(row=3, columnspan=3)

        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.grid(row=4, columnspan=3)

    def move(self, i, j):
        if self.board[i,j] == 0:
            self.board[i,j] = self.turn
            self.button_list[i][j].config(text="X" if self.turn == 1 else "O")
            self.button_list[i][j].config(state="disabled")
            self.turn *= -1
            self.label.config(text="Player 1's turn" if self.turn == 1 else "Player 2's turn")
            winner = self.check_winner()
            if winner != 0:
                self.label.config(text="Player 1 wins!" if winner == 1 else "Player 2 wins!")
                for row in self.button_list:
                    for button in row:
                        button.config(state="disabled")

    def check_winner(self):
        for i in range(3):
            if np.all(self.board[i,:] == 1):
                return 1
            elif np.all(self.board[i,:] == -1):
                return -1
            elif np.all(self.board[:,i] == 1):
                return 1
            elif np.all(self.board[:,i] == -1):
                return -1
        if np.all(np.diag(self.board) == 1):
            return 1
        elif np.all(np.diag(self.board) == -1):
            return -1
        elif np.all(np.diag(np.fliplr(self.board)) == 1):
            return 1
        elif np.all(np.diag(np.fliplr(self.board)) == -1):
            return -1
        elif np.count_nonzero(self.board == 0) == 0:
            return 2
        else:
            return 0

    def restart(self):
        self.board = np.zeros((3,3), dtype=int)
        self.turn = 1
        self.label.config(text="Player 1's turn")
        for i in range(3):
            for j in range(3):
                self.button_list[i][j].config(text="")
                self.button_list[i][j].config(state="normal")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
