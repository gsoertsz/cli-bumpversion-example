from datetime import datetime
from pydoc import describe
import click
import logging
import hello
from typing import List
from hello import logger
from hello.greeting import greeting as greeter
import uuid
import random
import json

from logging.handlers import RotatingFileHandler
import logging

def configure_logging_handlers(filename, debug=False) -> None:
    logger.addHandler(RotatingFileHandler(
        backupCount=1, maxBytes=1000000, filename=filename
    ))

    if debug:
        logger.addHandler(logging.StreamHandler())

    level = logging.DEBUG if debug else logging.INFO
    logger.setLevel(level)

@click.group()
@click.option("debug", "--debug", default=False, is_flag=True)
def main(debug):
    configure_logging_handlers(
        hello.LOG_FILENAME, debug)

@click.command()
@click.option("to_whom", "--to-whom", default=False, is_flag=False, required=True, type=str)
@click.option("greeting", "--greeting", default=False, is_flag=False, required=True, type=str)
def say_hello(to_whom: str, greeting: str) -> None:
    click.echo(message=greeter.generate(to_whom, greeting))

main.add_command(say_hello)

if __name__ == "__main__":
    main()