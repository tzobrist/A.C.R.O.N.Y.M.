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

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Verifeye", className="header"),
        html.Div([
            dcc.Input(id="api-key", type="text", placeholder="API Key"),
            dcc.Dropdown(
                id="gpt-model",
                options=[
                    {"label": "Option 1", "value": "option1"},
                    {"label": "Option 2", "value": "option2"},
                    {"label": "Option 3", "value": "option3"},
                ],
                placeholder="GPT Model"
            ),
            dcc.Input(id="prompt-size", type="number", placeholder="Prompt size"),
            html.Button("SCAN", id="scan-button", n_clicks=0),
            dcc.Textarea(id="output-text", value="", readOnly=True)
        ], className="input-container"),
    ], className="main-container"),

    html.Div([
        dcc.Upload(
            id="upload-data",
            children=html.Div([
                html.A("Drag and Drop or "),
                html.Button("UPLOAD", id="upload-button")
            ]),
            multiple=True
        ),
    ], className="file-upload-container"),
])


@app.callback(
    Output("output-text", "value"),
    Input("scan-button", "n_clicks"),
    State("api-key", "value"),
    State("gpt-model", "value"),
    State("prompt-size", "value")
)
def update_output_text(n_clicks, text1, text2, text3):
    if n_clicks > 0:
        result = f"Text 1: {text1}\nText 2: {text2}\nText 3: {text3}"
        return result
    return ""


if __name__ == "__main__":
    app.run_server(debug=True)
