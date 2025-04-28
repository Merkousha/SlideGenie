# Slider - Educational Slide Generator

This project is designed to generate educational slides using OpenAI API and convert Mermaid diagrams to images.

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
Slider/
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
SLIDES_LANGUAGE = "English"  # Change to "Persian" for Persian slides
```

This setting determines the language of all generated content, including:
- Slide titles
- Slide content
- Code examples
- Key points
- Presenter notes

### Setting Chapter Name

The chapter name can be set in two places:

1. In `run.py` (recommended for production use):
```python
if __name__ == "__main__":
    chapter_name = "Chapter1"  # Change this to your desired chapter name
    generate_chapter_slides(chapter_name)
```

2. In `src/main.py` (for development/testing):
```python
if __name__ == "__main__":
    chapter_name = "Flowchart and Sequence Diagrams"  # Change this to your desired chapter name
    generate_chapter_slides(chapter_name)
```

The chapter name is used to:
- Create a folder in the output directory
- Name the generated PowerPoint file
- Organize topic files

## Mermaid Diagrams

To use Mermaid diagrams in slides, place the Mermaid code in the `mermaid_text` field. Example:

```json
{
  "slides": [
    {
      "title": "Flow Diagram",
      "content": "Diagram description",
      "code_examples": "",
      "key_points": "Key points",
      "presenter_notes": "Presenter notes",
      "mermaid_text": "graph TD\n    A[Start] --> B{Condition}\n    B -->|Yes| C[Operation 1]\n    B -->|No| D[Operation 2]"
    }
  ]
}
```

## Contributing

We welcome contributions to this project! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Submit a Pull Request (PR)

### Pull Request Process

1. Ensure your PR includes a clear description of the changes
2. Make sure all tests pass
3. Update documentation if necessary
4. Your PR will be reviewed by maintainers
5. Once approved, your changes will be merged into the main branch

We review all PRs and will get back to you as soon as possible. Thank you for your contributions!

## Troubleshooting

### Mermaid CLI Not Found

If you encounter the error "mermaid-cli (mmdc) not found":

1. Make sure you have installed mermaid-cli
2. Check the mermaid-cli installation path:

```bash
which mmdc  # on Linux/Mac
where mmdc  # on Windows
```

3. If the path is not found, you can add the full path in the `mermaid_generator.py` file.

### OpenAI API Access Issues

If you encounter OpenAI API access errors:

1. Make sure your API key is valid
2. Check if the API key is properly set in the `config.py` file
3. If you're using a VPN, make sure you have access to OpenAI servers. 