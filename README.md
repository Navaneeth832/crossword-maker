#Crossword Puzzle Generator
This project generates a crossword puzzle using a list of words and clues. It supports both custom and automatic crossword generation.

Features:
Custom Crossword: Allows users to input words and clues manually to create a custom crossword puzzle.

Automatic Crossword: Automatically generates a crossword using a set of predefined questions and answers sourced from an Excel file.

Greedy Algorithm: Utilizes a greedy algorithm to place words on the grid in the most optimal way, considering available space and pre-filled cells.

Output: Displays the crossword puzzle and clues, and writes them to a text file for easy access.

How It Works:
Choose your option:

1: Generate a custom crossword.

2: Generate an automatic crossword using predefined questions and answers.

Custom Mode:

Users can enter their own words and clues manually.

The program ensures that words fit within the grid, ensuring no overlap with existing words unless it's valid.

Automatic Mode:

The program selects random questions and answers from the GK_Questions_and_Answers.xlsx file.

The crossword is generated based on these random selections.

Displaying the Puzzle:

The generated crossword is displayed with empty spaces represented as '.' and filled cells with words.

The answer grid is displayed with hints for each word, indicating the direction (up, down, left, right).

Text File Output:

The crossword grid and clues are written to crossword_output.txt.

Requirements:
Python 3.x

pandas (pip install pandas)

Installation:
Clone the repository or download the script.

Install the necessary dependencies:

bash
Copy
Edit
pip install pandas
Make sure to have an Excel file (GK_Questions_and_Answers.xlsx) with columns Question and Answer for automatic crossword generation.

Running the Application:
Run the script:

bash
Copy
Edit
python crossword_generator.py
Choose between custom or automatic crossword generation and follow the prompts.

Output Example:
The program will generate a crossword puzzle and display it in the terminal.

It will also save the crossword puzzle and clues to a text file named crossword_output.txt.
