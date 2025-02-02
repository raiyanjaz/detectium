from openai import OpenAI

def summarize_text(text):
    client = OpenAI(
        api_key="API-KEY" 
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Summarize the following: {text}"}
        ]
    )
    summary = completion.choices[0].message.content

    print('CHATGPT SUMMARY: ', summary)
    return summary 


