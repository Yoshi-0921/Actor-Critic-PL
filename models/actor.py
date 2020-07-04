import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import pytorch_lightning as pl

class Actor(nn.Module):
    def __init__(self):
        super(Actor, self).__init__()

    def forward(self, x):
        pass