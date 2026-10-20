"""Square a number."""


def square(n: float) -> float:
    """Return n multiplied by itself."""
    return n * n


def main() -> None:
    raw = input("Enter a number: ")
    try:
        number = float(raw)
    except ValueError:
        print(f"'{raw}' is not a valid number.")
        return

    result = square(number)
    # Show whole numbers without a trailing ".0"
    if result.is_integer():
        result = int(result)
    print(f"{raw} squared is {result}")


if __name__ == "__main__":
    main()
