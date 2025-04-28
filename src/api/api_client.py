import os
from dotenv import load_dotenv
from openai import OpenAI
from ..config.settings import API_CONFIG,SLIDES_LANGUAGE,SLIDES_SCHEMA

# Load environment variables from .env file
load_dotenv()

class APIClient:
    def __init__(self):
        self.config = API_CONFIG
        self.language = SLIDES_LANGUAGE
        self.schema = SLIDES_SCHEMA
        if self.config["provider"] == "openai":
            api_key = os.getenv("OPENAI_API_KEY")
            api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
            print(api_key)
            print(api_base)
            if not api_key:
                raise ValueError("OPENAI_API_KEY environment variable is not set in .env file")
            
            # Initialize OpenAI client
            self.client = OpenAI(
                api_key=api_key,
                base_url=api_base
            )

    def generate_slides(self, chapter, topic):
        if self.config["provider"] == "openai":
            return self._generate_with_openai(chapter, topic)
        else:
            raise ValueError(f"Unsupported API provider: {self.config['provider']}")

    def _generate_with_openai(self, chapter, topic):
        prompt = f"""Create a detailed slide presentation about {topic} for the chapter {chapter}.
        Include:
        1. A title slide
        2. 5-7 content slides with key points
        3. Any relevant diagrams or visualizations using Mermaid syntax
        4. any relevant code snippets
        Format the response as a JSON"""
        prompt = prompt + f"Language Contents must be {self.language} ."
        response = self.client.chat.completions.create(
            model=self.config["model"],
            messages=[
                {"role": "system", "content": "You are a professional slide content generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.config["temperature"],
            max_tokens=self.config["max_tokens"],
            response_format={
                        "type": "json_schema",
                        "json_schema": {
                            "name": "slides_output",
                            "strict": True,
                            "schema": self.schema
                        }
                    }

        )

        # Parse and return the response
        try:
            return eval(response.choices[0].message.content)
        except:
            return {"slides": [{"title": "Error", "content": "Failed to generate slides"}]} 