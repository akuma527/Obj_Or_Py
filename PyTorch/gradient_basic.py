import torch

x = torch.ones(1, requires_grad=True)
y = x + 2
c = x**2+5*x
z = y * y * 2

# Gradients are Accumulating
z.backward()     # automatically calculates the gradient
y.backward()
c.backward()
print(x.grad)    # ∂z/∂x = 12