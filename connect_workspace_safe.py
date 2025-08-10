# src/connect_safe.py
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# Fill in if you DO have access; otherwise this will fail gracefully.
SUBSCRIPTION_ID = "<subscription-id>"
RESOURCE_GROUP  = "<resource-group>"
WORKSPACE_NAME  = "<workspace-name>"

try:
    ml_client = MLClient(
        DefaultAzureCredential(),
        SUBSCRIPTION_ID,
        RESOURCE_GROUP,
        WORKSPACE_NAME
    )
    print("Connected to workspace:", ml_client.workspace_name)
    # Try listing computes (if permitted)
    for c in ml_client.compute.list():
        print("Compute:", c.name, "-", c.type)
except Exception as e:
    print("No Azure workspace connection available (this is OK for now):", e)

#Azure ML v2 SDK (azure-ai-ml) is installed and working

#Local Python code runs fine in VS Code

#Workspace connection attempt runs but fails authentication (expected for students without a configured Azure sign-in)

#We can give students offline/local examples they can run now, and later the same code can be submitted to Azure ML when their subscription/credentials are ready.