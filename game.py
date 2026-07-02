import pygame
import random

WIDTH = 600
HEIGHT = 600

BALL_SIZE = 20

PLAYER_WIDTH = 120
PLAYER_HEIGHT = 20

BALL_SPEED = 5
PLAYER_SPEED = 8


class CatchGame:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch the Ball")

        self.clock = pygame.time.Clock()

        self.reset()

    def reset(self):

        self.ball_x = random.randint(0, WIDTH - BALL_SIZE)
        self.ball_y = 0

        self.player_x = WIDTH // 2 - PLAYER_WIDTH // 2
        self.player_y = HEIGHT - 40

        self.score = 0

    def step(self, action):

        # action:
        # 0 left
        # 1 stay
        # 2 right

        if action == 0:
            self.player_x -= PLAYER_SPEED

        elif action == 2:
            self.player_x += PLAYER_SPEED

        self.player_x = max(0, min(self.player_x, WIDTH - PLAYER_WIDTH))

        self.ball_y += BALL_SPEED

        reward = 0
        done = False

        if self.ball_y >= self.player_y:

            if self.player_x <= self.ball_x <= self.player_x + PLAYER_WIDTH:
                reward = 1
                self.score += 1
            else:
                reward = -1

            done = True

        return reward, done

    def draw(self):

        self.screen.fill((30, 30, 30))

        pygame.draw.circle(
            self.screen,
            (255, 255, 255),
            (self.ball_x, self.ball_y),
            BALL_SIZE // 2,
        )

        pygame.draw.rect(
            self.screen,
            (0, 200, 255),
            (
                self.player_x,
                self.player_y,
                PLAYER_WIDTH,
                PLAYER_HEIGHT,
            ),
        )

        pygame.display.flip()

    def tick(self):
        self.clock.tick(60)
