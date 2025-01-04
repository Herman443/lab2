import math
import json
import azure.functions as func


def numerical_integration(lower, upper, N):
    """Perform numerical integration of |sin(x)| from lower to upper with N iterations."""
    dx = (upper - lower) / N
    total_area = sum(abs(math.sin(lower + i * dx)) * dx for i in range(N))
    return total_area


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Get 'lower' and 'upper' query parameters
        lower = float(req.params.get("lower", 0))
        upper = float(req.params.get("upper", math.pi))

        # Define the iteration steps
        iterations = [10, 100, 1000, 10000, 100000, 1000000]

        # Calculate results for all iterations
        results = {f"N={N}": numerical_integration(lower, upper, N) for N in iterations}

        # Return results as JSON response
        return func.HttpResponse(
            json.dumps(results), mimetype="application/json", status_code=200
        )

    except Exception as e:
        # Return an error response if something goes wrong
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
