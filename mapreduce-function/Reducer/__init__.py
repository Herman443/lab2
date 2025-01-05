def main(reduce_input: tuple) -> tuple:
    word, counts = reduce_input
    return word, sum(counts)
