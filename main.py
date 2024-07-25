from src.data.data_loader import get_celeba_dataloader

def main():
    get_celeba_dataloader(32, 2, 'train')


if __name__ == "__main__":
    main()