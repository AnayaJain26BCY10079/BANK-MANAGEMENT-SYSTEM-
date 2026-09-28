# ============================================================
#              BANK MANAGEMENT SYSTEM
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import random

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ============================================================
#                       COLORS
# ============================================================

BG_COLOR = "#F4F7FB"
NAVY = "#14213D"
BLUE = "#2563EB"
LIGHT_BLUE = "#E8F0FE"
WHITE = "#FFFFFF"
GREEN = "#16A34A"
RED = "#DC2626"
ORANGE = "#F59E0B"
TEXT = "#1F2937"
GRAY = "#6B7280"
BORDER = "#D9E1EC"


# ============================================================
#                  PRE-STORED ADMIN DATA
# ============================================================

admins = {
    "admin": "admin123"
}


# ============================================================
#                  PRE-STORED ACCOUNT DATA
# ============================================================

accounts = {

    1000000001: {
        "name": "Rahul Sharma",
        "phone": "9876543210",
        "email": "rahul@gmail.com",
        "address": "Delhi",
        "balance": 50000,
        "loan_taken": "Yes",
        "username": "rahul",
        "password": "1234"
    },

    1000000002: {
        "name": "Priya Singh",
        "phone": "9123456780",
        "email": "priya@gmail.com",
        "address": "Mumbai",
        "balance": 75000,
        "loan_taken": "No",
        "username": "priya",
        "password": "5678"
    },

    1000000003: {
        "name": "Aman Verma",
        "phone": "9988776655",
        "email": "aman@gmail.com",
        "address": "Bhopal",
        "balance": 40000,
        "loan_taken": "Yes",
        "username": "aman",
        "password": "1111"
    }
}


# ============================================================
#                     PRE-STORED LOAN DATA
# ============================================================

loans = {

    1000000001: {
        "name": "Rahul Sharma",
        "loan_taken": "Yes",
        "loan_type": "Home Loan",
        "status": "Pending",
        "months_unpaid": 3
    },

    1000000003: {
        "name": "Aman Verma",
        "loan_taken": "Yes",
        "loan_type": "Education Loan",
        "status": "Clear",
        "months_unpaid": 0
    }
}


# ============================================================
#                   PRE-STORED FEEDBACK
# ============================================================

feedbacks = [

    {
        "account_no": 1000000001,
        "feedback": "Good banking service."
    },

    {
        "account_no": 1000000002,
        "feedback": "The staff was very helpful."
    }
]


# ============================================================
#                PRE-STORED TRANSACTIONS
# ============================================================

transactions = [

    {
        "transaction_id": 101,
        "account_no": 1000000001,
        "type": "DEPOSIT",
        "amount": 50000,
        "date": "01-09-2026 10:30 AM"
    },

    {
        "transaction_id": 102,
        "account_no": 1000000001,
        "type": "WITHDRAW",
        "amount": 5000,
        "date": "05-09-2026 02:15 PM"
    },

    {
        "transaction_id": 103,
        "account_no": 1000000002,
        "type": "DEPOSIT",
        "amount": 75000,
        "date": "07-09-2026 11:00 AM"
    }
]


# ============================================================
#               LOAN DATA OVER 10 YEARS
# ============================================================
# Hypothetical data for demonstration

loan_over_years_data = {

    2017: 18,
    2018: 25,
    2019: 32,
    2020: 29,
    2021: 41,
    2022: 48,
    2023: 57,
    2024: 66,
    2025: 78,
    2026: 91
}


# ============================================================
#                     MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Bank Management System")

root.geometry("1100x720")

root.minsize(950, 650)

root.configure(bg=BG_COLOR)


# ============================================================
#                    TKINTER STYLING
# ============================================================

style = ttk.Style()

try:
    style.theme_use("clam")
except:
    pass


style.configure(
    "TButton",
    font=("Segoe UI", 11),
    padding=10
)


style.configure(
    "Treeview",
    font=("Segoe UI", 10),
    rowheight=32,
    background=WHITE,
    fieldbackground=WHITE,
    foreground=TEXT
)


style.configure(
    "Treeview.Heading",
    font=("Segoe UI", 10, "bold"),
    background=NAVY,
    foreground=WHITE,
    padding=8
)


style.map(
    "Treeview",
    background=[
        ("selected", "#DCE8FF")
    ],
    foreground=[
        ("selected", TEXT)
    ]
)


# ============================================================
#                     HELPER FUNCTIONS
# ============================================================

def clear_window():

    for widget in root.winfo_children():
        widget.destroy()


