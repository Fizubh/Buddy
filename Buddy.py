import os
import requests

from groq import Groq

groq_api_key = os.environ.get("GROQ_API_KEY")


def main():
    for model in groq_models().split():
        print(model)
    name = input("Choose Model: ")
    groq_loader(model_name=name)
    

def groq_loader(model_name: str):
    if model_name not in groq_models():
        print(f"Cannot find model: {model_name}")
        return

    client = Groq(api_key=groq_api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain how to write a window in Python",
            }
        ],
        model=model_name,
    )

    print(chat_completion.choices[0].message.content)


def groq_models():
    url = "https://api.groq.com/openai/v1/models"

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers).json()
    output = ""
    for data in response["data"]:
        #print(data["id"])
        output += data["id"] + " "        
    return output        


if __name__ == "__main__":
    main()