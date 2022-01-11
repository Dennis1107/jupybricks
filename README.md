:warning: PACKAGE IN DEVELOPMENT. No stable version yet.

<img src="docs/assets/logo.PNG" width=70% height=70%>
 

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->

 

![GitHub contributors](https://img.shields.io/github/contributors/ALIHAMA/kZB_KI_Structural_Breaks)

 

`Jupybricks` is a `python package` that allows `databricks developers` to switch easily between `local development in jupyter notebooks` and `databricks notebooks`. 

# What `Jupybricks` does
* convert databricks .py files into jupyter notebooks to work on your local machine
* convert local jupyter notebooks to .py files which can be read by databricks notebooks
 
By using Jupybricks you can benefit from your local IDE and in addition save databricks costs. No more manual refactoring needed if you want to deploy notebooks from you local machine to databricks (and back).
 

# Software Architecture
<img src="docs/assets/architecture.PNG" width=100% height=70%>

databricks saves python notebooks in a specific format as `.py files`. Usually these files are tracked via a git repository. In the past there was always a manual refactoring necessary if you want to work transform these .py files into jupyter notebooks and back. Jupybricks helps as it `translates the databricks.py files` into normal `jupyter notebooks`. In addition it can also `transform the jupyter notebook back into a runnig .py file` which has the format which is understood by databricks.

 

# Prerequisites & Installation
:warning: PACKAGE IN DEVELOPMENT. No stable version yet. See next steps at the bottom.

```
pip install dist/jupybricks-0.2.0-py3-none-any.whl --force-reinstall
```

Tested only on windows with anaconda and python > 3.8
 

# Using `Jupybricks` 

Jupybricks is a command line tool can be used. More information with:
```
jupybricks --help
```

## For single file conversion:

Transforming databricks .py file to jupyter .ipynb:
```
jupybricks databricks-to-jupyter --input-filename <example_files/databricks_example.py> --output-filename <example_files/jupyter_example.ipynb>
```
Transforming jupyter .ipynb file to databricks .py file
```
jupybricks jupyter-to-databricks --input-filename <example_files/jupyter_example.ipynb> --output-filename <example_files/databricks_example.py>
```

## For multiple files:
:warning: it is necessary to have a file named convert_list.json in your root folder from where you call jupybricks. Jupybricks uses this file in order to know which files are used for mapping .py files with the corresponding .ipynb files.
As an example. 
```
{
    "example_files/jupyter_example.ipynb" : "example_files/databricks_example.py"    
}
```

If you have the convert_list.json properly set up then you can run the cli commands without paramets:
```
jupybricks databricks-to-jupyter
```
```
jupybricks jupyter-to-databricks
```

# Next Steps
Feel free to reach out to give advice or feature requests.
Planned next steps:
- [ ] adding unit tests
- [ ] adding mkdocs documentation
- [ ] testing on different OS
- [ ] heavy testing on different kind of databricks formats
- [ ] Github Actions & pre commit hooks
- [ ] installable version over pip

**Developers:**

[Dennis Hartel](https://github.com/Dennis1107) 💻
 
