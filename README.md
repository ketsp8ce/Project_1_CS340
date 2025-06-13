# Project_1_CS340

TLDR:

An explanation of the purpose of the CRUD Python module: CRUD stands for create, read, update, and delete. The Python portable module encodes these four functions to be flexible and portable. 
An explanation of how the module should be used, including: The module can be accessed to enable easier and smoother querying and interaction with the database.

A description of the Python driver for Mongo that was used and why it was chosen: pymongo is the official Python driver for MongoDB. It is imported into the Python module in order to access mongoDB.

An explanation of the attributes and working functionality of the CRUD operations: The user can add documents/entries to the database, read documents by querying to read documents by attribute, update information of a specific document, and delete a specific document.

A demonstration of the module’s functional operations, including:
Screenshots of the MongoDB import execution. You took these screenshots in Step 1.
Screenshots of the user authentication execution. You took these screenshots in Step 2.
Screenshots of the CRUD functionality test execution. You took these screenshots in Step 4.
See the ‘usage’ section.




About the Project/Project Title:
The following project consists of the development of a python module which can apply Create, Read, Update, and Delete (CRUD) functionality on the Austin Animal Center (AAC) Outcomes dataset in MongoDB.


Motivation:
My professor structured our class around 2 smaller projects, which ultimately relate as one web application with connectivity to a client-side user interface.  This application should be complete by the end of the class for me as well as each student. Project one focuses on developing the portable Python module and testing its functionality.


Getting Started:
Ensure all installations listed below, such as MongoDB, are installed on your local system.
Clone or download this repository (as in the one posted on github where this readME file will eventually be uploaded) to your local machine
Install the required Python packages with the following bash commands: pip install pymongo jupyter pandas
Create a user account with unique credentials, and with privileges to interact with the database


Installation:
MongoDB 6.0 – databass system for storing animal shelter data
Python 3.7+ – programming language for the module
MongoPy – python driver for MongoDB. Install with pip.
Jypiter Notebook 
Pandas – python library for data handling.Install with pip.

Usage:
Once everything is installed and configured, you can import the database using the ‘mongoimport’ tool
![image](https://github.com/user-attachments/assets/1da9c0fc-7933-4d2a-9ce1-0e60982956e9)
Next, boot up the mongo shell with the ‘mongosh’ command, then type ‘use AAC’ and ‘use admin’; then db.auth(“yourusername”, “yourpassword”). Do not use my password, which only applies to my local system. Use your account that you created in the getting started section above.
![image](https://github.com/user-attachments/assets/76c901e5-071c-45e2-9a00-3a4c605343f1)


Next, you will see a python file and an ipynb file attached in this repository. You should have then both downloaded, and ensure they are somewhere in your filesystem where they can be mutually accessible. ipynb file.
!!!!!!!!!!!!!!(IMPORTANT. The IPYNB file included currently is UNFINISHED. There seems to be a connection error which I have not resolved yet.)!!!!!!!!!!!!!!!!!

Below is some brief description of part of the process when I coded my ipynb file. This was my process for writing a client side attempt at usingt the “create” function via the python module. I also coded the read, update, and delete queries from a client side perspective:

After instantiating an instance of the AnimalShelter() module and naming it petClub in this ipynb file, I defined the contents of an entry and called it juni_document (juni is the name of my roomate’s cat), and then finally I used the “Create” method, which is defined in my .py file in order to add these contents into the AnimalShelter database.

![image](https://github.com/user-attachments/assets/b0e2be12-6e96-414d-976e-25a0ecba5995)

Again, all of these failed to connect to the network. I troubleshooted this for multiple days, and I am resolving to submit my work on time, with the intention to improve things later after feedback. At that time, I will also update this readme folder.
Contact
Hunter Marx
3312291251
hunter.marx@snhu.edu







