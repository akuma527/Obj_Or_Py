import torch
import torchvision

torch.manual_seed(1)

x = torch.randn(1, 1)
w = torch.randn(1, 1, requires_grad=True)
w.register_hook(lambda x: print(x))
y = torch.randn(1, 1)

out = x * w
loss = (out - y)**2
loss.register_hook(lambda x: print(x))
loss.mean().backward(gradient=torch.tensor(0.1))  # prints the gradient in w and loss
