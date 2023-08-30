"""
Verifeye Dashboard Code using Dash
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

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Verifeye", className="header"),

    html.Div([
        html.Div([
            html.Label("API Key"),
            dcc.Input(id="api-key", type="text", placeholder="API Key")
        ], className="field"),

        html.Div([
            html.Label("GPT Model"),
            dcc.Dropdown(
                id="gpt-model",
                options=[
                    {"label": "davinci", "value": "davinci"},
                    {"label": "curie", "value": "curie"},
                    {"label": "babbage", "value": "babbage"},
                    {"label": "text-davinci-003", "value": "text-davinci-003"},
                    {"label": "davinci-codex", "value": "davinci-codex"},
                ],
                placeholder="GPT Model"
            ),
        ], className="field"),

        html.Div([
            html.Label("Prompt Size (tokens):"),
            dcc.Input(id="prompt-size", type="number", placeholder="Prompt size"),
        ], className="field"),

        html.Div([
            html.Label("Input:"),
            dcc.Textarea(id="input-text", placeholder="Data to scan", value=""),
        ], className="field"),

        html.Button("SCAN", id="scan-button", n_clicks=0),
    ], className="input-container"),

    html.Div([
        html.Label("Output"),
        dcc.Textarea(id="output-text", value="", readOnly=True)
    ], className="output-container"),

    html.Div([
        dcc.Upload(
            id="upload-data",
            children=html.Div([
                html.A("Drag and Drop or "),
                html.Button("UPLOAD", id="upload-button")
            ]),
            multiple=True
        ),
    ], className="file-upload-container")
])

@app.callback(
    Output("output-text", "value"),
    Input("scan-button", "n_clicks"),
    State("api-key", "value"),
    State("input-text", "value"),
    State("gpt-model", "value"),
    State("prompt-size", "value")
)
def scan(n_clicks, api_key, prompt, engine, tokens):
    if n_clicks > 0:
        result = generate_response(api_key, prompt, engine, tokens)
        return result
    return ""

if __name__ == "__main__":
    app.run_server(debug=True)
