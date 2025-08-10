from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

ml_client = MLClient(
    DefaultAzureCredential(),
    "<subscription-id>",
    "<resource-group>",
    "<workspace-name>"
)
print("Connected to:", ml_client.workspace_name)
