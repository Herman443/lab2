import azure.durable_functions as df
import azure.functions as func
import json


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new("MasterOrchestrator", None)

    # Wait for orchestration to complete
    results = await client.wait_for_completion_or_create_check_status_response(
        req, instance_id
    )
    if results.runtime_status == "Completed":
        return func.HttpResponse(
            json.dumps(results.output), mimetype="application/json", status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Orchestration did not complete in time."}),
            mimetype="application/json",
            status_code=504,
        )
