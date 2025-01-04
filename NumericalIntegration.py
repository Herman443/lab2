import math


def numerical_integration(lower, upper, N):
    dx = (upper - lower) / N
    total_area = 0.0
    for i in range(N):
        x = lower + i * dx
        total_area += abs(math.sin(x)) * dx
    return total_area


if __name__ == "__main__":
    lower = 0
    upper = math.pi
    for N in [10, 100, 1000, 10000, 100000, 1000000]:
        result = numerical_integration(lower, upper, N)
        print(f"N={N}, Result={result}")
