import os


def get_all_files_in_a_folder(folder_path):
    # Get a list of all files and directories in the folder
    yaml_files = []
    for root, dirs, files in os.walk(folder_path):
        print(f"dirs is {dirs}")
        yaml_files_at_sub_folder = [os.path.join(root, file) for file in files if file.endswith(".yaml") or file.endswith(".yml")]
        yaml_files.extend(yaml_files_at_sub_folder)
    return yaml_files
