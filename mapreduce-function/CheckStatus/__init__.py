import azure.durable_functions as df
import azure.functions as func
import json


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    instance_id = req.route_params.get("instanceId")
    if not instance_id:
        return func.HttpResponse(
            json.dumps({"error": "Instance ID is required"}),
            mimetype="application/json",
            status_code=400,
        )

    client = df.DurableOrchestrationClient(starter)
    status = await client.get_status(instance_id)

    if status:
        return func.HttpResponse(
            json.dumps(status.to_json()),
            mimetype="application/json",
            status_code=200,
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": f"No instance found with ID '{instance_id}'"}),
            mimetype="application/json",
            status_code=404,
        )
