import os
import shutil

source = input("Enter source folder path: ")
destination = input("Enter destination folder path: ")

for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), destination)

print("All JPG files moved successfully.")