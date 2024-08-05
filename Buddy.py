import os


from groq import Groq


def main():
    groq_loader()    
    

def groq_loader():    
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain how to write a window in Python",
            }
        ],
        model="llama3-8b-8192",
    )

    print(chat_completion.choices[0].message.content) 


if __name__ == "__main__":
    main()