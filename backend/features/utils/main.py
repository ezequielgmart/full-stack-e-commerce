

def format_dict_to_pydancti_model(pydantic_model, data:list[dict]) -> list[dict]: 

    result: list = [pydantic_model(**item) for item in data]

    return result