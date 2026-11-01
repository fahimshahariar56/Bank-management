# 🏦 Bank Management System

> **A console-based Bank Management System built with Python and JSON for learning Object-Oriented Programming, file handling, data management, and basic banking operations.**

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/JSON-Database-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON">
  <img src="https://img.shields.io/badge/OOP-Python-FFCA28?style=for-the-badge&logo=python&logoColor=black" alt="OOP">
  <img src="https://img.shields.io/badge/Status-In%20Development-22C55E?style=for-the-badge" alt="Status">

</p>

---

## 📌 Overview

**Bank Management System** is a Python-based console application designed to simulate basic banking operations.

The project uses **Object-Oriented Programming (OOP)** with a `Bank` class and stores account information in a local **JSON file** instead of using a traditional SQL database.

It is mainly built as a learning project to practice:

- 🐍 Python
- 🧱 Object-Oriented Programming
- 📦 Lists & Dictionaries
- 📄 JSON File Handling
- 🔐 PIN-based authentication
- 💰 Banking operations
- 🔄 Data persistence
- 🧩 Modular methods

---

## ✨ Features

### 👤 Account Management

- ➕ Create a new bank account
- 👁️ View account details
- ✏️ Update account information
- 🗑️ Delete an account
- 🔎 Search account
- 💳 Check account balance

### 💰 Money Management

- 💵 Deposit money
- 💸 Withdraw money
- 🔄 Transfer money between accounts

### 🔐 Security

- 🔑 PIN-based account verification
- 🔄 Change account PIN
- ✅ PIN confirmation during PIN change

### 📊 Transaction Management

- 🧾 Transaction history
- 📑 Account statement
- 💰 Balance tracking
- 🔄 Transfer records

### 💾 Data Storage

Account information is stored locally inside:

```text
Data.json
```

The application automatically loads existing JSON data when the program starts and updates the file after account-related changes.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 📄 JSON | Local data storage |
| 🧱 OOP | Application structure |
| 📦 Lists | Account & transaction data |
| 🗂️ Dictionaries | Account records |
| 📁 pathlib | File existence checking |
| 🎲 random | Account number generation |
| 🔤 string | Numeric account number generation |

---

## 📂 Project Structure

```text
BankManagement/
│
├── 📄 main.py
├── 🗃️ Data.json
└── 📘 README.md
```

### `main.py`

Contains the complete Bank Management System including:

- `Bank` class
- Account operations
- Money operations
- Transaction handling
- PIN management
- Console menu

### `Data.json`

Works as the local database where account information is stored.

---

## 🧱 Core Class

The project is centered around a single `Bank` class:

```python
class Bank:
    Database = 'Data.json'
    data = []
```

The class contains methods for different banking operations.

### Available Methods

```text
create_account()
view_account()
deposit_money()
withdraw_money()
update_account()
delete_account()
check_balance()
transfer_money()
transaction_history()
change_pin()
search_account()
account_statement()
```

---

## 🔄 How It Works

```text
              ┌─────────────────────┐
              │   Bank Management   │
              │       System        │
              └──────────┬──────────┘
                         │
              ┌──────────▼──────────┐
              │      main.py        │
              └──────────┬──────────┘
                         │
             ┌───────────▼───────────┐
             │      Bank Class       │
             └───────────┬───────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   Account Ops      Money Ops       Security
        │                │                │
        ▼                ▼                ▼
 Create/View       Deposit/Withdraw   PIN Change
 Update/Delete       Transfer         PIN Verify
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  ┌──────────────┐
                  │   Data.json  │
                  │ Local Storage│
                  └──────────────┘
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/fahimshahariar56/Bank-management.git
```

### 2️⃣ Navigate to the Project

```bash
cd Bank-management
```

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 🖥️ Application Menu

When the application starts, you will see:

```text
Welcome to the Bank Management System

Please select an option:

1. Create a new account
2. View account details
3. Deposit money
4. Withdraw money
5. Update account information
6. Delete account
7. Check account balance
8. Transfer money
9. Transaction history
10. Change PIN
11. Search account
12. Account statement
13. Exit
```

---

## 💾 Data Example

A basic account is stored as a JSON object:

```json
{
    "name": "Fahim",
    "age": 21,
    "gender": "Male",
    "account_number": "8686992225",
    "pin": 1234,
    "balance": 5000.0,
    "transaction": []
}
```

After a transaction, the account balance can be updated and transaction information can be stored with the account.

---

## 🧠 Concepts Practiced

This project is useful for practicing several important Python concepts.

### 🧱 Object-Oriented Programming

```python
class Bank:
    ...
```

### 🔹 Instance Methods

```python
def create_account(self):
    ...
```

### 🔹 Class Methods

The project uses a class method to update the JSON database:

```python
@classmethod
def __update_json(cls):
    ...
```

### 🔹 List Comprehension

Account lookup is performed using list comprehension:

```python
userData = [
    i for i in Bank.data
    if i['account_number'] == account_number
    and i['pin'] == pin
]
```

### 🔹 JSON File Handling

The application loads data from the JSON file and writes updated data back to it.

### 🔹 Exception Handling

The project also handles possible errors while loading the database.

---

## 🔐 Security Note

This project is intended for **educational purposes**.

The PIN is currently stored directly inside the JSON file, which is **not suitable for a real banking application**.

A production-level banking system should use:

- 🔒 Password/PIN hashing
- 🛡️ Strong authentication
- 🔑 Secure session management
- 🗄️ A real database
- 🔐 Encryption
- 📝 Audit logs
- 🚨 Rate limiting
- 🔍 Input sanitization

---

## 🚧 Future Improvements

The project can be extended with:

- [ ] 🔐 Password/PIN hashing
- [ ] 🗄️ MySQL/PostgreSQL database
- [ ] 👨‍💼 Admin dashboard
- [ ] 🧾 Detailed transaction IDs
- [ ] 🕒 Transaction timestamps
- [ ] 📊 Monthly account statements
- [ ] 📧 Email notifications
- [ ] 📱 GUI version
- [ ] 🌐 Web version
- [ ] 🔑 Better authentication system
- [ ] 🧪 Unit testing
- [ ] 📦 Better project architecture
- [ ] 📝 Logging system

---

## 🎯 Learning Goals

The main goal of this project is to build a practical Python application while improving understanding of:

```text
Python
   ↓
OOP
   ↓
Lists & Dictionaries
   ↓
JSON
   ↓
File Handling
   ↓
Data Validation
   ↓
Banking Logic
   ↓
Project Structure
```

---

## 👨‍💻 Author

### **Fahim Shahariar**

💻 CSE Student | Frontend Developer | Python Learner

I'm currently learning software development, data structures, full-stack development, and AI/ML while building practical projects.

---

## ⭐ Support

If you find this project useful for learning, consider giving the repository a ⭐ on GitHub.

---

<p align="center">

### 🏦 Built with Python & ❤️

**Learning by building real projects.**

</p>