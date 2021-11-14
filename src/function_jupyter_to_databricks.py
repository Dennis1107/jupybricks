import nbconvert
import json
#from src import help_functions
import os

#----siblings import from help functions does not work with typer
def check_for_ending(filename: str, ending: str):
    if not filename.endswith(ending):
        raise ValueError(f"{filename} not valid. Should be a file with ending {ending}")
    return

def remove_temp_file(filename: str = "temp_file348234283o23478234ip.py"):
    os.remove(filename)
    return
#-----------------------------------


def jupyterfile_tolist(
    file: str, temp_filename: str = "temp_file348234283o23478234ip.py"
):
    # Get lines
    exporter = nbconvert.exporters.get_exporter("python")
    jupyter_file = nbconvert.exporters.export(exporter=exporter, nb=file)[0]

    # Write to temp file
    with open(temp_filename, "w") as f:
        f.write(jupyter_file)

    # Read from temp file
    with open(temp_filename, "r") as f:
        lines = f.readlines()

    remove_temp_file(temp_filename)

    return lines


def write_topython(
    lines: list,
    output_filename: str,
    skip_lines: list = ["#!/usr/bin/env python\n", "# coding: utf-8\n", "\n"],
):
    # open
    with open(output_filename, "w", encoding="utf8") as f:
        # databricks needs to have the header at the top
        f.write("# Databricks notebook source\n")

        for line in lines:
            # Replace in future with better regex:
            if "# In[" in line:
                f.write("\n")
                f.write("# COMMAND ----------\n")
                f.write("\n")
            elif "# MAGIC %md" in line:
                f.write("# COMMAND ----------\n")
                f.write(line)
            elif line in skip_lines:
                pass
            else:
                f.write(line)
    return


def convert_jupyter_to_databricks(
    input_filename: str = "nofile", output_filename: str = "nofile"
):
    # Default use the convert_list.json
    if (input_filename == "nofile") & (output_filename == "nofile"):
        try:
            f = open(
                "src/convert_list.json",
            )
            files = json.load(f)
        except Exception as e:
            raise ValueError(
                f"Loading default list did not work. Make sure to create a convert_list.json: {e}"
            )
    else:
        check_for_ending(input_filename, ".ipynb")
        check_for_ending(output_filename, ".py")
        files = {input_filename: output_filename}

    for file in files:

        # Get Lines from jupyter
        try:
            lines = jupyterfile_tolist(file)
        except Exception as e:
            raise ValueError(
                f"Transforming jupyter file to python file did not work: {e}"
            )

        #write to Python file
        try:
            write_topython(lines, files[file])
        except Exception as e:
            raise ValueError(f"Saving to python file did not work: {e}")

    return True

