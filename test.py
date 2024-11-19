import torch
from astra.model import Model
from astra.gpt_model import GPTModel

torch.serialization.add_safe_globals([GPTModel])


# Example usage
model = Model('')
print(model.config)