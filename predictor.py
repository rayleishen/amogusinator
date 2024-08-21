import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import random_split, Dataset, DataLoader
import torchvision.transforms as transforms
from torchvision import models, transforms
from torchvision.datasets import ImageFolder 
from PIL import Image

class ResNet(nn.Module):
    def __init__(self,num_classes):
        super(ResNet, self).__init__()
        self.name = "resnetclassifier"

        # Load the pre-trained ResNet model
        resnet = models.resnet152(weights=models.ResNet152_Weights.IMAGENET1K_V1)

        # Replace the last fully connected layer
        num_features = resnet.fc.in_features
        self.features = nn.Sequential(*list(resnet.children())[:-1])
        self.classifier = nn.Sequential(
            nn.Linear(num_features,num_classes),
            # nn.Softmax(dim=1)  #single label 
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x


num_classes = 17
use_cuda = False
resnetclassifier = ResNet(num_classes)

if use_cuda and torch.cuda.is_available():
    device = torch.device("cuda")
    resnetclassifier.cuda()
else:
    device = torch.device("cpu")

# Load in the model checkpoint
state = torch.load(r"C:\Users\Ricky\Desktop\Amongusinator\model_resnetclassifier_bs4_lr0.0001_dr0.5_epoch4", map_location=device)
state = {k.replace('module.', ''): v for k, v in state.items()}
resnetclassifier.load_state_dict(state)
resnetclassifier.eval()

# Load in a single image to perform the prediction on
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

image_path = str(input("Enter complete image path here (eg: images\test_images\align_engine_output\20240814205724_1.jpg): "))
image = Image.open(image_path).convert('RGB')
input_img = transform(image).unsqueeze(0)


# Make the prediction
output = resnetclassifier(input_img)

# Convert the tensor to a NumPy array for formatting
output_np = output.cpu().detach().numpy()

# Define the 17 possible classes
classes = ['align_engine_output', 'calibrate_distributor', 'chart_course', 'clean_o2_filter', 'clean_vent', 'clear_asteroids', 'divert_power', 'empty_garbage', 'fix_wiring', 'fuel_engines', 'inspect_sample', 'prime_shields', 'stabilize_steering', 'start_reactor', 'swipe_card', 'unlock_manifolds', 'upload_data']

for i, probabilities in enumerate(output_np):
    print("The following is the model's confidence on the task in the photo: ")
    for j, probability in enumerate(probabilities):
        print("  {}: {:.2%}".format(classes[j], probability))

threshold = 0.5
output = output.detach().cpu()
best = (output >= threshold).int()
predicted_index = best.squeeze().nonzero().flatten().tolist()
predicted_task = [classes[i] for i in predicted_index]

print(predicted_task)