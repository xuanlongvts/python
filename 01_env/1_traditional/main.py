import os
import click
from dotenv import load_dotenv

@click.command()
@click.option(
    '--env',
    type=click.Choice(['dev', 'qc', 'production'], case_sensitive=False),
    default='dev',
    help='Runtime environment.'
)

def main(env):
    load_dotenv(f".env.{env}")
    click.echo(f"Running in {env.upper()} mode")
    getDb = os.getenv("DB")
    print(f"---------> getDb: {getDb}")

if __name__ == '__main__':
    main()