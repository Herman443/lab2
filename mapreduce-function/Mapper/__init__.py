def main(input_pair: tuple) -> list:
    _, line = input_pair
    words = line.split()
    return [(word.lower(), 1) for word in words]