def header(parent, title, subtitle=""):

    frame = tk.Frame(
        parent,
        bg=NAVY,
        height=100
    )

    frame.pack(
        fill="x"
    )

    frame.pack_propagate(False)

    tk.Label(
        frame,
        text=title,
        font=("Segoe UI", 24, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(
        anchor="w",
        padx=35,
        pady=(18, 0)
    )

    if subtitle:

        tk.Label(
            frame,
            text=subtitle,
            font=("Segoe UI", 10),
            bg=NAVY,
            fg="#D7E3FF"
        ).pack(
            anchor="w",
            padx=37,
            pady=(2, 0)
        )

    return frame


def create_button(
        parent,
        text,
        command,
        color=BLUE,
        width=22):

    button = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Segoe UI", 11, "bold"),
        bg=color,
        fg=WHITE,
        activebackground=color,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        cursor="hand2",
        width=width,
        pady=10
    )

    return button


def create_card(parent):

    card = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    return card


def close_window(window):

    window.destroy()


# ============================================================
#                   ACCOUNT NUMBER
# ============================================================

def generate_account_number():

    while True:

        number = random.randint(
            1000000000,
            9999999999
        )

        if number not in accounts:

            return number


# ============================================================
#                  TRANSACTION ID
# ============================================================

def generate_transaction_id():

    while True:

        number = random.randint(
            1000,
            9999
        )

        exists = False

        for transaction in transactions:

            if transaction["transaction_id"] == number:

                exists = True

                break

        if not exists:

            return number


# ============================================================
#                    TABLE WINDOW
# ============================================================

def create_table_window(
        title,
        columns,
        rows):

    window = tk.Toplevel(root)

    window.title(title)

    window.geometry("950x550")

    window.configure(
        bg=BG_COLOR
    )

    header(
        window,
        title,
        "Bank Management System"
    )

    container = tk.Frame(
        window,
        bg=BG_COLOR
    )

    container.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=25
    )

    table_frame = tk.Frame(
        container,
        bg=WHITE
    )

    table_frame.pack(
        fill="both",
        expand=True
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    for column in columns:

        tree.heading(
            column,
            text=column
        )

        tree.column(
            column,
            width=150,
            anchor="center"
        )

    scrollbar_y = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=tree.yview
    )

    scrollbar_x = ttk.Scrollbar(
        table_frame,
        orient="horizontal",
        command=tree.xview
    )

    tree.configure(
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set
    )

    tree.pack(
        side="top",
        fill="both",
        expand=True
    )

    scrollbar_y.pack(
        side="right",
        fill="y"
    )

    scrollbar_x.pack(
        side="bottom",
        fill="x"
    )

    for row in rows:

        tree.insert(
            "",
            "end",
            values=row
        )

    return window


# ============================================================
#                    ACCOUNT DETAILS
# ============================================================

def view_account(account_no):

    data = accounts[account_no]

    rows = [

        (
            "Account Number",
            account_no
        ),

        (
            "Account Holder",
            data["name"]
        ),

        (
            "Phone Number",
            data["phone"]
        ),

        (
            "Email",
            data["email"]
        ),

        (
            "Address",
            data["address"]
        ),

        (
            "Current Balance",
            f"₹ {data['balance']:,.2f}"
        ),

        (
            "Loan Taken",
            data["loan_taken"]
        )
    ]

    create_table_window(
        "ACCOUNT DETAILS",
        ["FIELD", "DETAIL"],
        rows
    )


# ============================================================
#                     UPDATE NAME
# ============================================================

def update_name(account_no):

    new_name = simpledialog.askstring(
        "Update Name",
        "Enter new name:",
        parent=root
    )

    if not new_name:
        return

    accounts[account_no]["name"] = new_name

    if account_no in loans:

        loans[account_no]["name"] = new_name

    messagebox.showinfo(
        "Success",
        "Name updated successfully."
    )


# ============================================================
#                     UPDATE EMAIL
# ============================================================

def update_email(account_no):

    new_email = simpledialog.askstring(
        "Update Email",
        "Enter new email:",
        parent=root
    )

    if not new_email:
        return

    accounts[account_no]["email"] = new_email

    messagebox.showinfo(
        "Success",
        "Email updated successfully."
    )


# ============================================================
#                  UPDATE PHONE NUMBER
# ============================================================

def update_phone(account_no):

    new_phone = simpledialog.askstring(
        "Update Phone",
        "Enter 10-digit phone number:",
        parent=root
    )

    if not new_phone:
        return

    if not new_phone.isdigit():

        messagebox.showerror(
            "Invalid Number",
            "Phone number must contain digits only."
        )

        return

    if len(new_phone) != 10:

        messagebox.showerror(
            "Invalid Number",
            "Phone number must contain exactly 10 digits."
        )

        return

    accounts[account_no]["phone"] = new_phone

    messagebox.showinfo(
        "Success",
        "Phone number updated successfully."
    )


