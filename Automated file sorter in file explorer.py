import os, shutil
path = r"D:\Aaliya\Data Analytics Bootcamp\PYTHON\T1/"
file_name = os.listdir(path)

folder_names = ['csv files', 'image files', 'text files']

for loop in range(0, 3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file or ".png" in file:  # Check for image files
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file:  # Check for text files
        shutil.move(path + file, path + "text files/" + file)





