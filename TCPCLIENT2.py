import socket
import json
import PySimpleGUI as sg
import os.path
import time
import webbrowser


def Main():
    turn = None
    host = '127.0.0.1'
    ports = [8888, 12346]
    employees = {}

            
    

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

    window = sg.Window('Employee Information Form', layout)
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

        for port in ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))

                jsonFile = json.dumps(employees)
                s.send(jsonFile.encode('utf-8'))
                print ("Sending your data")
                values.clear()
                data = s.recv(1024)      # recv data
                print('From server: ' + repr(data))

                with open("employee_data.html", "w") as f:
                    f.write(data.decode())

                webbrowser.open("employee_data.html")
                break  # Break the loop if a successful connection is made
            except Exception as e:
                print(f"Failed to connect to {host}: {e}")

        



        time.sleep(5)
        
    s.close()
    

if __name__ == '__main__':
    Main()
