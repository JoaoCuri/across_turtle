from turtle import Screen
from player import Player
from barras import Barras
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
barras = Barras()
score = Score()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    barras.carros()
    barras.move()
    
    #detectar colisão com os carros
    for car in barras.all_cars:
        if car.distance(player)<20:
            score.over()
            game_is_on=False
            
    #chegou ao topo da tela
    if player.finish():
        player.start()
        barras.level_up()
        score.soma_se()


screen.exitonclick()