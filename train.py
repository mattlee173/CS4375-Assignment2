{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import torch\
from torch.utils.data import DataLoader, Dataset\
import json\
from ffnn import FFNN\
from rnn import RNN\
\
# Load dataset\
class ReviewDataset(Dataset):\
    def __init__(self, data_path):\
        with open(data_path, 'r') as f:\
            self.data = json.load(f)\
\
    def __len__(self):\
        return len(self.data)\
\
    def __getitem__(self, idx):\
        return self.data[idx]['text'], self.data[idx]['stars']\
\
if __name__ == "__main__":\
    train_dataset = ReviewDataset("training.json")\
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)\
\
    model = FFNN(input_dim=100, hidden_dim=64, output_dim=5)\
    print("Model initialized for FFNN.")\
}