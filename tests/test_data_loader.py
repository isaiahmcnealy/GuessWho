import unittest
from torch.utils.data import DataLoader
from src.data.data_loader import get_celeba_dataloader

class TestCelebADataLoader(unittest.TestCase):

    def test_get_celeba_dataloader(self):
        # Test if the function returns a DataLoader
        dataloader = get_celeba_dataloader(batch_size=32, num_workers=2, split='train')
        self.assertIsInstance(dataloader, DataLoader)

        # Test if the DataLoader returns the correct batch size
        batch_size = 32
        for batch_idx, (images, labels) in enumerate(dataloader):
            self.assertEqual(images.shape[0], batch_size)
            break  # Test only the first batch

        # Test if the DataLoader returns images with the correct shape
        expected_image_shape = (3, 64, 64)  # (channels, height, width)
        for batch_idx, (images, labels) in enumerate(dataloader):
            self.assertEqual(images.shape[1:], expected_image_shape)
            break  # Test only the first batch

if __name__ == '__main__':
    unittest.main()