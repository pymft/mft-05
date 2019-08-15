class Sample:
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with Sample() as f:
    pass
