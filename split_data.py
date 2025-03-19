import os
import shutil
import random

# Paths based on your structure
data_dir = 'dataset'
images_dir = os.path.join(data_dir, 'data/images')
labels_dir = os.path.join(data_dir, 'data/labels')

train_images = os.path.join(data_dir, 'train/images')
train_labels = os.path.join(data_dir, 'train/labels')
val_images = os.path.join(data_dir, 'val/images')
val_labels = os.path.join(data_dir, 'val/labels')

# Create directories if not exist
os.makedirs(train_images, exist_ok=True)
os.makedirs(train_labels, exist_ok=True)
os.makedirs(val_images, exist_ok=True)
os.makedirs(val_labels, exist_ok=True)

# Get list of images and labels
images = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
random.shuffle(images)

# Split 80% train, 20% validation
split_idx = int(0.8 * len(images))
train_files = images[:split_idx]
val_files = images[split_idx:]

# Move files to respective folders
for file in train_files:
    shutil.move(os.path.join(images_dir, file), os.path.join(train_images, file))
    label_file = file.replace('.jpg', '.txt')
    if os.path.exists(os.path.join(labels_dir, label_file)):
        shutil.move(os.path.join(labels_dir, label_file), os.path.join(train_labels, label_file))

for file in val_files:
    shutil.move(os.path.join(images_dir, file), os.path.join(val_images, file))
    label_file = file.replace('.jpg', '.txt')
    if os.path.exists(os.path.join(labels_dir, label_file)):
        shutil.move(os.path.join(labels_dir, label_file), os.path.join(val_labels, label_file))

print("Data split completed!")
