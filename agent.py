import torch
from collections import deque
from model import CatchModel
import torch.nn as nn
import torch.optim as optim

class Agent:

    def __init__(self):

        self.model = CatchModel()
        self.memory = deque(maxlen=10000)
        self.optimizer = optim.Adam(
            self.model.parameters(),
            lr=0.001
        )
        self.criterion = nn.CrossEntropyLoss()

    def get_action(self, state):

        state = torch.tensor(
            state,
            dtype=torch.float32
        ) # get the current state ex: [220, 100, 320] -> convert it into tensor "[ball_x, ball_y, player_x]"

        with torch.no_grad():
            prediction = self.model(state)

        # supose the model returns : tensor([-1.4, 0.8, 2.4]) meaning left = -1.4, stay = 0.8 and right 2.4
        action = torch.argmax(prediction).item() # choose the biggest one , for this example becomes "2" which means "move right"

        return action

    def remember(
        self,
        state,
        action,
        reward,
        next_state,
        done
    ):
        self.memory.append(
            (
                state,
                action,
                reward,
                next_state,
                done
            )
        )

    def train(self):

        if len(self.memory) == 0:
            return

        state, action, reward, next_state, done = self.memory[-1]

        paddle_center = state[2] + 120 / 2

        if state[0] < paddle_center - 10:
            target = 0

        elif state[0] > paddle_center + 10:
            target = 2

        else:
            target = 1

        state = torch.tensor(
            state,
            dtype=torch.float32
        )

        target = torch.tensor([target])
        prediction = self.model(state)
        loss = self.criterion(
            prediction.unsqueeze(0),
            target
        )

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
