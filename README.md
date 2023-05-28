# AfreenAlvinCDE2
A repository created for the Collaborative Distributed Environments Assignment 2 application. 

Lead Developer: Afreen Hussain
Lead Designer: Alvin Jacob

This application is used to record employee details regarding information about their first name, surname, age, and employed status. This information will be able to be sent from a single client or multiple clients to the server, and will automatically generate a HTML webpage listing the data entries. 

Steps to clone repository folder from GitHub 
1) Navigate to https://github.com/alvinkjacob/AfreenAlvinCDE2 
2) Click the green 'Code' button and copy the link that is housed under the HTTPS section.
3) Navigate to the local folder that you wish to save the cloned repository.
4) Right-click and select 'Git Bash Here'.
5) Type 'git clone [paste url]' and press 'enter'.
6) The repository folder should now appear in your local folder.
7) Open the repository folder using your chosen IDE. 

Installing PySimpleGui
1) Open the Command Prompt
2) Change directory to the project folder
3) Enter the following command to install PySimpleGui: python -m pip install PySimpleGUI
4) Wait for installation to complete

Steps to send employee information from 1 client to the server
1) Open cmd
2) Using the 'cd' command navigate to the location that you have saved the 'AfreenAlvinCDE2' repository folder.
3) Type 'py SERVER3.py' or 'python3 SERVER3.py' and press 'enter'. You should read a message that says 'Listening on: 8888'. You have connected to the server.
4) Open another cmd window
5) Using the 'cd' command navigate to the location that you have saved the 'AfreenAlvinCDE2' repository folder.
6) Type 'py TCPCLientCode.py' and press 'enter'. A GUI should appear in the form of a pop-up box that requests information about the employee's first name, last name, age, and employed status.
7) Fill the fields in and press 'Submit'. A HTML webpage should automatically appear that contains an overview of the data that you have just entered. 
8) Navigate to the cmd window that is connected to the server. You should be able to view messages that relate to a connection to the client being established, the employee information that you ahve submitted, and a client connection closed message once the information was recieved. 
9) Navigate to the cmd window that is connected to TCPCLientCode. You should be able to view messages that relate to the data that you have submitted in the GUI, 'Sending your data' confirmation message that indicates that the data is being sent from client to server, and the 'from server...' message that retrieves the information recieved by the server. 

To test for multi-threading by sending information from multiple clients to 1 server, follow the steps to 'send employee information from 1 client to the server' but after step 6, repeat steps 4-6 depending on the number of clients you want to create, and then continue from step seven onwards. Each time that there is a client connection established message in the server cmd window, there should be a different source port each time, e.g. 'Connection from ('138.0.0.2', 54650)', 'Connection from ('138.0.0.2', 54789)'. The different source ports indicate the different clients. 
