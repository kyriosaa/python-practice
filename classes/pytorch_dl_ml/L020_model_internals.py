import L019_build_model

# PyTorch model building essentials
#
# torch.nn - Contains all of the building components for computational graphs (a neural network can be considered as this).
# torch.nn.Parameter - What parameters should our model try and learn, often a PyTorch layer from torch.nn will set these for us.
# torch.nn.Module - The base class for all neural network modules, if you subclass it, you should overwrite forward().
# torch.optim - This is where the optimizers in PyTorch live, they will help with gradient descent.
# def forward() - All nn.Module subclasses require you to overwrite forward(). This method defines what happens in the forward computation.

