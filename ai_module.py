from dotenv import load_dotenv
from mistralai import Mistral
import os


def generate_ai_feedback(code_content):
    """
    Generates AI-driven feedback on a block of code using the new Mistral AI API.
    """
    try:
        load_dotenv()
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key:
            raise ValueError("Mistral AI API key not found. Please set it in your .env file.")

        # New client
        client = Mistral(api_key=api_key)

        prompt = f"As a senior software engineer, please review the following Python code for bugs, security issues, and style violations. Provide a detailed report and suggest fixes.\n\nCode to review:\n```python\n{code_content}\n```"

        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error during AI review: {e}"
