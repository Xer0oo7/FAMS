# 💸 FAMS - Finance Account Management System

[![GitHub stars](https://img.shields.io/github/stars/yourusername/fams?style=flat&color=yellow)](https://github.com/yourusername/fams/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/fams?style=flat&color=blue)](https://github.com/yourusername/fams/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)
![Issues](https://img.shields.io/github/issues/yourusername/fams?color=important)
![Pull Requests](https://img.shields.io/github/issues-pr/yourusername/fams?color=brightgreen)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/fams)
![Repo Size](https://img.shields.io/github/repo-size/yourusername/fams)

---

Welcome to **FAMS** – your all-in-one 🧾 **personal finance account manager** built using Python & MySQL!  
Whether you're tracking expenses, managing your budget, or analyzing financial trends with charts, FAMS makes it simple and intuitive. 🎯

---

## 📌 Features

- **Tkinter UI** – User-friendly GUI for ease of use  
- **Budget Tracking & Setting** – Stay within your spending goals  
- **Budget Overflow Warnings** – Alerts when crossing limits 🚨  
- **Graphical Analysis** –  
  - 📊 Pie charts for expense distribution  
  - 📈 Line charts for trend analysis  
- **Export Options** –  
  - PDF reports for printing/sharing  
  - CSV for spreadsheet use  
- **MySQL Database** – Secure storage for financial data

---

## 🖥️ Technologies Used

| Tech          | Description                                |
|---------------|--------------------------------------------|
| 🐍 Python     | Core programming language                  |
| 🪟 Tkinter    | GUI framework                              |
| 📊 Matplotlib | Graph plotting (pie & line charts)         |
| 🧾 FPDF       | PDF generation                             |
| 📁 CSV        | CSV export functionality                   |
| 🗄️ MySQL      | Database for secure expense data storage   |

---

## 📂 Project Structure

```bash
FAMS FINAL PROJECT CS XII/
│
├── fams.py              # Main application entry point
├── login.py             # Handles user login
├── mic.py               # Additional utility (mic-based input feature)
├── PDF.py               # PDF export functionality
├── csvproducer.py       # CSV export functionality
├── database_details.py  # MySQL connection details & queries
│
├── dash.png             # Dashboard UI image (asset)
├── pattern.png          # UI background pattern (asset)
├── popup.mp4            # Demo / animation video
│
├── __pycache__/         # Compiled Python bytecode
