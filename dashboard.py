"""
A.C.R.O.N.Y.M. Dashboard Code using Dash
Author: Trevor Zobrist
Last Updated: 8/29/23

I/O:
Input - GPT API Key
Input - GPT Model
Input - Prompt/File to scan
Input - Size of prompt
Output - Audit of input code/file
"""

import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from gpt import generate_response

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]
app = dash.Dash(
    __name__,
    external_scripts=external_script,
)
app.scripts.config.serve_locally = True


app.layout = html.Div([
    html.H1(children="A.C.R.O.N.Y.M.", title="Autonomous Context-aware Refactoring Of the Name for Your Material",
            className="py-3 ml-5 text-4xl font-mono-bold text-black hover:text-green-700"),

    html.Div([
        html.Form([
            html.Div([
                html.Label(htmlFor="api-key", children="API Key", title="Key used to access GPT API",
                           className="mb-1 block text-sm font-medium text-black after:ml-0.5 after:text-red-500 after:content-['*']"),
                dcc.Input(id="api-key", type="text", placeholder="API Key",
                          className="block w-full rounded-md border-green-800 shadow-sm focus:border-green-300 focus:ring focus:ring-green-200 focus:ring-opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-500"),
            ]),

            html.Div([
                html.Label(htmlFor="gpt-model", children="GPT Model", title="Model to use for GPT query",
                           className="mb-1 block text-sm font-medium text-black after:ml-0.5 after:text-red-500 after:content-['*']"),
                dcc.Dropdown(
                    id="gpt-model",
                    options=[
                        {"label": "gpt-3.5-turbo (recommended)", "value": "gpt-3.5-turbo"},
                        {"label": "gpt-3.5-turbo-16k", "value": "gpt-3.5-turbo-16k"},
                        {"label": "gpt-4", "value": "gpt-4"},
                        {"label": "gpt-4-32k", "value": "gpt-4-32k"}
                    ],
                    placeholder="gpt-3.5-turbo", value='gpt-3.5-turbo',
                    className="block w-full rounded-md border-green-800 shadow-sm focus:border-green-300 focus:ring focus:ring-green-200 focus:ring-opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-500"
                ),
            ]),

            html.Div([
                html.Label(htmlFor="prompt-size", children="Prompt Size (max tokens)",
                           title="Maximum number of tokens to query with",
                           className="mb-1 block text-sm font-medium text-black after:ml-0.5 after:text-red-500 after:content-['*']"),
                dcc.Input(id="prompt-size", type="number", value=1300, placeholder="1300",
                          className="block w-full rounded-md border-green-800 shadow-sm focus:border-green-300 focus:ring focus:ring-green-200 focus:ring-opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-500"),
            ]),

            html.Div([
                html.Label(htmlFor="acronym-num", children="Number of Acronyms", title="Number of acronyms to output",
                           className="mb-1 block text-sm font-medium text-black after:ml-0.5 after:text-red-500 after:content-['*']"),
                dcc.Input(id="acronym-num", type="number", value=10, placeholder="10",
                          className="block w-full rounded-md border-green-800 shadow-sm focus:border-green-300 focus:ring focus:ring-green-200 focus:ring-opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-500"),
            ]),

            html.Div([
                html.Label(htmlFor="input-text", children="Abstract or other text source",
                           title="Source to generate acronyms from",
                           className="mb-1 block text-sm font-medium text-black after:ml-0.5 after:text-red-500 after:content-['*']"),
                dcc.Textarea(id="input-text", value="", rows="10", placeholder="Enter text here...",
                             className="block w-full rounded-md border-green-800 shadow-sm focus:border-green-300 focus:ring focus:ring-green-200 focus:ring-opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-500"),
            ]),

            html.Div([
                html.Button(children="GENERATE ACRONYMS", type="button", id="gen-button", n_clicks=0,
                            className="rounded-lg border border-primary-100 bg-green-700 px-20 py-2.5 text-center text-sm font-medium text-white transition-all hover:bg-green-500 hover:border-primary-200 focus:ring focus:ring-primary-50 disabled:border-primary-50 disabled:bg-primary-50 disabled:text-primary-400"),
            ], className="flex flex-col items-center"),
        ], className="space-y-3"),
    ], className="mx-auto max-w-xl"),

    html.Div([
        html.Label(htmlFor="output-text", children="A.C.R.O.N.Y.M. Output",
                   className="mb-1 block text-sm font-medium text-black"),
        dcc.Textarea(id="output-text", value="", rows="15", readOnly=True,
                     className="block w-full rounded-md border-green-800 shadow-sm focus:border-green-300 focus:ring focus:ring-green-200 focus:ring-opacity-50 disabled:cursor-not-allowed disabled:bg-gray-50 disabled:text-gray-500"),
    ], className="py-5 mx-auto max-w-4xl")
], className="bg-gray-200 bg-cover")


@app.callback(
    Output("output-text", "value"),
    Input("gen-button", "n_clicks"),
    State("api-key", "value"),
    State("acronym-num", "value"),
    State("input-text", "value"),
    State("gpt-model", "value"),
    State("prompt-size", "value")
)
def scan(n_clicks, api_key, choices, prompt, engine, tokens):
    if n_clicks > 0:
        result = generate_response(api_key, prompt, choices, engine, tokens)
        return result
    return ""


if __name__ == "__main__":
    app.run_server(debug=True)
