import PySimpleGUI as sg
from zip_creator import make_archive
import os

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()                            #filepath box
choose_button1 = sg.FilesBrowse("Choose", key="file_path")      #Choose button for file compression
                            #key= applies a key to the choose button
label2 = sg.Text("Select destination folder:")
input2 = sg.Input()                            #filepath box
choose_button2 = sg.FolderBrowse("Choose", key="folder")     #Choose button for file destination

compress_button = sg.Button("Compress")        #Compress execute button

window = sg.Window("File Compressor",                         #Creates the GUI window
                   layout=[[label1,input1, choose_button1],   #row1
                           [label2,input2, choose_button2],   #row2
                           [compress_button]])                #row3

""" When creating buttons, each pair of brackets
represents 1 horizontal row. The next set of brackets = the next row """
while True:
        event, values = window.read()
        print(event, values)
        #Reads the event(Buttons) and values(Textboxes)
        filepaths = values["file_path"].split(";")

        #Grabs the filepaths, both input and output paths are one string split by a semicolon
        folderpath = values["folder"]
        make_archive(filepaths, folderpath)

        os.startfile(folderpath)


window.read()
window.close()