# ============================================================
#                     UPDATE ADDRESS
# ============================================================

def update_address(account_no):

    new_address = simpledialog.askstring(
        "Update Address",
        "Enter new address:",
        parent=root
    )

    if not new_address:
        return

    accounts[account_no]["address"] = new_address

    messagebox.showinfo(
        "Success",
        "Address updated successfully."
    )


# ============================================================
#                      FEEDBACK
# ============================================================

def give_feedback(account_no):

    feedback = simpledialog.askstring(
        "Customer Feedback",
        "Enter your feedback:",
        parent=root
    )

    if not feedback:
        return

    feedbacks.append({

        "account_no": account_no,
        "feedback": feedback
    })

    messagebox.showinfo(
        "Thank You",
        "Your feedback has been submitted successfully."
    )


# ============================================================
#                    LOAN STATUS
# ============================================================

def view_loan_status(account_no):

    if account_no not in loans:

        messagebox.showinfo(
            "Loan Status",
            "No loan data found for this account."
        )

        return

    data = loans[account_no]

    rows = [

        (
            "Account Number",
            account_no
        ),

        (
            "Account Holder",
            data["name"]
        ),

        (
            "Loan Taken",
            data["loan_taken"]
        ),

        (
            "Loan Type",
            data["loan_type"]
        ),

        (
            "Loan Status",
            data["status"]
        ),

        (
            "Months Unpaid",
            data["months_unpaid"]
        )
    ]

    create_table_window(
        "LOAN STATUS",
        ["FIELD", "DETAIL"],
        rows
    )


# ============================================================
#                 LOAN GRAPH WINDOW
# ============================================================

def loan_over_years():

    window = tk.Toplevel(root)

    window.title(
        "Loans Taken Over The Years"
    )

    window.geometry("900x620")

    window.configure(
        bg=BG_COLOR
    )

    header(
        window,
        "LOANS TAKEN OVER THE YEARS",
        "Hypothetical 10-year banking data"
    )

    # --------------------------------------------------------
    # Graph
    # --------------------------------------------------------

    years = list(
        loan_over_years_data.keys()
    )

    loan_count = list(
        loan_over_years_data.values()
    )

    graph_frame = tk.Frame(
        window,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    graph_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=20
    )

    figure = Figure(
        figsize=(8, 5),
        dpi=100
    )

    axis = figure.add_subplot(111)

    axis.bar(
        years,
        loan_count,
        width=0.65
    )

    axis.set_title(
        "Loans Taken From 2017 to 2026",
        fontsize=15,
        fontweight="bold"
    )

    axis.set_xlabel(
        "Year",
        fontsize=11
    )

    axis.set_ylabel(
        "Number of Loans",
        fontsize=11
    )

    axis.set_xticks(years)

    axis.grid(
        axis="y",
        alpha=0.25
    )

    # Display values on bars

    for year, count in zip(
        years,
        loan_count
    ):

        axis.text(
            year,
            count + 1,
            str(count),
            ha="center",
            fontsize=9
        )

    figure.tight_layout()

    canvas = FigureCanvasTkAgg(
        figure,
        master=graph_frame
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )

    # --------------------------------------------------------
    # Data table below graph
    # --------------------------------------------------------

    table_frame = tk.Frame(
        window,
        bg=WHITE
    )

    table_frame.pack(
        fill="x",
        padx=25,
        pady=(0, 20)
    )

    tree = ttk.Treeview(
        table_frame,
        columns=("Year", "Loans"),
        show="headings",
        height=3
    )

    tree.heading(
        "Year",
        text="YEAR"
    )

    tree.heading(
        "Loans",
        text="LOANS TAKEN"
    )

    tree.column(
        "Year",
        width=150,
        anchor="center"
    )

    tree.column(
        "Loans",
        width=150,
        anchor="center"
    )

    for year, count in zip(
        years,
        loan_count
    ):

        tree.insert(
            "",
            "end",
            values=(year, count)
        )

    tree.pack(
        fill="x"
    )


# ============================================================
#                 DEPOSIT / WITHDRAW WINDOW
# ============================================================

