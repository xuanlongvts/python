import os
import argparse
from dotenv import load_dotenv


def main():
    parse = argparse.ArgumentParser("Run app with specific environment.")
    parse.add_argument("--env", choices=["dev", "qc", "production"], default="dev", help="Specify the runtime environment (default: dev)")
    args = parse.parse_args()

    env_file = f".env.{args.env}"
    if os.path.exists(env_file):
        load_dotenv(env_file)
        print(f"Loaded configuration from {env_file}")
    else:
        print(f"Warning: {env_file} not found. Using system defaults.")

    print(f"Current Environment: {args.env}")
    print(f"Current db:",{os.getenv('DB')})

if __name__ == '__main__':
    main()