## gpt3-prompt-to-text
A command line program in Python that can turn a prompt into a text using OpenAI's GPT-3 API.

# Installation
`pip install gpt3-prompt-to-text`

# Usage
```
gpt3-prompt-to-text [-h] [-k API_KEY] [-e ENGINE] [-s] prompt

Convert a prompt into text using OpenAI's GPT-3 API

  -k, --api-key TEXT    The OpenAI API key to use.
  -e, --engine TEXT     The GPT-3 engine to use.
  -s, --store           Store the provided parameters in a configuration file.
  -t, --tokens INTEGER  The maximum number of tokens to generate.
  --stdin               Read the prompt from stdin instead of from the command line.
  --help                Show this message and exit.
  
```

#Configuration

The api-key and engine parameters can be stored in a JSON configuration file in the user's profile directory. This file is automatically read and sets the parameters when the script is run. The command line arguments override the configuration file parameters.

#License

This project is licensed under the MIT License - see the LICENSE file for details.