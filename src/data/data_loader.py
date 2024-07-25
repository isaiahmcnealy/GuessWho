import torchvision.transforms as transforms
from torchvision.datasets import CelebA
from torch.utils.data import DataLoader


def get_celeba_dataloader(batch_size=32, num_workers=2, split='train'):
    """
    Returns a DataLoader for the CelebA dataset.

    Args:
        batch_size (int): Number of samples in a batch
        num_workers (int): Number of parallel processes to read data. Default is 2.
        split (str): The dataset split to use. ('train', 'valid', 'test'). Default is 'train'.
    """
    # Define transformations for the dataset
    transform = transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.CenterCrop(64),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
    ])

    # Load the CelebA dataset
    celeba_data = CelebA(
        root='./data',
        split=split,
        transform=transform,
        download=True
    )

    # Return a DataLoader
    data_loader = DataLoader(
        dataset=celeba_data,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers
    )

    return data_loader