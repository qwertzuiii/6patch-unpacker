import zipfile, os

def extract_zip(zip_file, extract_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

def make_extraction_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)