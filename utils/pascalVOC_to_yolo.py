import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')

args = parser.parse_args()

import os
import xml.etree.ElementTree as ET

# change class mapping to get only annotations needed 
class_mapping = {
    'hard-hat': 0,
    'gloves': 1,
    'boots' : 2,
    'vest' : 3,
    'ppe-suit': 4
}

#function to convert pascalVOC to yolov8 annotations
def convert_pascal_voc_to_yolo(xml_file, output_folder):
    # Parse XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract image dimensions
    image_width = int(root.find('size/width').text)
    image_height = int(root.find('size/height').text)

    # Open YOLO annotation file
    filename = os.path.splitext(os.path.basename(xml_file))[0]
    yolo_annotation_file = open(os.path.join(output_folder, filename + '.txt'), 'w')

    # Iterate through each object in the XML
    for obj in root.findall('object'):
        class_name = obj.find('name').text
        class_index = class_mapping.get(class_name)
        if class_index is None:
            print(f"Warning: Class '{class_name}' not found in class mapping.")
            continue

        # Extract bounding box coordinates
        xmin = float(obj.find('bndbox/xmin').text)
        ymin = float(obj.find('bndbox/ymin').text)
        xmax = float(obj.find('bndbox/xmax').text)
        ymax = float(obj.find('bndbox/ymax').text)

        # Convert bounding box coordinates to YOLO format
        x_center = (xmin + xmax) / 2 / image_width
        y_center = (ymin + ymax) / 2 / image_height
        box_width = (xmax - xmin) / image_width
        box_height = (ymax - ymin) / image_height

        # Write YOLO annotation to file
        yolo_annotation_file.write(f"{class_index} {x_center} {y_center} {box_width} {box_height}\n")

    # Close YOLO annotation file
    yolo_annotation_file.close()

def pascal_voc_to_yolo(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each XML file in the input folder
    for xml_file in os.listdir(input_folder):
        if xml_file.endswith('.xml'):
            convert_pascal_voc_to_yolo(os.path.join(input_folder, xml_file), output_folder)

# Example usage
input_folder = args.input_folder
output_folder = args.output_folder
pascal_voc_to_yolo(input_folder, output_folder)
