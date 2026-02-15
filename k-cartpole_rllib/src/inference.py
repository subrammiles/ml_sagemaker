import torch
import torch.nn as nn
import json
import io
from PIL import Image
import torchvision.transforms as transforms

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Flatten(),
            nn.Linear(64 * 8 * 8, 256),
            nn.ReLU(),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        return self.net(x)


def model_fn(model_dir):
    model = SimpleCNN()
    model.load_state_dict(
        torch.load(f"{model_dir}/model.pth",
                   map_location="cpu")
    )
    model.eval()
    return model


def input_fn(request_body, content_type):
    image = Image.open(io.BytesIO(request_body)).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    return transform(image).unsqueeze(0)


def predict_fn(input_data, model):
    with torch.no_grad():
        outputs = model(input_data)
        return torch.argmax(outputs, dim=1).item()


def output_fn(prediction, accept):
    return json.dumps({"class": int(prediction)})
