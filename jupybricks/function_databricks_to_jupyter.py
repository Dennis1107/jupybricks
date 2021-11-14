import jupytext
import json
import os

# import help_functions

# ----siblings import from help functions does not work with typer
def check_for_ending(filename: str, ending: str):
    if not filename.endswith(ending):
        raise ValueError(f"{filename} not valid. Should be a file with ending {ending}")
    return


def remove_temp_file(filename: str = "temp_file348234283o23478234ip.py"):
    os.remove(filename)
    return


# -----------------------------


def processing_lines(
    lines: list, skip_lines: list = ["# Databricks notebook source\n", "\n"]
):
    # filter out specific databricks lines
    filtered_lines = [line for line in lines if line not in skip_lines]
    # replace the databricks command for new cell with line break which is for jupyter
    processed_lines = [
        "\n" if line == "# COMMAND ----------\n" else line for line in filtered_lines
    ]
    if processed_lines[0] == "\n":
        processed_lines.pop(0)
    return processed_lines


def write_list_tofile(lines: list, filename: str = "temp_file348234283o23478234ip.py"):
    # Open temp python file to write into filtered lines
    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
    return


def write_to_jupyter(
    output_filename: str, input_filename: str = "temp_file348234283o23478234ip.py"
):
    notebook = jupytext.read(input_filename)
    jupytext.write(notebook, output_filename)
    return


def convert_databricks_to_jupyter(
    input_filename: str = "nofile", output_filename: str = "nofile"
):
    # Default use the convert_list.json
    if (input_filename == "nofile") & (output_filename == "nofile"):
        try:
            f = open(
                "convert_list.json",
            )
            files = json.load(f)
        except Exception as e:
            raise ValueError(
                f"Loading default list did not work. Make sure to create a convert_list.json: {e}"
            )
    else:
        check_for_ending(input_filename, ".py")
        check_for_ending(output_filename, ".ipynb")
        files = {output_filename: input_filename}

    for file in files:
        # Open the python file and read lines
        try:
            with open(files[file], "r") as f:
                lines = f.readlines()
        except Exception as e:
            raise ValueError(
                f"Failed to load file {files[file]}. Make sure this file exists: {e}"
            )

        # Processing lines
        try:
            processed_lines = processing_lines(lines)
        except Exception as e:
            raise ValueError(f"Processing lines accidentialy failed {e}")

        # Writing lines back
        try:
            # Open temp python file to write into filtered lines
            write_list_tofile(processed_lines)
            # Write to notebook
            write_to_jupyter(file)
            # Remove temp file
            remove_temp_file()
        except Exception as e:
            raise ValueError(f"Writing process failed {e}")
    return True
