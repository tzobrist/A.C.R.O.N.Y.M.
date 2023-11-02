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
from thesarus import find_keyword_synonyms
"""
GPT Engine Values

davinci: The default engine, provides general-purpose text generation.

curie: Designed for tasks that require more straightforward language and concise answers.

babbage: Intended for tasks that involve instructive prompts.

text-davinci-003: An older version of the davinci engine.

davinci-codex: A specific engine designed for code-related tasks and generation.
"""


def generate_response(key, prompt_query, choices=10, engine="gpt-3.5-turbo", tokens=500):
    # Find relevant synonyms to aid acronym generation
    synonyms = find_keyword_synonyms(prompt_query)

    # GPT query
    openai.api_key = str(key)
    prompt = f'Act has a highly sophisticated natural language processing program. I am going to give you the' \
             f' abstract for a technical research paper that I need to come up with a title for.' \
             f' The title should be an acronym and this acronym should be a valid english word. Commonly, the leading' \
             f' letter for every word in the title should correspond to a letter in the acronym word, but some words can be' \
             f' excluded to make grammatical sense. Or, a word may have multiple letters that correspond to the acronym.' \
             f' Display {str(choices)} relevant acronyms using the following abstract and display them in list format.' \
             f' The abstract is as follows "{prompt_query}" On top of the abstract here are synonyms of keywords, seperated by commas,' \
             f' from within the abstract that can also be used to supplement acronym generation: "{synonyms}"'
    response = openai.ChatCompletion.create(
        model=engine,  # GPT Model
        messages=[{  # Text prompt
            "role": "user",
            "content": prompt
        }],
        max_tokens=tokens  # Prompt size in tokens
    )
    prompt_tokens = response.usage.prompt_tokens
    model_tokens = response.usage.completion_tokens

    # Print usage and debug
    print(f"Prompt Tokens: {prompt_tokens}, Completion Tokens: {model_tokens}")
    print(f"_prompt_query: {prompt_query}")
    print(f"_synonyms: {synonyms}")

    print(f"_output: {response.choices[0].message.content.strip()}")
    return response.choices[0].message.content.strip()


def main():
    prompt = str(input("Prompt: "))
    response = generate_response(prompt)
    print("Response:", response)


if __name__ == "__main__":
    main()
