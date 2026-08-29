import cv2
import random
from pathlib import Path

SOURCE_DIR = Path(
    "/content/kaggle_dataset/colored_images/colored_images"
)

OUTPUT_DIR = Path("/content/DR_dataset")

CLASSES = [
    "No_DR",
    "Mild",
    "Moderate",
    "Severe"
]

IMG_SIZE = (224, 224)
TEST_SIZE = 0.20
RANDOM_SEED = 42

random.seed(RANDOM_SEED)
