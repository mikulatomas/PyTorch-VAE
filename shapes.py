from torch.utils.data.dataset import Dataset
from glob import glob
from PIL import Image
import random


class Shapes(Dataset):
    def __init__(self, root, split, transform=None):
        self.root = root
        self.transform = transform
        self.image_list = tuple(glob(os.path.join(self.root, '*', '*.png')))
        self.split = split

        random.shuffle(self.image_list)

    def __getitem__(self, index):
        if self.split == 'test':
            index += (len(self.image_list) // 0.8) - 1

        path = self.image_list[index]
        # dummy label
        label = 0

        image = Image.open(path)

        if self.transform:
            image = self.transform(image)

        return image, label_id

    def __len__(self):
        if self.split == 'train':
            return len(self.image_list) // 0.8
        else:
            return len(self.image_list) - (len(self.image_list) // 0.8)
