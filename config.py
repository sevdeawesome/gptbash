from types import SimpleNamespace



default_config = SimpleNamespace(

    chat_temperature=0.3,
    max_fallback_retries=1,
    model_name="gpt-4",
    user_prompt_1 = """     """,
    user_prompt_2=""""     """,
    system_prompt = """    """,
    system_prompt_commands = """"""

    # eval_model="gpt-3.5-turbo",
    # eval_artifact="darek/llmapps/generated_examples:v0",
)