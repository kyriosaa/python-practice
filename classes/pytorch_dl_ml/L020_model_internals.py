import L019_build_model
import torch

# Checking the contents of our PyTorch model

# Now that we've created a model, let's see what's inside...
# We can check using .parameters()

# Create random seed
torch.manual_seed(42) 

# Create an instance of the model (this is a subclass of nn.Module)
model_0 = LinearRegressionModel()