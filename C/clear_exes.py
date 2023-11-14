import os

def delete_exes_in_script_dir():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # List all files in the script's directory
    files = os.listdir(script_dir)
    
    # Filter for .exe files
    exe_files = [file for file in files if file.endswith('.exe')]

    # Delete each .exe file
    for exe_file in exe_files:
        try:
            os.remove(os.path.join(script_dir, exe_file))
            print(f"Deleted {exe_file}")
        except Exception as e:
            print(f"Error deleting {exe_file}: {e}")

if __name__ == "__main__":
    delete_exes_in_script_dir()
