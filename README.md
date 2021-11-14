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

 

# Prerequisites 

Before you begin, ensure you have met the following requirements:

<!--- These are just example requirements. Add, duplicate or remove as required --->

* You have installed the latest version of `<coding_language/dependency/requirement_1>`

* You have read `<guide/link/documentation_related_to_project>`.

 

# Using `Jupybricks` 

Jupybricks can be used via the command line:

## For single file conversion:
```
python manage.py databricks-to-jupyter --input-filename <pythonfile.py> --output-filename <jupyterfile.ipynb>
```
```
python manage.py jupyter-to-databricks --input-filename <jupyterfile.ipynb> --output-filename <pythonfile.py>
```

## For multiple files:
:warning: it is necessary to have a file named convert_list.json in your root folder. Jupybricks uses this file in order to know which files are used for mapping .py files with the corresponding .ipynb files
As an example. 
```
{
    "jupyter_example.ipynb" : "databricks_example.py"    
}
```

If you have the convert_list.json properly set up then you can run the cli commands without paramets:
```
python manage.py databricks-to-jupyter
```
```
python manage.py jupyter-to-databricks
```


**Developers:**

* [Dennis Hartel](https://github.com/Dennis1107) 💻
 
