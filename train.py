import torch
import torch.nn as nn
import torch.optim as optim

from model import CatchModel

model = CatchModel()

optimizer = optim.Adam(model.parameters(), lr=0.001)

criterion = nn.CrossEntropyLoss()
