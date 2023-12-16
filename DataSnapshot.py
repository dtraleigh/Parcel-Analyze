import os


class DataSnapshot:
    def __init__(self, directory_path_and_name):
        self.directory_name = directory_path_and_name
        self.file_list = self.get_file_list
        self.shp_file_name = ""

    def __repr__(self):
        return f"Snapshot files from {self.directory_name}"

    @property
    def get_file_list(self):
        return [file for file in os.listdir(self.directory_name)]

    @property
    def contains_shp_data(self):
        file_list = self.get_file_list

        shp_files = []
        for file in file_list:
            if file.split(".")[-1] == "shp":
                shp_files.append(file)

        if len(shp_files) == 0:
            return False
        elif len(shp_files) == 1:
            print(shp_files[0])
            return True
        else:
            raise Exception(f"{self.directory_name} contains multiple .shp files, {shp_files}")

    @property
    def get_shp_data_file(self):
        if self.contains_shp_data:
            return [file for file in self.get_file_list if file.split(".")[-1] == "shp"][0]
        return None
