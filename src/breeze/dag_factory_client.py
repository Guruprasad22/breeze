from dagfactory import dagfactory, load_yaml_dags
from src.breeze.file_util import get_all_files_in_a_folder


yaml_files = get_all_files_in_a_folder("""C:\\Users\\gurub\\PycharmProjects\\breeze\\src\\data_config""")

load_yaml_dags(
        globals_dict=globals(),
        dags_folder="tests/fixtures",
        suffix=yaml_files,
    )

