from azure.identity import AzureCliCredential
import os

os.environ["AZURE_CLI_OUTPUT"] = "json"
credential = AzureCliCredential()
token = credential.get_token("https://management.azure.com/.default")  # 尝试获取 Token
print(token.token)  # 如果成功，会打印 Token