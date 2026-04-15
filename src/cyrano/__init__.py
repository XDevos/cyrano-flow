from importlib.metadata import version


def main() -> None:
    print("Hello from cyrano!")
    print(version("cyrano"))
