import os
from pathlib import Path
from ..config.settings import DATA_DIR, OUTPUT_DIR

class ChapterManager:
    def __init__(self, chapter_name):
        self.chapter_name = chapter_name
        self.chapter_folder = OUTPUT_DIR / chapter_name
        self.topics_file = DATA_DIR / "Topics.txt"
        self.chapter_pptx = self.chapter_folder / f"{chapter_name}.pptx"

    def read_topics(self):
        if not self.topics_file.exists():
            raise FileNotFoundError(f"Topics file not found at {self.topics_file}")
        
        with open(self.topics_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]

    def get_topic_file(self, topic):
        return self.chapter_folder / f"{topic}.txt"

    def ensure_chapter_folder(self):
        os.makedirs(self.chapter_folder, exist_ok=True) 