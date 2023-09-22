import os
import shutil
import uuid

# Replace with the path to your main folder
main_folder_path = 'C:/Users/kaspe/Documents/GitHub/SkoleProg/NeuralNetwork/Neural_Banana/images/test_test'

# Iterate over all items in the main folder
for folder_name in os.listdir(main_folder_path):
    subfolder_path = os.path.join(main_folder_path, folder_name)
    
    # Check if the item is a folder
    if os.path.isdir(subfolder_path):
        
        # Iterate over all files in the subfolder
        for file_name in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file_name)
            
            # Check if the item is a file
            if os.path.isfile(file_path):
                
                # Generate a unique name for the file
                unique_name = f"{uuid.uuid4()}_{file_name}"
                dest_path = os.path.join(main_folder_path, unique_name)
                
                # Move and rename the file to the main folder
                shutil.move(file_path, dest_path)
                
        # Optionally, remove the empty subfolder
        os.rmdir(subfolder_path)
