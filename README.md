# 💸 Budget Tracker (Python CLI)

A simple, command-line based Budget Tracker built in Python that allows users to:

- Add daily expenses with category and date
- View total and category-wise expenses
- Visualize spending trends using graphs
- Delete all saved data

---

## 📦 Features

✅ Add new expenses  
✅ View total expense  
✅ View category-wise summary  
✅ Visualize spending trend using `seaborn` and `matplotlib`  
✅ Option to delete all stored data  
✅ CSV file-based persistent storage

---

## 🛠️ Tech Stack

- **Python 3**
- `csv` for file handling  
- `datetime` for date tracking  
- `matplotlib` & `seaborn` for data visualization  
- `os` for file management

---

## 📂 File Structure

budget_tracker.py # Main Python script
expenses.csv # Automatically created to store expense data

---

## ▶️ How to Run
1. **Clone the repository:**
git clone https://github.com/your-username/budget-tracker.git
cd budget-tracker
Install required libraries:

pip install matplotlib seaborn

Run the app:
python budget_tracker.py

📊 Sample Output

=========== Budget Tracker ===========
1. Add Expense
2. Show Total Expense
3. Show Category-wise Summary
4. Show Spending Trend (Graph)
5. Delete data
6. Exit
======================================
Enter your choice (1-6):
📉 Graph Example
The spending trend will be shown as a date-wise histogram of your expenses.

⚠️ Data Handling
All data is stored in expenses.csv.

Selecting "Delete Data" will permanently remove this file.
## 👩‍💻 Author

**Waniya Farooq**  

 LinkedIn: https://www.linkedin.com/in/waniya-farooq-b4086630b/

 GitHub: https://github.com/WaniyaFarooq 
