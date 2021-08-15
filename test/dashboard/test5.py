# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_table
import pandas as pd
import re

df = pd.DataFrame(
    {
        "Version": ["Oct 1st 2016", "June 1st 2021"],
        "Nº entities": ["5765325", "7435957 (+1670632)"],
        "Nº types": ["418", "421 (-3)"],
    }
)

pattern = re.compile("(\(.*?)\)")


def color_brackets(value):
    found = re.search(pattern, value)

    if found:
        color = "red"

        if found.group()[1] == "+":
            color = "green"

        substituted = pattern.sub(
            f"<span style='background-color: {color};'>{found.group()}</span>", value
        )
        return substituted

    return value


df["Nº entities"] = df["Nº entities"].apply(color_brackets)
df["Nº types"] = df["Nº types"].apply(color_brackets)


app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dash_table.DataTable(
            css=[dict(selector="p", rule="margin: 0px; text-align: center")],
            style_cell={"textAlign": "center"},
            data=df.to_dict("records"),
            columns=[
                {"name": "Version", "id": "Version"},
                {
                    "name": "Nº entities",
                    "id": "Nº entities",
                    "presentation": "markdown",
                },
                {"name": "Nº types", "id": "Nº types", "presentation": "markdown"},
            ],
            markdown_options={"html": True},
        )
    ]
)

if __name__ == "__main__":
    app.run_server()

