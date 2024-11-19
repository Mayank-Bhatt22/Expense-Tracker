# Expense-Tracker
This Python script is a simple Expense Tracker designed to help users record and summarize their daily expenses. It demonstrates the use of essential programming concepts such as dictionaries, file handling, and user interaction.
Key Features:
Add Expense: Users can add expenses under specific categories (e.g., food, travel). The program automatically updates the total amount for each category.
View Expenses: Displays a summary of all recorded expenses by category, showing the total amount spent in each.
Save and Load Data: The program uses a JSON file (expenses.json) to save expense data. On startup, it automatically loads any existing data from the file, ensuring no data is lost between sessions.
Interactive Menu: Provides a user-friendly menu to navigate through different functionalities like adding or viewing expenses and exiting the program.
How It Works:
On startup, the program checks if an expenses.json file exists. If found, it loads the existing data; otherwise, it initializes with an empty dictionary.
Users can interact with the program through a simple menu system:
Option 1: Add a new expense.
Option 2: View all expenses categorized.
Option 3: Exit and save all expense data to the JSON file.
The data is stored as a dictionary, where each key is a category and the value is the total amount spent in that category.
Purpose of the Project:
This project is ideal for beginners learning Python. It introduces practical concepts like:

Dictionaries: For organizing and categorizing data.
File Handling: Using JSON to persist data.
Loops & Conditional Statements: For building an interactive menu system.
This project is a great foundation for enhancing Python skills and can be expanded with features like date tracking, monthly summaries, or visualizations using libraries like matplotlib.
