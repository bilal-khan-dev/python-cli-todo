"""App Entry point"""
# mylib/__main__.py

from mylib import cli, __app_name__
import typer

def main():
    cli.app()


if __name__ == "__main__":
    main()