def money_deposit_withdraw(account_no):

    window = tk.Toplevel(root)

    window.title(
        "Deposit / Withdraw Money"
    )

    window.geometry("450x430")

    window.configure(
        bg=BG_COLOR
    )

    header(
        window,
        "MONEY TRANSACTION",
        "Deposit or withdraw money"
    )

    card = create_card(
        window
    )

    card.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    tk.Label(
        card,
        text=f"Current Balance: ₹ {accounts[account_no]['balance']:,.2f}",
        font=("Segoe UI", 14, "bold"),
        bg=WHITE,
        fg=NAVY
    ).pack(
        pady=25
    )

    tk.Label(
        card,
        text="Select Transaction",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        pady=(5, 5)
    )

    transaction_type = tk.StringVar(
        value="Deposit"
    )

    combo = ttk.Combobox(
        card,
        textvariable=transaction_type,
        values=[
            "Deposit",
            "Withdraw"
        ],
        state="readonly",
        width=25,
        font=("Segoe UI", 11)
    )

    combo.pack(
        pady=10
    )

    tk.Label(
        card,
        text="Enter Amount",
        font=("Segoe UI", 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        pady=(15, 5)
    )

    amount_entry = tk.Entry(
        card,
        font=("Segoe UI", 12),
        width=28,
        relief="solid",
        bd=1
    )

    amount_entry.pack(
        pady=10
    )

    def process_transaction():

        try:

            amount = float(
                amount_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Amount",
                "Please enter a valid amount.",
                parent=window
            )

            return

        if amount <= 0:

            messagebox.showerror(
                "Invalid Amount",
                "Amount must be greater than zero.",
                parent=window
            )

            return

        selected = transaction_type.get()

        if selected == "Deposit":

            accounts[account_no]["balance"] += amount

            transaction_type_text = "DEPOSIT"

        else:

            if amount > accounts[account_no]["balance"]:

                messagebox.showerror(
                    "Insufficient Balance",
                    "You do not have sufficient balance.",
                    parent=window
                )

                return

            accounts[account_no]["balance"] -= amount

            transaction_type_text = "WITHDRAW"

        transactions.append({

            "transaction_id":
                generate_transaction_id(),

            "account_no":
                account_no,

            "type":
                transaction_type_text,

            "amount":
                amount,

            "date":
                datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                )
        })

        messagebox.showinfo(
            "Transaction Successful",
            f"{selected} successful!\n\n"
            f"Amount: ₹ {amount:,.2f}\n"
            f"New Balance: ₹ "
            f"{accounts[account_no]['balance']:,.2f}",
            parent=window
        )

        window.destroy()

    create_button(
        card,
        "PROCESS TRANSACTION",
        process_transaction,
        GREEN,
        25
    ).pack(
        pady=25
    )


# ============================================================
#                       PASSBOOK
# ============================================================

def view_passbook(account_no):

    rows = []

    for transaction in transactions:

        if transaction["account_no"] == account_no:

            rows.append(

                (
                    transaction["transaction_id"],
                    transaction["type"],
                    f"₹ {transaction['amount']:,.2f}",
                    transaction["date"]
                )
            )

    if not rows:

        messagebox.showinfo(
            "Passbook",
            "No transactions found."
        )

        return

    create_table_window(

        "PASSBOOK",

        [
            "TRANSACTION ID",
            "TYPE",
            "AMOUNT",
            "DATE"
        ],

        rows
    )


# ============================================================
#                 ADMIN: ADD NEW ACCOUNT
# ============================================================

def add_new_account():

    window = tk.Toplevel(root)

    window.title(
        "Add New Account"
    )

    window.geometry(
        "550x650"
    )

    window.configure(
        bg=BG_COLOR
    )

    header(
        window,
        "ADD NEW ACCOUNT",
        "Create a new bank account"
    )

    card = create_card(
        window
    )

    card.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=20
    )

    fields = {}

    field_names = [

        "Name",
        "Phone",
        "Email",
        "Address",
        "Initial Balance"
    ]

    for field in field_names:

        tk.Label(
            card,
            text=field,
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=35,
            pady=(8, 2)
        )

        entry = tk.Entry(
            card,
            font=("Segoe UI", 11),
            width=38,
            relief="solid",
            bd=1
        )

        entry.pack(
            padx=35,
            pady=(0, 5)
        )

        fields[field] = entry

    tk.Label(
        card,
        text="Loan Taken",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(8, 2)
    )

    loan_var = tk.StringVar(
        value="No"
    )

    loan_combo = ttk.Combobox(
        card,
        textvariable=loan_var,
        values=["Yes", "No"],
        state="readonly",
        width=35
    )

    loan_combo.pack(
        padx=35,
        pady=5
    )

    def save_account():

        name = fields["Name"].get().strip()
        phone = fields["Phone"].get().strip()
        email = fields["Email"].get().strip()
        address = fields["Address"].get().strip()
        balance_text = fields["Initial Balance"].get().strip()

        if not name:

            messagebox.showerror(
                "Error",
                "Name cannot be empty.",
                parent=window
            )

            return

        if not phone.isdigit() or len(phone) != 10:

            messagebox.showerror(
                "Error",
                "Phone number must contain exactly 10 digits.",
                parent=window
            )

            return

        if not email:

            messagebox.showerror(
                "Error",
                "Email cannot be empty.",
                parent=window
            )

            return

        if not address:

            messagebox.showerror(
                "Error",
                "Address cannot be empty.",
                parent=window
            )

            return

        try:

            balance = float(
                balance_text
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid initial balance.",
                parent=window
            )

            return

        if balance < 0:

            messagebox.showerror(
                "Error",
                "Balance cannot be negative.",
                parent=window
            )

            return

        account_no = generate_account_number()

        username = (
            name.lower()
            .replace(" ", "")
        )

        original_username = username

        number = 1

        while True:

            exists = False

            for data in accounts.values():

                if data["username"] == username:

                    exists = True
                    break

            if not exists:
                break

            username = (
                original_username
                + str(number)
            )

            number += 1

        password = str(
            random.randint(1000, 9999)
        )

        accounts[account_no] = {

            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "balance": balance,
            "loan_taken": loan_var.get(),
            "username": username,
            "password": password
        }

        messagebox.showinfo(

            "Account Created",

            f"Account created successfully!\n\n"
            f"Account Number: {account_no}\n"
            f"Username: {username}\n"
            f"Password: {password}",

            parent=window
        )

        window.destroy()

    create_button(
        card,
        "CREATE ACCOUNT",
        save_account,
        GREEN,
        25
    ).pack(
        pady=20
    )


