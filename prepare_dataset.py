import os
import csv
import cv2

def preprocess_image(image_path, output_directory):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (224, 224))
    image_name = os.path.basename(image_path)
    output_path = os.path.join(output_directory, image_name)
    cv2.imwrite(output_path, resized_image)

def label_images(input_directory, output_csv, label):
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['filename', 'label'])

        for filename in os.listdir(input_directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                writer.writerow([filename, label])

    print(f"Labels saved to {output_csv}")

def main():
    input_directory = "unlabeled_images"
    output_directory = "dataset/splay_foot"
    output_csv = "labeled_dataset.csv"
    label = "splay_foot"

    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_directory, filename)
            preprocess_image(image_path, output_directory)
    
    label_images(output_directory, output_csv, label)

    print("Dataset preparation and labeling completed.")

if __name__ == "__main__":
    main()
