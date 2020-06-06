import os
from tqdm import tqdm
from tkinter import Tk
from tkinter.filedialog import askdirectory


def readdirfiles(directory):
    """Function which returns all files in input directory and it's subdirectories.

    Arguments:
        directory {os.path} -- Input directory.

    Returns:
        list -- A list of all filepaths in the input directory. 
    """
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(directory):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]

    return listOfFiles


def main():

    # Get directory path from user.
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    dirname = askdirectory() # show an "Open" dialog box and return the path to the selected file
    print("Checking folder: {}...".format(dirname))

    # Get string to change
    strOld = input("\n\nWhat string should I change: ")

    # Get new string
    strNew = input("Replace the string with: ")

    print("\n")
    files = readdirfiles(dirname)
    for file in tqdm(files):

        newfile = file.replace(strOld, strNew)
        os.rename(file, newfile)

        if strOld in file:
            outfile = os.path.relpath(file, start=dirname)
    print("\n")


main()

    