# ============================================================
#                  ADMIN: VIEW LOAN DATA
# ============================================================

def view_all_loans():

    rows = []

    for account_no, data in loans.items():

        rows.append(

            (
                account_no,
                data["name"],
                data["loan_type"],
                data["status"],
                data["months_unpaid"]
            )
        )

    if not rows:

        messagebox.showinfo(
            "Loan Data",
            "No loan data available."
        )

        return

    create_table_window(

        "ALL LOAN DETAILS",

        [
            "ACCOUNT NO.",
            "NAME",
            "LOAN TYPE",
            "STATUS",
            "MONTHS UNPAID"
        ],

        rows
    )


# ============================================================
#                 ADMIN: UPDATE LOAN STATUS
# ============================================================

def update_loan_status():

    account_no = simpledialog.askinteger(
        "Update Loan Status",
        "Enter account number:",
        parent=root
    )

    if account_no is None:
        return

    if account_no not in loans:

        messagebox.showerror(
            "Error",
            "Loan record not found."
        )

        return

    current = loans[account_no]["status"]

    status = simpledialog.askstring(

        "Update Status",

        f"Current status: {current}\n\n"
        "Enter new status:\n"
        "Clear / Pending",

        parent=root
    )

    if not status:
        return

    status = status.strip().capitalize()

    if status not in ["Clear", "Pending"]:

        messagebox.showerror(
            "Invalid Status",
            "Please enter Clear or Pending."
        )

        return

    loans[account_no]["status"] = status

    messagebox.showinfo(
        "Success",
        "Loan status updated successfully."
    )


# ============================================================
#                 ADMIN: LOAN DEFAULTERS
# ============================================================

def view_loan_defaulters():

    months = simpledialog.askinteger(

        "Loan Defaulters",

        "Show accounts with unpaid months >=:",

        minvalue=0,

        parent=root
    )

    if months is None:
        return

    rows = []

    for account_no, data in loans.items():

        if data["months_unpaid"] >= months:

            rows.append(

                (
                    account_no,
                    data["name"],
                    data["loan_type"],
                    data["status"],
                    data["months_unpaid"]
                )
            )

    if not rows:

        messagebox.showinfo(
            "Loan Defaulters",
            "No loan defaulters found."
        )

        return

    create_table_window(

        "LOAN DEFAULTERS",

        [
            "ACCOUNT NO.",
            "NAME",
            "LOAN TYPE",
            "STATUS",
            "MONTHS UNPAID"
        ],

        rows
    )


# ============================================================
#                  ADMIN: VIEW FEEDBACK
# ============================================================

def view_feedbacks():

    rows = []

    for feedback in feedbacks:

        rows.append(

            (
                feedback["account_no"],
                feedback["feedback"]
            )
        )

    if not rows:

        messagebox.showinfo(
            "Feedback",
            "No feedback available."
        )

        return

    create_table_window(

        "CUSTOMER FEEDBACK",

        [
            "ACCOUNT NUMBER",
            "FEEDBACK"
        ],

        rows
    )


# ============================================================
#                  ADMIN: ADD LOAN DATA
# ============================================================

