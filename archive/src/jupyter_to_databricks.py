import nbconvert
import json
import os

f = open(
    "src/convert_list.json",
)
files = json.load(f)

exporter = nbconvert.exporters.get_exporter("python")

skip_lines = ["#!/usr/bin/env python\n", "# coding: utf-8\n", "\n"]

for file in files:
    try:
        # Get lines 
        jupyter_file = nbconvert.exporters.export(exporter=exporter, nb=file)[0]

        #Write to temp file
        with open("temp_file348234283o23478234ip.py", "w") as f:
            f.write(jupyter_file)

        #Read from temp file
        with open("temp_file348234283o23478234ip.py", "r") as f:
            lines = f.readlines()
        
        # Remove temp file
        os.remove("temp_file348234283o23478234ip.py")
        
        #open 
        with open("result_todatabricks.py", "w", encoding="utf8") as f:
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
    except Exception as e:
        print(e)
    