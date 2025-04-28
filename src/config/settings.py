import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# API Configuration
API_CONFIG = {
    "provider": "openai", 
    "model": "gpt-4.1",
    "temperature": 0.7,
    "max_tokens": 2000,
    "api_version": "2024-02-15-preview"  # API version for GPT-4
}

# Mermaid Configuration
MERMAID_CONFIG = {
    "theme": "default",
    "backgroundColor": "white",
    "width": 800,
    "height": 600
}

# Slide Configuration
SLIDE_CONFIG = {
    "title_font_size": 44,
    "content_font_size": 32,
    "max_lines_per_slide": 7
}

# Slides Language
SLIDES_LANGUAGE = "English"

# Slide Schema
SLIDES_SCHEMA = {
    "type": "object",
    "properties": {
        "slides": {
            "type": "array",
            "description": "An array of slides to be generated",
            "items": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the slide"
                    },
                    "content": {
                        "type": "string",
                        "description": "The main content of the slide with detailed explanation"
                    },
                    "code_examples": {
                        "type": "string",
                        "description": "Example code to illustrate the concept"
                    },
                    "key_points": {
                        "type": "string",
                        "description": "Key points to remember from the slide"
                    },
                    "presenter_notes": {
                        "type": "string",
                        "description": "Notes for the presenter to guide the presentation"
                    },
                    "mermaid_text": {
                        "type": "string",
                        "description": "Mermaid diagram code to be rendered as an image"
                    }
                },
                "required": ["title", "content", "code_examples", "key_points", "presenter_notes", "mermaid_text"],
                "additionalProperties": False
            }
        }
    },
    "required": ["slides"],
    "additionalProperties": False
} 


# Create necessary directories
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True) 


