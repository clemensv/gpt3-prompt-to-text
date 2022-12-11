# gpt3-prompt-to-text

A command line program that converts a prompt into text using OpenAI's GPT-3 API.

## Installation

```
pip install gpt3-prompt-to-text
```

## Usage

```
gpt3-prompt-to-text [prompt] [-k | --api-key] [-e | --engine] [-s | --store] [-t | --tokens]
```

## Options

```
prompt The prompt to convert into text
-k | --api-key The OpenAI API key to use (default: OpenAI API key in environment)
-e | --engine The GPT-3 engine to use (default: text-davinci-002)
-s | --store Store the provided parameters in a configuration file
-t | --tokens The maximum number of tokens to generate (default: 1024)
```

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

## Development

For information on how to contribute to the project and what prerequisites must be installed, see [DEVELOP.md](DEVELOP.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Code of Conduct

This project adheres to the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.