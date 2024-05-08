import os
import random
import shutil

# Define paths to image dataset and labels folders
image_dataset_folder = 'D:\coding\github\yolov8-ppe-detection\datasets\datasets\images'
labels_folder = 'D:\coding\github\yolov8-ppe-detection\datasets\datasets\yolo_annotations_ppe_5'

# Define paths for training and validation folders
train_folder = 'datasets/datasets/data_ppe_5/train'
val_folder = 'datasets/datasets/data_ppe_5/val'

# Create train and val folders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

# Create subdirectories for images and labels inside train and val folders
train_image_folder = os.path.join(train_folder, 'images')
train_label_folder = os.path.join(train_folder, 'labels')
val_image_folder = os.path.join(val_folder, 'images')
val_label_folder = os.path.join(val_folder, 'labels')

os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(train_label_folder, exist_ok=True)
os.makedirs(val_image_folder, exist_ok=True)
os.makedirs(val_label_folder, exist_ok=True)

# Get list of image files
image_files = os.listdir(image_dataset_folder)

# Get list of label files
label_files = os.listdir(labels_folder)

# Extract filenames without extensions
image_filenames = {os.path.splitext(filename)[0] for filename in image_files}
label_filenames = {os.path.splitext(filename)[0] for filename in label_files}

# Find common filenames between image and label datasets
common_filenames = image_filenames.intersection(label_filenames)

# Shuffle the list of common filenames to ensure randomness
common_filenames = list(common_filenames)
random.shuffle(common_filenames)

# Calculate split indices
split_index = int(0.9 * len(common_filenames))

# Split the common filenames into training and validation sets
train_filenames = common_filenames[:split_index]
val_filenames = common_filenames[split_index:]

# Copy images and labels to respective train and val folders
for filename in train_filenames:
    # Copy images
    shutil.copy(os.path.join(image_dataset_folder, filename + '.jpg'), os.path.join(train_image_folder, filename + '.jpg'))
    # Copy labels
    shutil.copy(os.path.join(labels_folder, filename + '.txt'), os.path.join(train_label_folder, filename + '.txt'))

for filename in val_filenames:
    # Copy images
    shutil.copy(os.path.join(image_dataset_folder, filename + '.jpg'), os.path.join(val_image_folder, filename + '.jpg'))
    # Copy labels
    shutil.copy(os.path.join(labels_folder, filename + '.txt'), os.path.join(val_label_folder, filename + '.txt'))

print("Dataset divided into training and validation sets successfully.")