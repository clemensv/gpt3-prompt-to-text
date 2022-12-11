import argparse
import json
import os

from openai import api_key
import openai 


DEFAULT_CONFIG_FILE_NAME = ".gpt3-prompt-to-text-config.json"
DEFAULT_ENGINE = "text-davinci-002"


def create_parser():
    parser = argparse.ArgumentParser(
        description="Convert a prompt into text using OpenAI's GPT-3 API"
    )
    parser.add_argument(
        "prompt",
        type=str,
        nargs="?",
        help="The prompt to convert into text. If not provided, the prompt will be read from stdin.",
    )
    parser.add_argument(
        "-k",
        "--api-key",
        type=str,
        help="The OpenAI API key to use",
        default=api_key,
    )
    parser.add_argument(
        "-e",
        "--engine",
        type=str,
        help="The GPT-3 engine to use",
        default=DEFAULT_ENGINE,
    )
    parser.add_argument(
        "-s",
        "--store",
        action="store_true",
        help="Store the provided parameters in a configuration file",
    )
    parser.add_argument(
        "-t",
        "--tokens",
        type=int,
        help="The maximum number of tokens to generate",
        default=1024,
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read the prompt from stdin instead of from the command line",
    )

    return parser




def get_config():
    config_file_path = os.path.join(
        os.path.expanduser("~"), DEFAULT_CONFIG_FILE_NAME
    )
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as config_file:
            return json.load(config_file)
    return {}


def store_config(config):
    config_file_path = os.path.join(
        os.path.expanduser("~"), DEFAULT_CONFIG_FILE_NAME
    )
    with open(config_file_path, "w") as config_file:
        json.dump(config, config_file)


def main():
    parser = create_parser()
    args = parser.parse_args()
    config = get_config()

    # Use provided command line arguments, or fall back to configuration file values
    api_key = args.api_key or config.get("api_key")
    engine = args.engine or config.get("engine")
    tokens = args.tokens or config.get("tokens")

    if not args.prompt:
        # Prompt not provided as an argument
        if args.stdin:
            # Read the prompt from stdin
            prompt = input()
        else:
            # Set the prompt to an empty string
            prompt = ""
    else:
        # Use the provided prompt
        prompt = args.prompt

    if args.store:
        # Store provided parameters in configuration file
        store_config({"api_key": api_key, "engine": engine, "tokens": tokens})
        return

    # Use OpenAI's GPT-3 API to convert the prompt into text
    openai.api_key = api_key 
    completion = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    print(completion.choices[0].text)



if __name__ == "__main__":
    main()
