{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import torch\
import torch.nn as nn\
\
class RNN(nn.Module):\
    def __init__(self, embedding_dim, hidden_dim, output_dim, vocab_size, pad_idx):\
        super(RNN, self).__init__()\
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=pad_idx)\
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)\
        self.fc = nn.Linear(hidden_dim, output_dim)\
        self.softmax = nn.Softmax(dim=1)\
\
    def forward(self, x):\
        embedded = self.embedding(x)\
        _, hidden = self.rnn(embedded)\
        output = self.fc(hidden.squeeze(0))\
        output = self.softmax(output)\
        return output\
\
if __name__ == "__main__":\
    print("RNN script loaded. Use a training script for execution.")\
}