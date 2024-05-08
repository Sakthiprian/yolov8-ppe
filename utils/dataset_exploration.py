import os
import cv2
import matplotlib.pyplot as plt
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i",default="datasets/datasets/yolo_annotations_ppe")
args = parser.parse_args()

# Path to annotations directory
annotations_dir = args.i

class_mapping = {
    'hard-hat': 0,
    'gloves': 1,
    'mask' : 2,
    'glasses':3,
    'boots' : 4,
    'vest' : 5,
    'ppe-suit': 6,
    'ear-protector': 7,
    'safety-harness': 8
}

class_mapping_inverse = {v: k for k, v in class_mapping.items()}

# Dictionary to store class occurrences
class_counts = defaultdict(int)

# Function to read YOLO annotations and count class occurrences
def read_annotations_and_count(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r") as f:
                lines = f.readlines()
                for line in lines:
                    class_label = line.split()[0]
                    class_counts[class_label] += 1

# Function to visualize class distribution
def visualize_class_distribution(class_counts):
    class_numbers = list(class_counts.keys())
    labels = [class_mapping_inverse[int(class_number)] for class_number in class_numbers] 
    counts = list(class_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts)
    plt.xlabel('Class Labels')
    plt.ylabel('Count')
    plt.title('Class Distribution')
    plt.xticks(rotation=45)
    plt.show()

read_annotations_and_count(annotations_dir)
visualize_class_distribution(class_counts)

