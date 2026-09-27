import os
folders =input("Please provide the list of folders with spaces in between:").split()
for folder in folders:
        try:
          files =os.listdir(folder)
        except FileNotFoundError:
          print("Please provide a valid folder name, " + folder + " does not exsists")
          break
        except PermissionError:
          print("Permission denied for this particular folder" + folder)
          break

        print("the list of files in folder" + folder)

        for file in files:
          print(file)
