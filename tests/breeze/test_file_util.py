from src.breeze.file_util import get_all_files_in_a_folder


def test_filter_for_yaml():
    files = get_all_files_in_a_folder("""C:\\Users\\gurub\\PycharmProjects\\breeze\\src\\data_config""")
    print("yaml files are :")
    for file in files:
        print(file)

