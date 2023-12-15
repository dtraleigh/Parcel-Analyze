from functions import get_zip_files_list
from ZipFile import ZipFile

zip_files = get_zip_files_list()
zip_file_objects = [ZipFile(zip_file) for zip_file in zip_files]

for zip_file_object in zip_file_objects:
    zip_file_object.unzip_the_file()
