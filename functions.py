import os


def get_zip_files_list():
    list_of_zip_files = []

    for file in os.listdir("parcel_zips"):
        if file.endswith(".zip"):
            list_of_zip_files.append(file)

    return list_of_zip_files


def get_parcel_data_dirs():
    return [f.path for f in os.scandir("parcel_data") if f.is_dir()]
