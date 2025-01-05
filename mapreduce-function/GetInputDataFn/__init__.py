from azure.storage.blob import BlobServiceClient


def main(_) -> list:
    connection_string = "string_goes_here"
    container_name = "input-data"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    input_data = []
    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob)
        lines = blob_client.download_blob().readall().decode("utf-8").splitlines()
        input_data.extend(lines)

    return [(i, line) for i, line in enumerate(input_data)]
