import torch
from astra.model import Model



# # Example usage
model = Model('')
print(model.config)
# model_path = 'Astra_1.4B.pth'

# import torch
# from torch._utils import _rebuild_tensor_v2

# def rebuild_storage(storage):
#     # Example of manually rebuilding a tensor from storage
#     return _rebuild_tensor_v2(
#         storage,  # Storage object
#         storage_offset=0,
#         size=(10, 10),  # Replace with the correct size
#         stride=(10, 1),  # Replace with the correct stride
#         requires_grad=False,
#         backward_hooks=None,
#     )

# model = torch.load(model_path, map_location=lambda storage, loc: rebuild_storage(storage))
