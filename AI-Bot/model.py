import torch
import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        #1linear layer
        self.l1 = nn.Linear(input_size, hidden_size) 
        #2linear layer
        self.l2 = nn.Linear(hidden_size, hidden_size)
        #3linear layer
        self.l3 = nn.Linear(hidden_size, num_classes)
        #activation function Relu
        self.relu = nn.ReLU() 

    #Implemetation of forward pass
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        # no activation and softmax (later to be used)
        return out