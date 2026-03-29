import torch
import torch.nn as nn
from torch.nn import functional as F

class HydraConfig:
    """Hyperparameters for the Hydra Brain."""
    batch_size = 32 
    block_size = 256
    n_embd = 384
    n_head = 6
    n_layer = 6
    dropout = 0.2
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

class Head(nn.Module):
    """One head of self-attention."""
    def __init__(self, head_size):
        super().__init__()
        self.key = nn.Linear(HydraConfig.n_embd, head_size, bias=False)
        self.query = nn.Linear(HydraConfig.n_embd, head_size, bias=False)
        self.value = nn.Linear(HydraConfig.n_embd, head_size, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(HydraConfig.block_size, HydraConfig.block_size)))
        self.dropout = nn.Dropout(HydraConfig.dropout)

    def forward(self, x):
        B, T, C = x.shape
        k = self.key(x)   
        q = self.query(x) 
        # Compute attention scores ("affinities")
        wei = q @ k.transpose(-2, -1) * C**-0.5
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf'))
        wei = F.softmax(wei, dim=-1)
        wei = self.dropout(wei)
        # Perform the weighted aggregation of the values
        v = self.value(x)
        out = wei @ v
        return out

class MultiHeadAttention(nn.Module):
    """Multiple heads of self-attention in parallel."""
    def __init__(self, num_heads, head_size):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size) for _ in range(num_heads)])
        self.proj = nn.Linear(HydraConfig.n_embd, HydraConfig.n_embd)
        self.dropout = nn.Dropout(HydraConfig.dropout)

    def forward(self, x):
        out = torch.cat([h(x) for h in self.heads], dim=-1)
        out = self.dropout(self.proj(out))
        return out

class FeedForward(nn.Module):
    """A simple linear layer followed by a non-linearity."""
    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd),
            nn.Dropout(HydraConfig.dropout),
        )

    def forward(self, x):
        return self.net(x)

class Block(nn.Module):
    """Transformer block: communication followed by computation."""
    def __init__(self, n_embd, n_head):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size)
        self.ffwd = FeedForward(n_embd)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self, x):
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x

class HydraLanguageModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, HydraConfig.n_embd)
        self.position_embedding_table = nn.Embedding(HydraConfig.block_size, HydraConfig.n_embd)
        self.blocks = nn.Sequential(*[Block(HydraConfig.n_embd, n_head=HydraConfig.n_head) for _ in range(HydraConfig.n_layer)])
        self.ln_f = nn.LayerNorm(HydraConfig.n_embd)
        self.lm_head = nn.Linear(HydraConfig.n_embd, vocab_size)

    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding_table(idx)
        pos_emb = self.position_embedding_table(torch.arange(T, device=HydraConfig.device))
        x = tok_emb + pos_emb
        x = self.blocks(x)
        x = self.ln_f(x)
        logits = self.lm_head(x)

        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)

        return logits, loss

print(f" Hydra Core initialized on {HydraConfig.device.upper()}")

that is only start will carry on when bilt everything up!!
