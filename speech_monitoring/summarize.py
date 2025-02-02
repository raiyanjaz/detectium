from openai import OpenAI

def summarize_text(text):
    client = OpenAI(
        api_key="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" 
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


