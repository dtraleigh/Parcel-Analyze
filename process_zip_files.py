from DataSnapshot import DataSnapshot
from functions import get_zip_files_list, get_parcel_data_dirs, get_list_of_shp_col_names, reorder_lists
from ZipFile import ZipFile
from prettytable import PrettyTable
import csv
from datetime import datetime

start_time = datetime.now()

results_table = PrettyTable()
results_table.field_names = ["Snapshot", "shp file"]

zip_files = get_zip_files_list()
zip_file_objects = [ZipFile(zip_file) for zip_file in zip_files]

for zip_file_object in zip_file_objects:
    zip_file_object.unzip_the_file()

data_dirs = get_parcel_data_dirs()
data_snapshots = []
for data_dir in data_dirs:
    data_snapshot = DataSnapshot(f"{data_dir}")
    data_snapshots.append(data_snapshot)
    results_table.add_row([data_snapshot.directory_name, data_snapshot.get_shp_data_file])

print(results_table)

with open("column_names_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    print(f"Creating column_names_output.csv file with {data_snapshots}")

    for data_snapshot in data_snapshots:
        data_snapshot.shp_col_name_list = get_list_of_shp_col_names(data_snapshot, True)

    reorder_lists(data_snapshots)

    for data_snapshot in data_snapshots:
        writer.writerow([data_snapshot.directory_name] + data_snapshot.shp_col_name_list_aligned_w_others)

print(f"Start: {start_time}")
print(f"End: {datetime.now()}")
