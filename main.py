import seaborn as sns
import datetime
import matplotlib.pyplot as plt
import os
import csv

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    if not os.path.exists('expenses.csv'):
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount'])
            writer.writerow([date, category, amount])
    else:
        with open('expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])
            
def show_total_expense():
    if not os.path.exists('expenses.csv'):
        print("No expenses found.")
        return
    total = 0
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            total += float(row[2])
    print(f"Total expenses: {total}")

def category_summary():
    if not os.path.exists('expenses.csv'):
        print("No expenses found.")
        return
    summary = {}
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[1]
            amount = float(row[2])
            if category.lower() in summary:
                summary[category.lower()] += amount
            else:
                summary[category.lower()] = amount
    print("Category-wise Summary:")
    for category, total in summary.items():
        print(f"{category}: {total}")
        
def plot_expense_trend():
    if not os.path.exists('expenses.csv'):
        print("No expenses found.")
        return
    dates = []
    amounts = []
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            dates.append(row[0])
            amounts.append(float(row[2]))
    
    sns.set_theme(style="darkgrid")
    plt.hist(dates, weights=amounts, bins=len(set(dates)), alpha=0.7, color='pink')
    plt.title('Spending Trend')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
def delete_data():
    if os.path.exists("expenses.csv"):
        os.remove("expenses.csv")
        print("All expense data deleted.")
    else:
        print("No expense data found.")

def main():
    while True:
        print("\n=========== Budget Tracker ===========")
        print("1. Add Expense")
        print("2. Show Total Expense")
        print("3. Show Category-wise Summary")
        print("4. Show Spending Trend (Graph)")
        print("5. Delete data")
        print("6. Exit")
        print("======================================")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_total_expense()    
        elif choice == '3':
            category_summary()
        elif choice == '4':
            plot_expense_trend()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
