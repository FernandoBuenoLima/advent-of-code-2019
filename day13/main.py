import pygame
from pygame.locals import *
from intcode import IntcodeComputer
from arcade import *

program = [int(s) for s in open("input.txt").read().split(',')]
program[0] = 2 #inserting quarters

pygame.init()
screen = pygame.display.set_mode((400, 260))
pygame.display.set_caption("ARCADE - 0")
clock = pygame.time.Clock()

computer = IntcodeComputer(program)
arcade = Arcade(computer, (26, 40))

wall = pygame.Surface((10, 10))
wall.fill((255, 255, 255))
block = pygame.Surface((10, 10))
block.fill((255, 0, 0))
paddle = pygame.Surface((10, 10))
paddle.fill((255, 255, 255))
ball = pygame.Surface((10, 10))
ball.fill((0, 255, 0))

joystick = 0
current_mode = INPUT_UPDATE
arcade.start()

#drawing screen
screen.fill((0, 0, 0))

for x in range(arcade.width):
    for y in range(arcade.height):
        code = arcade.grid[x][y]
        if code == 0:
            pass
        elif code == 1:
            screen.blit(wall, ((x*10), (y*10)))
        elif code == 2:
            screen.blit(block, ((x*10), (y*10)))
        elif code == 3:
            screen.blit(paddle, ((x*10), (y*10)))
        elif code == 4:
            screen.blit(ball, ((x*10), (y*10)))
            
pygame.display.update()
keyPressed = False
while not keyPressed:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                joystick = -1
            elif event.key == K_RIGHT:
                joystick = 1
            keyPressed = True

while True:
    clock.tick(5)
    pygame.display.set_caption("ARCADE - " + str(arcade.score))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                joystick = -1
            elif event.key == K_RIGHT:
                joystick = 1
        if event.type == KEYUP:
            if event.key in (K_LEFT, K_RIGHT):
                joystick = 0
    
    if current_mode == DEFAULT:
        current_mode = arcade.run()    
    elif current_mode == INPUT_UPDATE:
        current_mode = arcade.run([joystick])
    else:
        assert current_mode == GAME_OVER
        pygame.quit()
        quit()
    
    #drawing screen
    screen.fill((0, 0, 0))
    
    for x in range(arcade.width):
        for y in range(arcade.height):
            code = arcade.grid[x][y]
            if code == 0:
                pass
            elif code == 1:
                screen.blit(wall, ((x*10), (y*10)))
            elif code == 2:
                screen.blit(block, ((x*10), (y*10)))
            elif code == 3:
                screen.blit(paddle, ((x*10), (y*10)))
            elif code == 4:
                screen.blit(ball, ((x*10), (y*10)))
                
    pygame.display.update()
    