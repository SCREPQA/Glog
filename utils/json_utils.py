import json

def format_json(text):
    try:
        parsed_json = json.loads(text)
        return json.dumps(parsed_json, indent=4, ensure_ascii=False)
    except json.JSONDecodeError:
        return text