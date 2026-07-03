import random
import pygame
from agent import Agent
from game import CatchGame

game = CatchGame()
agent = Agent()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    state = game.get_state()

    action = agent.get_action(state)

    next_state, reward, done = game.step(action)

    agent.remember(
        state,
        action,
        reward,
        next_state,
        done
    )

    print(agent.memory[-1])

    agent.train()

    game.draw()

    if done:
        print("Reward:", reward)
        game.reset()

    game.tick()

pygame.quit()
