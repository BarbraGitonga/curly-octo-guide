
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from main_design import *
import numpy as np

class MainApplication(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## Variables
        self.board = np.zeros((3,3), dtype=int)
        self.turn = 1
        self.button_index_dict = {}

        ## Setup Functions
        self.init_ui()

        ## Connections
        self.ui.exit_biutton.clicked.connect(self.exit_game)

        self.buttons_list = [
            self.ui.index1,
            self.ui.index2,
            self.ui.index3,
            self.ui.index4,
            self.ui.index5,
            self.ui.index6,
            self.ui.index7,
            self.ui.index8,
            self.ui.index9,
        ]

        self.ui.index1.clicked.connect(lambda: self.play_game(1))
        self.ui.index2.clicked.connect(lambda: self.play_game(2))
        self.ui.index3.clicked.connect(lambda: self.play_game(3))
        self.ui.index4.clicked.connect(lambda: self.play_game(4))
        self.ui.index5.clicked.connect(lambda: self.play_game(5))
        self.ui.index6.clicked.connect(lambda: self.play_game(6))
        self.ui.index7.clicked.connect(lambda: self.play_game(7))
        self.ui.index8.clicked.connect(lambda: self.play_game(8))
        self.ui.index9.clicked.connect(lambda: self.play_game(9))

        for i, button in enumerate(self.buttons_list):
            button.clicked.connect(lambda: print(i))

    
    def init_ui(self):
        
        ## Make fullscreen
        self.showMaximized()

        count = 1
        for i in range(3):
            for j in range(3):
                self.button_index_dict[count] = i,j
                count += 1
        
        print(self.button_index_dict)
         

    def exit_game(self):
        
        ## Other Logic

        ## Exit
        self.close()
    
    def play_game(self, index: int):
        
        print(f"Index {index} pressed")
        
        i, j = self.button_index_dict.get(index)
        self.move(i=i, j=j)
    

    def move(self, i, j):

        if self.board[i,j] == 0:
            self.board[i,j] = self.turn
            play = "X" if self.turn == 1 else "O"
            index = list(self.button_index_dict.keys())[list(self.button_index_dict.values()).index((i, j))]
            
            self.buttons_list[index-1].setText(play)
            print(play, index)
            # self.button_list[i][j].config(text="X" if self.turn == 1 else "O")
            # self.button_list[i][j].config(state="disabled")
            self.turn *= -1
            title = "Player 1's turn" if self.turn == 1 else "Player 2's turn"
            self.ui.title_label.setText(title)
            # self.label.config(text="Player 1's turn" if self.turn == 1 else "Player 2's turn")
            winner = self.check_winner()
            if winner != 0:
                state = "Player 1 wins!" if winner == 1 else "Player 2 wins!"
                self.ui.title_label.setText(state)
                print(state)
                self.buttons_list[index-1].blockSignals(False)
    

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
    



if __name__ == "__main__":

    w = QApplication([])
    app = MainApplication()
    app.show()
    w.exec()





