import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.current_player = "X"
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]

        self.score = {"X": 0, "O": 0}
        self.buttons = []

        # UI
        self.title_label = tk.Label(root, text="TicTacToe", font=("", 15))
        self.title_label.place(x=150, anchor="n")

        self.score_label = tk.Label(root, text="X: 0   O: 0", font=("", 12))
        self.score_label.place(x=150, y=30, anchor="n")

        self.create_board()

    # -----------------------------------------------------

    def create_board(self):
        for r in range(3):
            row = []
            for c in range(3):
                btn = tk.Button(self.root, anchor="center",
                                command=lambda rr=r, cc=c: self.click(rr, cc))
                btn.place(x=c*100, y=70 + r*100, width=100, height=100)
                row.append(btn)
            self.buttons.append(row)

    # -----------------------------------------------------

    def click(self, r, c):
        if self.board[r][c] != "":
            return

        
        if self.current_player == "X":
            self.buttons[r][c].config(text="X", fg="red", font=("", 40))
            self.board[r][c] = "X"
            self.current_player = "O"
        else:
            self.buttons[r][c].config(text="O", fg="blue", font=("", 40))
            self.board[r][c] = "O"
            self.current_player = "X"

        
        winner = self.check_win()
        if winner:
            self.score[winner] += 1
            self.update_score()
            self.reset_board()
            return

        
        if self.check_draw():
            self.reset_board()

    # -----------------------------------------------------

    def check_win(self):
        b = self.board

        
        for r in range(3):
            if b[r][0] != "" and b[r][0] == b[r][1] == b[r][2]:
                return b[r][0]

        
        for c in range(3):
            if b[0][c] != "" and b[0][c] == b[1][c] == b[2][c]:
                return b[0][c]

        
        if b[0][0] != "" and b[0][0] == b[1][1] == b[2][2]:
            return b[0][0]

        
        if b[0][2] != "" and b[0][2] == b[1][1] == b[2][0]:
            return b[0][2]

        return None

    # -----------------------------------------------------

    def check_draw(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    return False
        return True

    # -----------------------------------------------------

    def update_score(self):
        self.score_label.config(text=f"X: {self.score['X']}   O: {self.score['O']}")

    # -----------------------------------------------------

    def reset_board(self):
        for r in range(3):
            for c in range(3):
                self.board[r][c] = ""
                self.buttons[r][c].config(text="")
        self.current_player = "X"

# ---------------------------------------------------------

root = tk.Tk()
root.title("TicTacToe")
root.geometry("300x380")

game = TicTacToe(root)

root.mainloop()
