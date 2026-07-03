```
pytorch_catch_ball/
│
├── main.py          # game loop
├── model.py         # PyTorch network
├── agent.py         # chooses actions + tran model
├── game.py          # pygame game
```

### game.py

This file is **the game itself**.

It knows everything about the world:
- How big the window is.
- Where the ball is.
- Where the player is.
- How fast things move.
- Whether the ball was caught.
- Whether the game is over.

It **doesn't know anything about AI**.
Imagine you're making a real game. `game.py` is the game engine.

### main.py

This is the controller , it says `Start Game` Then `Repeat forever`.

Right now we have :
```
Random action
      ↓
Game
      ↓
Reward
```

We are going to replace the "Random action" with :
```
Game State
      ↓
PyTorch Neural Network
      ↓
Choose Action
      ↓
Game
      ↓
Reward
```

In-Order to build what we planted before, we need to understand that we are going to build neural network that can solve :
- We give information like :
```
Ball X = 250
Ball Y = 100
Player X = 300
```
- And then we ask :
```
Should the paddle move left, stay or right?
```

**Inputs :**
```
ball_x
ball_y
player_x
```

**Outputs :** 
```
[-0.4, 2.1, 0.3]
```

We interpret them as :
```
Left  = -0.4
Stay  =  2.1
Right =  0.3
```
The biggest value wins.

### agent.py
```python
optimizer = optim.Adam(...)
```
Imagine the network answers was `Left` but the right answer is `Right`, the `Optimizer` says "Oky, let's adjust the network's weights a little bit".

```python
criterion = nn.CrossEntropyLoss()
```
This one measures the how long was the network, example the correct answer is `Right` but the predication was `Left` , `Loss = 4.3` -> Very bad.

```python
state = torch.tensor([[150., 50., 300.]])  
target = torch.tensor([0]) # Left

# STEPS
prediction = model(state) # ASK THE MODEL

loss = criterion(prediction, target) # MEASURE HOW WRONG IT WAS

optimizer.zero_grad() # CLEAR GRADIENTS FROM THE PREVIOUS STEP

loss.backward() # It computes how every weight in the network should change to reduce the loss

optimizer.step() # UPDATES THE WEIGHTS
```
Every training loop in PyTorch follows these same five steps.

#### Example:
```
Ball X = 150
Player X = 300
```
What's the correct action ?
We think `Left` is correct, but in reinforcement leaning nobody tells the AI that, it only gets `Reward = 1 | Reward = -1` That isn't enough to train your network with `CrossEntropyLoss`.
This why `DQN` exisits `Deep Q-Network` 

#### DQN:
It introduces four new ideas:
1. Experience replay
2. Epsilon-greedy exploration
3. Q-values
4. Bellman equation
Those aren't just extra features, they're **required** for the network to learn from rewards.

(It's to hard for now to add this function, we gonna use it in the same project)

#### What happens during trainning?
```
Guess

↓

Measure error

↓

Adjust weights

↓

Guess again
```

We will use `from collections import deque` :
```
+-----------------------------------+
| A | B | C | D | E |
+-----------------------------------+
```
adding `F` :
```
+-----------------------------------+
| B | C | D | E | F |
+-----------------------------------+
```
The oldest experience disappears, we will use that in memory process because we need our ai to store all old experiences with their reward, this called **Experience Replay**.

We'll make the AI learn **one simple rule**:

> **Move toward the ball.**

This is called **Behavior Cloning (Supervised Learning)**.
