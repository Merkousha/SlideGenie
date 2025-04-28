import os
import subprocess
import tempfile
import shutil
import re
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image
from ..utils.logger import logger

class MermaidGenerator:
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()
        self.mmdc_path = self._find_mmdc_path()
        self.max_width = 12
        self.max_height = 6
        self.dpi = 96

    def _find_mmdc_path(self):
        try:
            mmdc_path = shutil.which('mmdc')
            if mmdc_path:
                return mmdc_path

            common_paths = [
                os.path.expanduser('~/.npm-global/bin/mmdc'),
                os.path.expanduser('~/.nvm/versions/node/current/bin/mmdc'),
                os.path.expanduser('~/.nvm/versions/node/current/lib/node_modules/@mermaid-js/mermaid-cli/src/cli.js'),
                '/usr/local/bin/mmdc',
                '/usr/bin/mmdc',
                'C:\\Users\\%USERNAME%\\AppData\\Roaming\\npm\\mmdc.cmd',
                'C:\\Program Files\\nodejs\\mmdc.cmd'
            ]

            for path in common_paths:
                expanded_path = os.path.expandvars(path)
                if os.path.exists(expanded_path):
                    return expanded_path

            return None
        except Exception as e:
            logger.error(f"Error finding mmdc path: {str(e)}")
            return None

    def _calculate_dimensions_from_image(self, image_path):
        try:
            with Image.open(image_path) as img:
                width_px, height_px = img.size
                width_inches = width_px / self.dpi
                height_inches = height_px / self.dpi
                aspect_ratio = width_px / height_px

                if width_inches > self.max_width or height_inches > self.max_height:
                    if width_inches / self.max_width > height_inches / self.max_height:
                        width_inches = self.max_width
                        height_inches = width_inches / aspect_ratio
                    else:
                        height_inches = self.max_height
                        width_inches = height_inches * aspect_ratio

                return width_inches, height_inches
        except Exception as e:
            logger.error(f"Error reading image dimensions: {str(e)}")
            return 8, 3

    def generate_image(self, mermaid_code, output_path):
        if not self.mmdc_path:
            logger.error("Error: mermaid-cli (mmdc) not found. Please install using 'npm install -g @mermaid-js/mermaid-cli'")
            return False

        mermaid_file = os.path.join(self.temp_dir, 'temp.mmd')
        with open(mermaid_file, 'w', encoding='utf-8') as f:
            f.write(mermaid_code)

        try:
            subprocess.run([
                self.mmdc_path,
                '-i', mermaid_file,
                '-o', output_path,
                '-b', 'transparent'
            ], check=True)
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Error converting Mermaid to image: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error in Mermaid conversion: {str(e)}")
            return False
        finally:
            if os.path.exists(mermaid_file):
                os.remove(mermaid_file)

    def add_mermaid_to_slide(self, slide, mermaid_code, width=None, height=None):
        temp_image = os.path.join(self.temp_dir, 'temp_mermaid.png')

        if self.generate_image(mermaid_code, temp_image):
            if width is None or height is None:
                width_inches, height_inches = self._calculate_dimensions_from_image(temp_image)
                width = Inches(width_inches)
                height = Inches(height_inches)

            slide_width = Inches(13.33)
            slide_height = Inches(7.5)

            left = (slide_width - width) / 2
            top = (slide_height - height) / 2

            slide.shapes.add_picture(temp_image, left, top, width, height)

            if os.path.exists(temp_image):
                os.remove(temp_image)
            return True
        return False
