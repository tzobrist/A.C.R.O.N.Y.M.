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

# OpenAI API key
openai.api_key = "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"

"""
GPT Engine Values

davinci: The default engine, provides general-purpose text generation.

curie: Designed for tasks that require more straightforward language and concise answers.

babbage: Intended for tasks that involve instructive prompts.

text-davinci-003: An older version of the davinci engine.

davinci-codex: A specific engine designed for code-related tasks and generation.
"""

# TODO: Connect gpt program to dashboard
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT Model
        prompt=prompt,  # Text prompt
        max_tokens=150  # Prompt size in tokens
    )
    return response.choices[0].text.strip()


def main():
    prompt = str(input("Prompt: "))
    response = generate_response(prompt)
    print("Response:", response)


if __name__ == "__main__":
    main()
