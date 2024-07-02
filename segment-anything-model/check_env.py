import torch

print("CUDA is available: " + str(torch.cuda.is_available()))
print("Number of devices: " + str(torch.cuda.device_count()))
print("Current device: " + str(torch.cuda.current_device()))
print("Active device: " + str(torch.cuda.device(0)))
print("Device name: " + str(torch.cuda.get_device_name(0)))