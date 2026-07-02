import pygame
import random

from game import CatchGame

game = CatchGame()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    action = random.randint(0, 2)

    reward, done = game.step(action)

    game.draw()

    if done:
        print("Reward:", reward)
        game.reset()

    game.tick()

pygame.quit()
