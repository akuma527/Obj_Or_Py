import torch
import numpy

class Feedforward(torch.nn.Module):
        
        def __init__(self, input_size, hidden_size):
            super().__init__()
            self.input_size = input_size
            self.hidden_size  = hidden_size
            self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size)
            self.relu = torch.nn.ReLU()
            self.fc2 = torch.nn.Linear(self.hidden_size, 1)
            self.sigmoid = torch.nn.Sigmoid()
        
        def forward(self, x):
            hidden = self.fc1(x)
            relu = self.relu(hidden)
            output = self.fc2(relu)
            output = self.sigmoid(output)
            return output



# CREATE RANDOM DATA POINTS
from sklearn.datasets import make_blobs
def blob_label(y, label, loc): # assign labels
    target = numpy.copy(y)
    for l in loc:
        target[y == l] = label
    return target
x_train, y_train = make_blobs(n_samples=40, n_features=2,
 cluster_std=1.5, shuffle=True, random_state=42)

x_train = torch.FloatTensor(x_train)
y_train = torch.FloatTensor(blob_label(y_train, 0, [0]))
y_train = torch.FloatTensor(blob_label(y_train, 1, [1,2,3]))
x_test, y_test = make_blobs(n_samples=10, n_features=2,
 cluster_std=1.5, shuffle=True, random_state=41)
x_test = torch.FloatTensor(x_test)
y_test = torch.FloatTensor(blob_label(y_test, 0, [0]))
y_test = torch.FloatTensor(blob_label(y_test, 1, [1,2,3]))

# Initialize Model
model = Feedforward(2, 3)
criterion = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)


model.eval()
y_pred = model(x_test)
before_train = criterion(y_pred.squeeze(), y_test)
print('Test loss before training' , before_train.item())


# model.train()
epoch = 30
correct = 0
for epoch in range(epoch):
    # Since Gradient accumulates
    optimizer.zero_grad()
    # Forward pass
    y_pred = model(x_train)
    # Compute Loss
    loss = criterion(y_pred.squeeze(), y_train)
   
    output = (y_pred.squeeze()>0.5).float()
    correct += (output == y_train).float().sum()
    accuracy = 100 * correct / len(x_train)

    print('Epoch {}: loss: {} Acc: {}'.format(epoch, loss.item(), accuracy))
    # Backward pass
    loss.backward()
    optimizer.step()
    correct=0

# for name,param in model.named_parameters():
#     print(name, param.shape)