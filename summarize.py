import openai

# Set up your OpenAI API key
OPENAI_API_KEY = "your_api_key_here"

def summarize_text(text):
    """Sends a request to ChatGPT API to summarize the given text."""
    prompt = f"Summarize the following: {text}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if you want a cheaper option
            messages=[{"role": "system", "content": "You are a helpful assistant that summarizes text."},
                      {"role": "user", "content": prompt}],
            max_tokens=150
        )
        
        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        return f"Error: {e}"

# Example input text
text_to_summarize = "Artificial Intelligence (AI) is transforming various industries by automating tasks, analyzing large datasets, and improving efficiency. It is used in healthcare, finance, autonomous vehicles, and more."

# Get summary and store it in the history variable
history = summarize_text(text_to_summarize)

# Print the summary
print("\nSummarized Text:\n", history)
