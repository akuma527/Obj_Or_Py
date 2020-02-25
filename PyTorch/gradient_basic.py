import torch

x = torch.ones(1, requires_grad=True)
y = x + 2
z = y * y * 2
z.backward()     # automatically calculates the gradient
print(x.grad)    # ∂z/∂x = 12