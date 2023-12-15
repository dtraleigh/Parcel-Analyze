import shutil
import unittest
import os

from ZipFile import ZipFile


class TestZipFile(unittest.TestCase):

    test_zip_file_name = "empty_doc_for_testing.zip"

    @classmethod
    def setUpClass(cls):
        shutil.copyfile(f"test_data\\{cls.test_zip_file_name}", f"parcel_zips\\{cls.test_zip_file_name}")

    @classmethod
    def tearDownClass(cls):
        os.remove(f"parcel_zips\\{cls.test_zip_file_name}")
        # shutil.rmtree(f"parcel_data\\{cls.test_zip_file_name.split('.')[0]}")

    def test_unzip_the_file1(self):
        """
        Unzip the test zip file
        """
        test_zip_file = ZipFile(f"{self.test_zip_file_name}")
        test_zip_file.unzip_the_file()
        self.assertTrue(os.path.isdir(f"parcel_data\\{self.test_zip_file_name.split('.')[0]}"))

        shutil.rmtree(f"parcel_data\\{self.test_zip_file_name.split('.')[0]}")

    def test_unzip_the_file2(self):
        """
        Try to unzip a file that's already been unzipped
        """
        test_zip_file = ZipFile(f"{self.test_zip_file_name}")
        self.assertTrue(test_zip_file.unzip_the_file())
        self.assertTrue(os.path.isdir(f"parcel_data\\{self.test_zip_file_name.split('.')[0]}"))
        self.assertFalse(test_zip_file.unzip_the_file())
        self.assertTrue(os.path.isdir(f"parcel_data\\{self.test_zip_file_name.split('.')[0]}"))

        shutil.rmtree(f"parcel_data\\{self.test_zip_file_name.split('.')[0]}")


if __name__ == '__main__':
    unittest.main()
