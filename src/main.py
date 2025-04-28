import os
from .api.api_client import APIClient
from .generators.slide_generator import SlideGenerator
from .utils.chapter_manager import ChapterManager
from .config.settings import API_CONFIG

def generate_slide(chapter, topic, output_pptx_path):
    api_client = APIClient()
    slides_data = api_client.generate_slides(chapter, topic)
    slide_generator = SlideGenerator(output_pptx_path)
    slide_generator.add_title_slide(topic, chapter)
    for slide_data in slides_data['slides']:
        # Create content slide
        content_slide_layout = slide_generator.prs.slide_layouts[1]
        slide = slide_generator.prs.slides.add_slide(content_slide_layout)
        
        # Add slide content
        title_shape = slide.shapes.title
        content_shape = slide.placeholders[1]
        
        title_shape.text = slide_data["title"]
        content_shape.text = slide_data["content"]
        
        # If Mermaid diagram exists, add it to the slide
        if 'mermaid_text' in slide_data and slide_data['mermaid_text'] != '':
            slide_generator.add_mermaid_diagram(slide, slide_data['mermaid_text'])
            
        # Add code examples
        if 'code_examples' in slide_data:
            slide_generator.add_code_examples(slide, slide_data['code_examples'])
            
        # Add presenter notes
        if 'presenter_notes' in slide_data:
            slide_generator.add_presenter_notes(slide, slide_data['presenter_notes'])
            
    slide_generator.save()
    return slides_data

def generate_chapter_slides(chapter_name):
    chapter_manager = ChapterManager(chapter_name)
    chapter_manager.ensure_chapter_folder()
    
    topics = chapter_manager.read_topics()
    for topic in topics:
        topic_file = chapter_manager.get_topic_file(topic)
        if not os.path.exists(topic_file):
            print(f"Generating slides for topic: {topic}")
            slides_data = generate_slide(chapter_name, topic, chapter_manager.chapter_pptx)
            with open(topic_file, 'w', encoding='utf-8') as f:
                f.write(str(slides_data))
        else:
            print(f"File {topic_file} already exists. Skipping regeneration.")
    print(f"All slides have been successfully generated in folder {chapter_manager.chapter_folder}")

if __name__ == "__main__":
    chapter_name = "Flowchart and Sequence Diagrams"  # You can change this or make it configurable
    generate_chapter_slides(chapter_name) 