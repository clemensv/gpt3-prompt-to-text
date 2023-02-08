# gpt3-prompt-to-text

gpt3-prompt-to-text is a command line program that converts a prompt into text using OpenAI's GPT-3 API. It is a simple wrapper around the [gpt3-client](https://github.com/openai/gpt-3-client) library. The program is meant to be simple and easy to use.

This code was developed by the very junior developer GPT-3 with patient mentoring by Clemens Vasters.

## Installation

With Python 3 installed, run

```
 pip install git+https://github.com/clemensv/gpt3-prompt-to-text.git
```

## Sign up for an OpenAI API Key

To use this tool, you need to sign up for an API key at [OpenAI](https://beta.openai.com/).

## Usage

```
gpt3-prompt-to-text [prompt] [-k | --api-key] [-e | --engine] [-s | --store] [-t | --tokens] [--edit] [--edit-file] [--noecho] [--amend] [--prepend]
```

## Options

| Option | Description |
| --- | --- |
| `prompt` | The prompt to convert into text |
| `-h, --help` | show this help message and exit |
| `-k API_KEY, --api-key API_KEY` | The OpenAI API key to use |
| `-e ENGINE, --engine ENGINE` | The GPT-3 engine to use (e.g. `gpt3-davinci-003` or `ada`). Optional. `gpt3-davinci-003` is the default. |
| `-s, --store` | Store the provided parameters in a configuration file |
| `-t TOKENS, --tokens TOKENS` | The maximum number of tokens to generate |
| `--edit` | Use the edit option. Takes the input to edit from stdin and the prompt from the command line |
| `--edit-file EDIT_FILE` | Use the edit option. Takes the input to edit from a file and the prompt from the command line. Writes the output back to the file. |
| `--endpoint` | The OpenAI endpoint to use. Optional. Defaults to `https://api.openai.com/v1/engines`. |
| `--show-deployments` | Show model deployments when running in Azure OpenAI |
| `--noecho` | don't echo the input |
| `--prepend PREPEND` | add the prepend text to the input (which is read from stdin) |

### Read prompt from stdin

```
echo [prompt] | gpt3-prompt-to-text
```

### Configuration file

The configuration file is stored in the user's profile directory and is named `.gpt3-prompt-to-text-config.json`. It contains the following fields:

```
{
"api_key": "The OpenAI API key to use",
"engine": "The GPT-3 engine to use",
"tokens": "The maximum number of tokens to generate"
}
```

## Store the API key

For convenience, run the script once with the -kl and -s options to store the key in the config file. Once that's done, the key will be read from there for all subsequent uses. 

```
gpt3-prompt-to-text -k [your api key] -s
```

## Examples

There are a few examples for how to use the tool:

Get help

```
gpt3-prompt-to-text -h
```

Write a short story using the default engine and the API key stored in the configuration file

```
gpt3-prompt-to-text "Once upon a time"
```

Suppress repeating the prompt or input into the output

```
gpt3-prompt-to-text --noecho "print a cat as ASCII art"
```

Control the number of tokens (length of the output)

```
gpt3-prompt-to-text "Once upon a time" -t 100
```

Send the output to a file

```
gpt3-prompt-to-text "Once upon a time" -t 100 > myfile.txt
```

Correct the story by prepending an instruction to what has been created

```
gpt3-prompt-to-text --prepend "Make a dragon appear here:" < myfile.txt
```

Similar to above but use the GPT-3 edit mode

```
gpt3-prompt-to-text --edit "Make a dragon appear here:" < myfile.txt
```

Edit the story file directly with an instruction

```
gpt3-prompt-to-text --edit-file myfile.txt "Make a dragon appear here"
```

## Development

For information on how to contribute to the project and what prerequisites must be installed, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.
