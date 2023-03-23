import torch
import torch.nn as nn
import torch.optim as optim

import math
import numpy as np

class Transformer(nn.Module):
    def __init__(
        self,
        num_tokens,
        dim_model,
        num_heads,
        num_encoder_layers,
        num_decoder_layers,
        dropout_p,
    ):
        super().__init__()
        
        self.transformer = nn.Transformer(
            d_model = dim_model,
            nhead = num_heads,
            num_encoder_layers= num_encoder_layers,
            num_decoder_layers= num_decoder_layers,
            dropout= dropout_p,
        )
        
    def forward(self):
        pass
    
    
class PositionalEncoding(nn.Module):
    def __init__(self, dim_model, dropout_p, max_len):
        super().__init__()
        
        self.dropout = nn.Dropout(dropout_p)
        
        pos_encoding = torch.zeros(max_len, dim_model)
        positions_list = torch.arrange(0, max_len, dtype=torch.float).view(-1, 1)
        division_term = torch.exp(torch.arrange(0, dim_model, 2).float() * (-math.log(10000.0)) / dim_model)
        
        # PE(pos, 2i) = sin(pos/1000^(2i/dim_model))
        pos_encoding[:, 0::2] = torch.sin(positions_list * division_term)
        
        # PE(pos, 2i + 1) = cos(pos/1000^(2i/dim_model))
        pos_encoding[:, 1::2] = torch.cos(positions_list * division_term)
        
        # Saving buffer (same as parameter without gradients needed)
        pos_encoding = pos_encoding.unsqueeze(0).transpose(0, 1)
        self.register_buffer("pos_encoding",pos_encoding)
        
    def forward(self, token_embedding: torch.tensor) -> torch.tensor:
         return self.dropout(token_embedding + self.pos_encoding[:token_embedding.size(0), :])
