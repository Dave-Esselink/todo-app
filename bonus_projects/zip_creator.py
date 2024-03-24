import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    #pathlib.Path=directory path, then filename(2 variables)
    with zipfile.ZipFile(dest_path, 'w') as archive:
    #Creates a zipfile type object

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            #extracts the filename
            archive.write(filepath, arcname=filepath.name)



if __name__ == "__main__":
    make_archive(filepaths=["e1.py", "e2.py"], dest_dir="dest")