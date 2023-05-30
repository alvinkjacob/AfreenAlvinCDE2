import socket
import json
import PySimpleGUI as sg
import os.path
import time
import webbrowser
import re
import sys

def validate(values):
    is_valid=True
    pattern = "^[A-Za-z-]*$"
    values_invalid = []

    if len(values['-NAME-'])==0:
        values_invalid.append("Please enter your first name")
        is_valid=False
    elif bool(re.match(pattern, values['-NAME-'])) != True:
        values_invalid.append("Please ensure your name does not contain numbers or special characters (hyphens are allowed)")
        is_valid=False
    
    if len(values['-SURNAME-'])==0:
        values_invalid.append("Please enter your surname")
        is_valid=False
    elif bool(re.match(pattern, values['-SURNAME-'])) != True:
        values_invalid.append("Please ensure your surname does not contain numbers or special characters (hyphens are allowed)")
        is_valid=False
    

    if len(values['-AGE-'])==0:
        values_invalid.append("Please enter your age")
        is_valid=False
    elif values['-AGE-'].isdigit()!=True:
        values_invalid.append("Please enter a positive integer")
        is_valid=False
    elif int(values['-AGE-'])<=15:
        values_invalid.append("You must be 16 or over to be employed")
        is_valid=False
    

    if len(values['-EMPLOYED-'])==0:
        values_invalid.append("Please enter Y or N to indicate employment status")
        is_valid=False
    elif values['-EMPLOYED-'].upper() != 'Y' and values['-EMPLOYED-'].upper() != 'N':
        values_invalid.append("Please enter Y or N to indicate employment status")
        is_valid=False

    result = [is_valid, values_invalid]
    return result

def display_error(values_invalid):
    error_message= ''
    for value_invalid in values_invalid:
        error_message += ('\nInvalid'+":"+value_invalid)
    return error_message


def Main():
    turn = None
    host = '127.0.0.1'
    ports = [8888, 12346]
    employees = {}

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, ports[0]))
        
    except socket.error as msg:
        print("Couldn't connect with the socket-server: %s" % msg + "Trying another server...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, ports[1]))
        except socket.error as msg:
            print("Couldn't connect with either socket-server: %s" % msg)
            sys.exit(1)
            
    

    # Add some color to the window
    sg.theme('DarkRed1')     
            
            # Very basic window.
            # Return values using automatic-numbered keys
    layout = [
                [sg.Text('Please enter your details:')],
                [sg.Text('First Name', size =(15, 1)), sg.InputText(key='-NAME-')],
                [sg.Text('Surname', size =(15, 1)), sg.InputText(key='-SURNAME-')],
                [sg.Text('Age', size =(15, 1)), sg.InputText(key='-AGE-')],
                [sg.Text('Are you employed? (Enter Y/N)', size =(15, 1)), sg.InputText(key='-EMPLOYED-')],
                [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Employee Information Form', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        else:
            validation_result = validate(values)
            if validation_result[0]:
                sg.popup('Employee data submitted')
                print(values)

                while bool(values) == True:
                    firstname = values['-NAME-']
                    surname = values['-SURNAME-']
                    Age = values['-AGE-']
                    employed = values['-EMPLOYED-']
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

                    try:
                        data = s.recv(1024)      # recv data
                        print('From server: data received: ' + repr(data))
                        time.sleep(5)

                    except:
                        print("Didn't receive confirmation data back from server", str(e))

                    with open("employee_data_client.html", "w") as f:
                        f.write(data.decode())

                    webbrowser.open("employee_data_client.html")

                    time.sleep(5)
                    
                s.close()

            else:
                error_message=display_error(validation_result[1])
                sg.popup(error_message)
        
    window.close()
    

if __name__ == '__main__':
    Main()