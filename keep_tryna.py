import os

dir_path = os.getcwd() + '/media_dir/'
print("Current Directory:", os.getcwd())
print("Folder Path:", dir_path)

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    print("Folder created successfully")
else:
    print("Folder already exists")