def add_loan_data():

    window = tk.Toplevel(root)

    window.title(
        "Add Loan Data"
    )

    window.geometry(
        "500x520"
    )

    window.configure(
        bg=BG_COLOR
    )

    header(
        window,
        "ADD LOAN DATA",
        "Add a loan record to an account"
    )

    card = create_card(
        window
    )

    card.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    tk.Label(
        card,
        text="Account Number",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(25, 5)
    )

    account_entry = tk.Entry(
        card,
        font=("Segoe UI", 11),
        width=35
    )

    account_entry.pack(
        padx=35
    )

    tk.Label(
        card,
        text="Loan Type",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(15, 5)
    )

    loan_entry = tk.Entry(
        card,
        font=("Segoe UI", 11),
        width=35
    )

    loan_entry.pack(
        padx=35
    )

    tk.Label(
        card,
        text="Status",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(15, 5)
    )

    status_var = tk.StringVar(
        value="Pending"
    )

    status_combo = ttk.Combobox(
        card,
        textvariable=status_var,
        values=["Clear", "Pending"],
        state="readonly",
        width=32
    )

    status_combo.pack(
        padx=35
    )

    tk.Label(
        card,
        text="Months Unpaid",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(15, 5)
    )

    months_entry = tk.Entry(
        card,
        font=("Segoe UI", 11),
        width=35
    )

    months_entry.pack(
        padx=35
    )

    def save_loan():

        try:

            account_no = int(
                account_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Invalid account number.",
                parent=window
            )

            return

        if account_no not in accounts:

            messagebox.showerror(
                "Error",
                "Account does not exist.",
                parent=window
            )

            return

        loan_type = loan_entry.get().strip()

        if not loan_type:

            messagebox.showerror(
                "Error",
                "Loan type cannot be empty.",
                parent=window
            )

            return

        try:

            months = int(
                months_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid number of months.",
                parent=window
            )

            return

        if months < 0:

            messagebox.showerror(
                "Error",
                "Months cannot be negative.",
                parent=window
            )

            return

        loans[account_no] = {

            "name":
                accounts[account_no]["name"],

            "loan_taken":
                "Yes",

            "loan_type":
                loan_type,

            "status":
                status_var.get(),

            "months_unpaid":
                months
        }

        accounts[account_no]["loan_taken"] = "Yes"

        messagebox.showinfo(
            "Success",
            "Loan data added successfully.",
            parent=window
        )

        window.destroy()

    create_button(
        card,
        "ADD LOAN",
        save_loan,
        GREEN,
        22
    ).pack(
        pady=25
    )


# ============================================================
#                ADMIN: DEPOSIT / WITHDRAW
# ============================================================

def admin_transaction():

    account_no = simpledialog.askinteger(

        "Account Number",

        "Enter account number:",

        parent=root
    )

    if account_no is None:
        return

    if account_no not in accounts:

        messagebox.showerror(
            "Error",
            "Account not found."
        )

        return

    money_deposit_withdraw(
        account_no
    )


# ============================================================
#                    USER DASHBOARD
# ============================================================

