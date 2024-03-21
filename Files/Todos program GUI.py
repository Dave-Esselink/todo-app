import cfun
import PySimpleGUI as sg                  #imports custom GUI modual

label = sg.Text("Type in a to-do")        #App user prompt
input_box = sg.InputText(tooltip="Enter todo")    #Input text box
add_button = sg.Button("Add")

window = sg.Window('To-Do App', layout=[[label], [input_box, add_button]])  #App header label. layout=List of buttons and boxes
window.read()                              #opens and closes the window
window.close()