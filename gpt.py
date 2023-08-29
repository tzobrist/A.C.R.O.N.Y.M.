"""
Basic program to access GPT Playground through OpenAI API
Author: Trevor Zobrist
Last Modified: 8/29/23

I/O:
Input - Prompt
Input - Model
Input - Token length
Output - GPT Response
"""

import openai
"""
GPT Engine Values

davinci: The default engine, provides general-purpose text generation.

curie: Designed for tasks that require more straightforward language and concise answers.

babbage: Intended for tasks that involve instructive prompts.

text-davinci-003: An older version of the davinci engine.

davinci-codex: A specific engine designed for code-related tasks and generation.
"""

# TODO: Connect gpt program to dashboard
def generate_response(key, prompt, engine = "davinci-codex", tokens = 150):
    openai.api_key = str(key)
    response = openai.Completion.create(
        engine=engine,  # GPT Model
        prompt=prompt,  # Text prompt
        max_tokens=tokens  # Prompt size in tokens
    )
    return response.choices[0].text.strip()


def main():
    prompt = str(input("Prompt: "))
    response = generate_response(prompt)
    print("Response:", response)


if __name__ == "__main__":
    main()
