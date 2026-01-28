import os

def get_file_extension(filename):
    return os.path.splitext(filename)[1].lower()

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def safe_move(src, dst):
    base, ext = os.path.splitext(dst)
    counter = 1
    while os.path.exists(dst):
        dst = f"{base}_{counter}{ext}"
        counter += 1
    os.rename(src, dst)