def user_dashboard(account_no):

    clear_window()

    data = accounts[account_no]

    header(
        root,
        "USER DASHBOARD",
        f"Welcome, {data['name']}  •  A/C {account_no}"
    )

    # --------------------------------------------------------
    # Top balance card
    # --------------------------------------------------------

    balance_frame = tk.Frame(
        root,
        bg=BG_COLOR
    )

    balance_frame.pack(
        fill="x",
        padx=35,
        pady=25
    )

    balance_card = tk.Frame(
        balance_frame,
        bg=NAVY,
        height=110
    )

    balance_card.pack(
        fill="x"
    )

    balance_card.pack_propagate(False)

    tk.Label(
        balance_card,
        text="CURRENT BALANCE",
        font=("Segoe UI", 11, "bold"),
        bg=NAVY,
        fg="#C8D7F5"
    ).pack(
        pady=(18, 0)
    )

    tk.Label(
        balance_card,
        text=f"₹ {data['balance']:,.2f}",
        font=("Segoe UI", 27, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(
        pady=2
    )

    # --------------------------------------------------------
    # Buttons
    # --------------------------------------------------------

    container = tk.Frame(
        root,
        bg=BG_COLOR
    )

    container.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=5
    )

    buttons = [

        (
            "👤  View Account",
            lambda: view_account(account_no),
            BLUE
        ),

        (
            "✏  Update Name",
            lambda: update_name(account_no),
            BLUE
        ),

        (
            "✉  Update Email",
            lambda: update_email(account_no),
            BLUE
        ),

        (
            "☎  Update Phone",
            lambda: update_phone(account_no),
            BLUE
        ),

        (
            "⌂  Update Address",
            lambda: update_address(account_no),
            BLUE
        ),

        (
            "★  Give Feedback",
            lambda: give_feedback(account_no),
            ORANGE
        ),

        (
            "🏦  View Loan Status",
            lambda: view_loan_status(account_no),
            GREEN
        ),

        (
            "📊  Loans Over 10 Years",
            loan_over_years,
            GREEN
        ),

        (
            "💰  Deposit / Withdraw",
            lambda: money_deposit_withdraw(account_no),
            GREEN
        ),

        (
            "📒  View Passbook",
            lambda: view_passbook(account_no),
            BLUE
        )
    ]

    for index, item in enumerate(buttons):

        row = index // 2
        column = index % 2

        button = create_button(
            container,
            item[0],
            item[1],
            item[2],
            27
        )

        button.grid(
            row=row,
            column=column,
            padx=12,
            pady=10,
            sticky="ew"
        )

    container.grid_columnconfigure(
        0,
        weight=1
    )

    container.grid_columnconfigure(
        1,
        weight=1
    )

    logout = create_button(
        root,
        "LOGOUT",
        main_screen,
        RED,
        20
    )

    logout.pack(
        pady=20
    )


# ============================================================
#                    ADMIN DASHBOARD
# ============================================================

def admin_dashboard():

    clear_window()

    header(
        root,
        "ADMIN DASHBOARD",
        "Manage accounts, loans, transactions and feedback"
    )

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    stats_frame = tk.Frame(
        root,
        bg=BG_COLOR
    )

    stats_frame.pack(
        fill="x",
        padx=35,
        pady=25
    )

    total_accounts = len(accounts)

    total_loans = len(loans)

    total_feedback = len(feedbacks)

    stats = [

        (
            "TOTAL ACCOUNTS",
            total_accounts,
            BLUE
        ),

        (
            "ACTIVE LOANS",
            total_loans,
            GREEN
        ),

        (
            "FEEDBACK",
            total_feedback,
            ORANGE
        )
    ]

    for index, item in enumerate(stats):

        card = tk.Frame(
            stats_frame,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=index,
            padx=8,
            sticky="nsew"
        )

        stats_frame.grid_columnconfigure(
            index,
            weight=1
        )

        tk.Label(
            card,
            text=item[0],
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=GRAY
        ).pack(
            pady=(15, 3)
        )

        tk.Label(
            card,
            text=str(item[1]),
            font=("Segoe UI", 25, "bold"),
            bg=WHITE,
            fg=item[2]
        ).pack(
            pady=(0, 15)
        )

    # --------------------------------------------------------
    # Admin Buttons
    # --------------------------------------------------------

    container = tk.Frame(
        root,
        bg=BG_COLOR
    )

    container.pack(
        fill="both",
        expand=True,
        padx=35
    )

    buttons = [

        (
            "➕  Add New Account",
            add_new_account,
            BLUE
        ),

        (
            "🏦  View Loan Data",
            view_all_loans,
            GREEN
        ),

        (
            "🔄  Update Loan Status",
            update_loan_status,
            GREEN
        ),

        (
            "⚠  View Loan Defaulters",
            view_loan_defaulters,
            RED
        ),

        (
            "★  View Feedback",
            view_feedbacks,
            ORANGE
        ),

        (
            "➕  Add Loan Data",
            add_loan_data,
            GREEN
        ),

        (
            "📊  Loans Over 10 Years",
            loan_over_years,
            BLUE
        ),

        (
            "💰  Deposit / Withdraw",
            admin_transaction,
            BLUE
        )
    ]

    for index, item in enumerate(buttons):

        row = index // 2
        column = index % 2

        button = create_button(
            container,
            item[0],
            item[1],
            item[2],
            27
        )

        button.grid(
            row=row,
            column=column,
            padx=12,
            pady=9,
            sticky="ew"
        )

    container.grid_columnconfigure(
        0,
        weight=1
    )

    container.grid_columnconfigure(
        1,
        weight=1
    )

    create_button(
        root,
        "LOGOUT",
        main_screen,
        RED,
        20
    ).pack(
        pady=18
    )


# ============================================================
#                    ADMIN LOGIN
# ============================================================

def admin_login():

    window = tk.Toplevel(root)

    window.title(
        "Admin Login"
    )

    window.geometry(
        "450x430"
    )

    window.configure(
        bg=BG_COLOR
    )

    header(
        window,
        "ADMIN LOGIN",
        "Secure administrator access"
    )

    card = create_card(
        window
    )

    card.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    tk.Label(
        card,
        text="Username",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(30, 5)
    )

    username_entry = tk.Entry(
        card,
        font=("Segoe UI", 12),
        width=30
    )

    username_entry.pack(
        padx=35
    )

    tk.Label(
        card,
        text="Password",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(20, 5)
    )

    password_entry = tk.Entry(
        card,
        font=("Segoe UI", 12),
        width=30,
        show="*"
    )

    password_entry.pack(
        padx=35
    )

    def login():

        username = username_entry.get()

        password = password_entry.get()

        if (
            username in admins
            and admins[username] == password
        ):

            window.destroy()

            admin_dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password.",
                parent=window
            )

    create_button(
        card,
        "LOGIN",
        login,
        BLUE,
        20
    ).pack(
        pady=30
    )

    tk.Label(
        card,
        text="Default: admin / admin123",
        font=("Segoe UI", 9),
        bg=WHITE,
        fg=GRAY
    ).pack()


