{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww34360\viewh19060\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import torch\
import torch.nn as nn\
\
class FFNN(nn.Module):\
    def __init__(self, input_dim, hidden_dim, output_dim):\
        super(FFNN, self).__init__()\
        self.fc1 = nn.Linear(input_dim, hidden_dim)\
        self.relu = nn.ReLU()\
        self.fc2 = nn.Linear(hidden_dim, output_dim)\
        self.softmax = nn.Softmax(dim=1)\
\
    def forward(self, x):\
        x = self.fc1(x)  # First layer\
        x = self.relu(x)  # Activation\
        x = self.fc2(x)  # Output layer\
        x = self.softmax(x)  # Convert to probabilities\
        return x\
\
if __name__ == "__main__":\
    print("FFNN script loaded. Use a training script for execution.")\
}