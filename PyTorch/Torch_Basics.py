import torch


torch.random.manual_seed(7)
print(torch.random.initial_seed())
ts = torch.randperm((4,4))
print(ts)