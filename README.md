# SlideGenie - AI-Powered Educational Slide Generator

SlideGenie is an intelligent educational slide generator that leverages the power of OpenAI API to create engaging presentations and converts Mermaid diagrams into visual assets.

## Features

- AI-powered slide content generation
- Automatic Mermaid diagram to image conversion
- Customizable slide templates
- Multi-language support
- Educational content optimization

## Prerequisites

1. **Python 3.8+**
2. **Node.js and npm** (for installing mermaid-cli)
3. **mermaid-cli** (for converting Mermaid diagrams to images)
4. **OpenAI API Key** (for API access)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install mermaid-cli

```bash
npm install -g @mermaid-js/mermaid-cli
```

If you encounter permission errors, you can use:

```bash
npm install -g @mermaid-js/mermaid-cli --unsafe-perm=true --allow-root
```

Or on Windows with admin privileges:

```bash
npm install -g @mermaid-js/mermaid-cli --unsafe-perm=true
```

### 3. Set up OpenAI API Key

Create a `.env` file in the project root directory with the following content:

```
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Usage

1. Fill the `Topics.txt` file with your desired topics.
2. Prepare the `Base.pptx` file with your desired template.
3. Run the program:

```bash
# From the project root directory
python -m src.main
```

## Project Structure

```
SlideGenie/
│
├── src/                     # Source code directory
│   ├── api/                # API related modules
│   ├── config/             # Configuration modules
│   ├── generators/         # Slide and content generators
│   ├── utils/              # Utility functions
│   ├── main.py             # Main program file
│   └── __init__.py         # Package initialization
│
├── data/                   # Data directory
│   └── Topics.txt         # Topics list
├── output/                 # Generated output files
├── run.py                  # Entry point script
├── requirements.txt        # Python dependencies
├── Base.pptx              # Base PowerPoint template
└── README.md              # Project documentation
```

## Configuration

Main configurations are in the `config.py` file:

- **API Configuration**: OpenAI API settings
- **Chapter Configuration**: Chapter settings
- **Prompt Configuration**: Prompt settings
- **Mermaid Configuration**: Mermaid diagram settings
- **File Paths**: File paths
- **Slide Schema**: Slide JSON structure
- **Language Settings**: Configure the language of generated slides

### Language Configuration

The language of the generated slides can be configured in `src/config/settings.py`:

```python
# Slides Language
LANGUAGE = "en"  # Change to your desired language code
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the API
- Mermaid.js team for the diagram generation tool
- All contributors who help improve SlideGenie 