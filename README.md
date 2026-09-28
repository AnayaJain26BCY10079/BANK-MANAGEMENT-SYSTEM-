#Bank Management System

A Bank Management System developed in Python with a graphical user interface (GUI). The project allows users and administrators to manage bank accounts, transactions, loans, feedback, and other banking-related activities.

Features User Features User login with username and password View account details View current balance Update name Update email Update phone number Update address Deposit money Withdraw money View transaction passbook View loan status Submit customer feedback View loans taken over the years using a graph Admin Features Secure admin login Add new bank accounts View all loan details Add loan data Update loan status View loan defaulters View customer feedback Deposit and withdraw money from customer accounts View loan statistics over the years Technologies Used Python Tkinter – Graphical User Interface Matplotlib – Data visualization and loan graph Datetime – Transaction date and time Random – Generating account numbers, transaction IDs, and passwords Requirements

Make sure Python is installed on your computer.

Install Matplotlib using: pip install matplotlib

Tkinter is generally included with standard Python installations.

Project Structure Bank-Management-System/ │ ├── BANK MANAGEMENT SYSTEM.py └── README.md How to Run

Clone the Repository git clone
Open the Project Folder cd
Install Required Library pip install matplotlib
Run the Program python "BANK MANAGEMENT SYSTEM.py"
The Bank Management System GUI will open after running the program.

Login Details Admin Login Username: admin Password: admin123 Sample User Login Username: rahul Password: 1234

Other sample users: Username: priya Password: 5678

Username: aman Password: 1111

Data Storage This project uses Python dictionaries and lists to store account, loan, transaction, and feedback data.

The project does not use MySQL or any external database. Therefore, changes made while the program is running are stored only in the current program session.

Loan Graph The project includes a graphical representation of loans taken from 2017 to 2026 using Matplotlib. The graph displays the number of loans for each year along with a data table.

Validation The system includes basic input validation such as: Checking for valid phone numbers Checking for valid account numbers Preventing negative balances Checking transaction amounts Preventing withdrawals greater than the available balance Validating loan status Checking required account information Project Objective

The objective of this project is to demonstrate the use of Python programming, GUI development, data structures, functions, input validation, transaction processing, and data visualization by creating a simple banking application.

Future Improvements The project can be improved by: Adding a database such as MySQL or SQLite Adding secure password hashing Adding money-transfer functionality Adding account deletion Adding transaction search and filtering Adding PDF statement generation Adding stronger authentication and security Making data persistent between program sessions
