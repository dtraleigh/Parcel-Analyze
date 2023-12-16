from DataSnapshot import DataSnapshot
from functions import get_zip_files_list, get_parcel_data_dirs
from ZipFile import ZipFile
from prettytable import PrettyTable

results_table = PrettyTable()
results_table.field_names = ["Snapshot", "shp file"]

zip_files = get_zip_files_list()
zip_file_objects = [ZipFile(zip_file) for zip_file in zip_files]

for zip_file_object in zip_file_objects:
    zip_file_object.unzip_the_file()

data_dirs = get_parcel_data_dirs()
for data_dir in data_dirs:
    data_snapshot = DataSnapshot(f"{data_dir}")
    results_table.add_row([data_snapshot.directory_name, data_snapshot.get_shp_data_file])

print(results_table)
