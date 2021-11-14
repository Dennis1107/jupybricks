import typer
from . import function_databricks_to_jupyter, function_jupyter_to_databricks

app = typer.Typer()


@app.command()
def databricks_to_jupyter(
    input_filename: str = "nofile", output_filename: str = "nofile"
):
    return_value = function_databricks_to_jupyter.convert_databricks_to_jupyter(
        input_filename, output_filename
    )
    if return_value:
        typer.echo(f"Successfully formatted to Jupyter \U0001F680")
    else:
        typer.echo(f"Formatting failed")


@app.command()
def jupyter_to_databricks(
    input_filename: str = "nofile", output_filename: str = "nofile"
):
    return_value = function_jupyter_to_databricks.convert_jupyter_to_databricks(
        input_filename, output_filename
    )
    if return_value:
        typer.echo(f"Successfully formatted to databricks \U0001F680")
    else:
        typer.echo(f"Formatting failed")


if __name__ == "__main__":
    app()
