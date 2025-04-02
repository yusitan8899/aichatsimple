from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.inference.prompts import PromptTemplate

project_connection_string = "eastus2.api.azureml.ms;818bbad7-04cb-4b7f-b578-031525f747dd;ODL-sandbox-1664952-02;AP-Explore_Al_Agent"
project = AIProjectClient.from_connection_string(
    conn_str=project_connection_string, credential=DefaultAzureCredential(ExcludeEnvironmentCredential = True)
)

chat = project.inference.get_chat_completions_client()
# response = chat.complete(
#     model="gpt-4o-mini",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are an AI assistant that speaks like a techno punk rocker from 2350. Be cool but not too cool. Ya dig?",
#         },
#         {"role": "user", "content": "Hey, can you help me with my taxes? I'm a freelancer."},
#     ],
# )

def get_chat_response(messages, context):
    # create a prompt template from an inline string (using mustache syntax)
    prompt_template = PromptTemplate.from_string(
        prompt_template="""
        system:
        You are an AI assistant that speaks like a techno punk rocker from 2350. Be cool but not too cool. Ya dig? Refer to the user by their first name, try to work their last name into a pun.Reply in Chinese.

        The user's first name is {{first_name}} and their last name is {{last_name}}.
        """
    )

    # generate system message from the template, passing in the context as variables
    system_message = prompt_template.create_messages(data=context)

    # add the prompt messages to the user messages
    return chat.complete(
        model="gpt-4o-mini",
        messages=system_message + messages,
        temperature=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )

if __name__ == "__main__":
    response = get_chat_response(
        messages=[{"role": "user", "content": "世界上哪个城市能获得最好的旅游体验?"}],
        context={"first_name": "Jessie", "last_name": "Irwin"},
    )
    print(response.choices[0].message.content)