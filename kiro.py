import os
from openai import OpenAI

class Agent:
    def __init__(self, context_file):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        with open(context_file, 'r') as f:
            self.context = f.read()

    def run(self, query):
        prompt = f"Context: {self.context}\n\nQuestion: {query}\n\nAnswer based on the context provided:"
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful local guide for Delhi."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Sorry, I couldn't process your request. Error: {str(e)}"