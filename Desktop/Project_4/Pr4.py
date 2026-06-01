
import random

class TicTacToeML:
    def __init__(self):
        self.board = [" "] * 9  
        self.memory = {} 
    
    def show(self):
        print(f"\n {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n")
    
    def empty(self):
        return [i for i in range(9) if self.board[i] == " "]
    def win(self, p):
        for a,b,c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]:
            if self.board[a] == self.board[b] == self.board[c] == p:
                return True
        return False
    def full(self):
        return " " not in self.board
    

    def ai_move(self):
        key = "".join(self.board)
        empty = self.empty()
        for m in empty:
            self.board[m] = "O"
            if self.win("O"):
                self.board[m] = " "
                return m
            self.board[m] = " "
        

        for m in empty:
            self.board[m] = "X"
            if self.win("X"):
                self.board[m] = " "
                return m
            self.board[m] = " "
        
       
        if key in self.memory:
            best_move = None
            best_score = -1000
            for m in empty:
                if m in self.memory[key]:
                    score = self.memory[key][m]  
                    if score > best_score:
                        best_score = score
                        best_move = m
            if best_move is not None:
                return best_move  
        
      
        if 4 in empty:
            return 4
        for c in [0,2,6,8]:
            if c in empty:
                return c
        return random.choice(empty)
    

    def learn(self, history, result):
        
        scores = {"win": 2, "draw": 0, "lose": -1}
        score = scores[result]
        
        for pos, board_key in history:
            if board_key not in self.memory:
                self.memory[board_key] = {}
          
            self.memory[board_key][pos] = self.memory[board_key].get(pos, 0) + score
    

    def play(self):
        print("=" * 45)
        print("  КРЕСТИКИ-НОЛИКИ С МАШИННЫМ ОБУЧЕНИЕМ")
        print("=" * 45)
        print("Вы - X, Компьютер - O\n")
        
        history = []  
        
        while True:
            self.show()
            
         
            try:
                m = int(input("Ваш ход (1-9): ")) - 1
                if m not in self.empty():
                    print("Клетка занята!")
                    continue
            except ValueError:
                print("Введите число от 1 до 9!")
                continue
            
            self.board[m] = "X"
            history.append((m, "".join(self.board)))  
            
            if self.win("X"):
                self.show()
                print("\nВЫ ВЫИГРАЛИ!")
                self.learn(history, "lose")  
                break
            
            if self.full():
                self.show()
                print("\nНИЧЬЯ!")
                self.learn(history, "draw")
                break
            
           
            print("\nКомпьютер думает...")
            m = self.ai_move()
            self.board[m] = "O"
            print(f"Компьютер сходил на {m + 1}")
            history.append((m, "".join(self.board)))
            
            if self.win("O"):
                self.show()
                print("\nКОМПЬЮТЕР ВЫИГРАЛ!")
                self.learn(history, "win")
                break
            
            if self.full():
                self.show()
                print("\nНИЧЬЯ!")
                self.learn(history, "draw")
                break
        
        
        print(f"\nОбучено позиций: {len(self.memory)}")
        
        again = input("\nСыграем ещё? (да/нет): ").lower()
        if again in ["да", "yes", "д", "y"]:
            self.board = [" "] * 9  
            self.play() 
        else:
            print("Спасибо за игру! Компьютер стал умнее!")


if __name__ == "__main__":
    game = TicTacToeML()
    game.play()
