# Example: Renaming each file to Nature_Photo1.jpg

# Import OS module
import os


# Define the folder where the images are stored
folder_path = 'C:/Users/olase/Downloads/nature_Photos'

# Create an empty list to store the image files
image_files = os.listdir(folder_path)

# Sort the images alphabetically
image_files.sort()

# Create a loop to rename each file in the list
for i in range(len(image_files)):
    old_name = image_files[i]
    new_name = f"Nature_Photo_{i+1}.jpg"

    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)
    print(f"The file: {old_name} has been renamed to: {new_name}")

print ("Renaming complete!")