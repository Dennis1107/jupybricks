import jupytext
import json
import os

f = open(
    "src/convert_list.json",
)
files = json.load(f)

skip_lines = ["# Databricks notebook source\n", "\n"]

for file in files:
    try:
        # Open the python file and read lines
        with open(files[file], "r") as f:
            lines = f.readlines()

        # filter out specific databricks lines
        filtered_lines = [line for line in lines if line not in skip_lines]
        # replace the databricks command for new cell with line break which is for jupyter
        processed_lines = [
            "\n" if line == "# COMMAND ----------\n" else line
            for line in filtered_lines
        ]

        if processed_lines[0] == "\n":
            processed_lines.pop(0)

        # Open temp python file to write into filtered lines
        with open("temp_file348234283o23478234ip.py", "w") as f:
            for line in processed_lines:
                f.write(line)

        # Write to notebook
        notebook = jupytext.read("temp_file348234283o23478234ip.py")
        jupytext.write(notebook, "result_tojupyter.ipynb")

        # Remove temp file
        os.remove("temp_file348234283o23478234ip.py")

    except Exception as e:
        print(e)
