from turtle import Turtle
ALINHAMENTO="right"
FONTE=("Courier",24,"normal")

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0        
        self.penup()
        self.goto(-200,270)        
        self.update_score()
        self.hideturtle()
        self.penup()
        
    def update_score(self):
        self.write(f"Score: {self.score}",align='right',font=12)
        
    def soma_se(self):
        self.score+=1
        self.clear()
        self.update_score()
        
    def over(self):                
        self.goto(0,0)        
        self.write("Game Over",align="center",font=24)