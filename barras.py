from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7

class Barras(Turtle):
    
    def __init__(self):
        self.all_cars = []
        self.car_speedy=STARTING_MOVE_DISTANCE
        
    
    def carros(self):
        random_chance=random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move(self):
        for carros in self.all_cars:
            carros.backward(self.car_speedy)
            
    def level_up(self):
        self.car_speedy += MOVE_INCREMENT
        