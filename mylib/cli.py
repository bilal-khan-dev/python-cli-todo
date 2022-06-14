"""This module provides name and version to mytodo CLI"""
# mylib/cli.py


from typing import Optional
from mylib import __app_name__, __version__

import typer


app = typer.Typer()


def _version_callback(value: bool) -> None:
    """
    Display app name, version and exit
    """
    if value:
        typer.echo(f"Our awesome {__app_name__} CLI app with version {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Display application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    """
    Our awesome mytodo CLI app
    """
    return
