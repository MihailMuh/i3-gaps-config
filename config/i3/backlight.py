import sys


def main() -> None:
    change_brightness(1 if sys.argv[1] == "up" else -1, sys.argv[2])


def change_brightness(scalar: int, card: str) -> None:
    with open(f"/sys/class/backlight/{card}/max_brightness") as file:
        max_brightness: int = int(file.readline())

    with open(f"/sys/class/backlight/{card}/brightness", "r+") as file:
        current_brightness: int = int(file.readline())

        file.truncate(0)
        file.write(str(int(current_brightness + max_brightness * 0.05 * scalar)))


if __name__ == '__main__':
    main()