# ============================================================
#                    USER LOGIN
# ============================================================

def user_login():

    window = tk.Toplevel(root)

    window.title(
        "User Login"
    )

    window.geometry(
        "450x460"
    )

    window.configure(
        bg=BG_COLOR
    )

    header(
        window,
        "USER LOGIN",
        "Access your bank account"
    )

    card = create_card(
        window
    )

    card.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=25
    )

    tk.Label(
        card,
        text="Username",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(25, 5)
    )

    username_entry = tk.Entry(
        card,
        font=("Segoe UI", 12),
        width=30
    )

    username_entry.pack(
        padx=35
    )

    tk.Label(
        card,
        text="Password",
        font=("Segoe UI", 10, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=35,
        pady=(20, 5)
    )

    password_entry = tk.Entry(
        card,
        font=("Segoe UI", 12),
        width=30,
        show="*"
    )

    password_entry.pack(
        padx=35
    )

    def login():

        username = username_entry.get()

        password = password_entry.get()

        for account_no, data in accounts.items():

            if (
                data["username"] == username
                and data["password"] == password
            ):

                window.destroy()

                user_dashboard(
                    account_no
                )

                return

        messagebox.showerror(
            "Login Failed",
            "Invalid username or password.",
            parent=window
        )

    create_button(
        card,
        "LOGIN",
        login,
        BLUE,
        20
    ).pack(
        pady=25
    )

    tk.Label(
        card,
        text="Sample login: rahul / 1234",
        font=("Segoe UI", 9),
        bg=WHITE,
        fg=GRAY
    ).pack()

    tk.Label(
        card,
        text="Other users: priya / 5678   |   aman / 1111",
        font=("Segoe UI", 9),
        bg=WHITE,
        fg=GRAY
    ).pack(
        pady=3
    )


# ============================================================
#                     MAIN SCREEN
# ============================================================

def main_screen():

    clear_window()

    # --------------------------------------------------------
    # Main header
    # --------------------------------------------------------

    top = tk.Frame(
        root,
        bg=NAVY,
        height=180
    )

    top.pack(
        fill="x"
    )

    top.pack_propagate(False)

    tk.Label(
        top,
        text="BANK MANAGEMENT SYSTEM",
        font=("Segoe UI", 30, "bold"),
        bg=NAVY,
        fg=WHITE
    ).pack(
        pady=(35, 5)
    )

    tk.Label(
        top,
        text="Secure • Simple • Smart Banking",
        font=("Segoe UI", 12),
        bg=NAVY,
        fg="#D7E3FF"
    ).pack()


    # --------------------------------------------------------
    # Welcome card
    # --------------------------------------------------------

    content = tk.Frame(
        root,
        bg=BG_COLOR
    )

    content.pack(
        fill="both",
        expand=True,
        padx=80,
        pady=35
    )

    card = create_card(
        content
    )

    card.pack(
        fill="both",
        expand=True
    )

    tk.Label(
        card,
        text="Welcome!",
        font=("Segoe UI", 25, "bold"),
        bg=WHITE,
        fg=NAVY
    ).pack(
        pady=(35, 5)
    )

    tk.Label(
        card,
        text=(
            "Choose an option to continue\n"
            "to the Bank Management System"
        ),
        font=("Segoe UI", 11),
        bg=WHITE,
        fg=GRAY,
        justify="center"
    ).pack(
        pady=(0, 25)
    )

    create_button(
        card,
        "🔐   ADMIN LOGIN",
        admin_login,
        NAVY,
        28
    ).pack(
        pady=8
    )

    create_button(
        card,
        "👤   USER LOGIN",
        user_login,
        BLUE,
        28
    ).pack(
        pady=8
    )

    create_button(
        card,
        "✕   EXIT",
        root.destroy,
        RED,
        28
    ).pack(
        pady=8
    )

    tk.Label(
        card,
        text="Python Only Project • No MySQL",
        font=("Segoe UI", 9),
        bg=WHITE,
        fg=GRAY
    ).pack(
        pady=25
    )


# ============================================================
#                     START PROGRAM
# ============================================================

main_screen()

root.mainloop()