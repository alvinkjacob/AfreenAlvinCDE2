import socket
import json
import PySimpleGUI as sg
import os.path


def Main():
    turn = None
    host = '127.0.0.1'
    port = 8080
    employees = {}


    s = socket.socket()
    s.connect((host, port))

    

    # Add some color to the window
    sg.theme('DarkRed1')     
            
            # Very basic window.
            # Return values using automatic-numbered keys
    layout = [
                [sg.Text('Please enter your details:')],
                [sg.Text('First Name', size =(15, 1)), sg.InputText()],
                [sg.Text('Surname', size =(15, 1)), sg.InputText()],
                [sg.Text('Age', size =(15, 1)), sg.InputText()],
                [sg.Text('Are you employed?', size =(15, 1)), sg.InputText()],
                [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Simple data entry window', layout)
    event, values = window.read()
    print(event, values)

    while bool(values) == True:
        firstname = values[0]
        surname = values[1]
        Age = values[2]
        employed = values[3]
        name = firstname + " " + surname
        employees[name]={
            'First name':firstname,
            'Last Name':surname,
            'Age':Age,
            'Employed':employed
        }
        print(employees)

        jsonFile = json.dumps(employees)
        s.send(jsonFile.encode('utf-8'))
        print ("Sending your data")
        values.clear()
    s.close()
    

if __name__ == '__main__':
    Main()
