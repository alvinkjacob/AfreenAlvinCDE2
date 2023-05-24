import socket

import PySimpleGUI as sg
import os.path


def Main():


    host = '127.0.0.1'
    port = 8888

    s = socket.socket()
    s.connect((host, port))


    # Add some color to the window
    sg.theme('DarkRed1')     
      
    # Very basic window.
    # Return values using automatic-numbered keys
    layout = [
        [sg.Text('Please enter your details:')],
        [sg.Text('Title', size =(15, 1)), sg.InputText()],
        [sg.Text('First Name', size =(15, 1)), sg.InputText()],
        [sg.Text('Surname', size =(15, 1)), sg.InputText()],
        [sg.Text('Age', size =(15, 1)), sg.InputText()],
        [sg.Text('Are you employed?', size =(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]
      
    window = sg.Window('Simple data entry window', layout)
    event, values = window.read()
    

    # message = input("You are now connected to the server. Please enter a message-> ")
    #while True:
    for value in values.values():
            #event, values = window.read()
            print(event, values)
            s.send(value.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            print("Message received from server: " +str(data))
            #values[x] = input("->")
    s.close()


    # The input data looks like a simple list 
    # when automatic numbered
    #print(event, values[0], values[1], values[2])
    #window.close()


if __name__ == '__main__':
    Main()
