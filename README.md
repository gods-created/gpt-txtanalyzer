# GPT Text Analyzer

A simple tool for analyzing and summarizing text using GPT models.

## Features

- Text summarization
- Keyword extraction
- Sentiment analysis
- Easy-to-use interface

## Installation

```bash
git clone https://github.com/yourusername/gpt-txtanalyzer.git
cd gpt-txtanalyzer
pip install -r requirements.txt
```

## Usage

You need to make a few changes to the main.py file, as the application itself is designed for lambda functions and as an API Gateway endpoint.

```bash
    python main.py
```

## Example

Input text:

```
Artificial intelligence is transforming the world. It enables new solutions and improves efficiency.
```

Output:

```
{
    'tags': [
        'value': '...'
    ],
    'sentiment': '...'
}
```

## Configuration

Edit `.env` to set your GPT API key and preferences.

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

[MIT](LICENSE)