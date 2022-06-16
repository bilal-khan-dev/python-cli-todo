"""App Entry point"""
# mylib/__main__.py


from mylib import cli, __app_name__
import typer


def main():
    cli.app()
    print(typer.get_app_dir(__app_name__))


if __name__ == "__main__":
    main()
