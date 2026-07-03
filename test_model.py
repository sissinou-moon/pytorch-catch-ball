import torch
from model import CatchModel

model = CatchModel()

state = torch.tensor([250.0, 100.0, 300.0])

output = model(state)

print(output)
