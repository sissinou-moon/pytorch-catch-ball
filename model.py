import torch
import torch.nn as nn


class CatchModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(3, 16), # 3 inputs -> 16 neural
            nn.ReLU(),
            nn.Linear(16, 3) # from 16 neural -> 3 outputs
        )

    def forward(self, x):
        return self.network(x)
