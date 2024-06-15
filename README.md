# Raulisr00t OSINT-Tool

Raulisr00t OSINT-Tool is a simple Python-based GUI application that allows users to perform Google searches and display the results in a scrollable text widget. It uses the `googlesearch-python` library to fetch search results and `tkinter` for the graphical user interface.

## Features

- User-friendly GUI to enter search queries.
- Option to specify the number of search results to retrieve.
- Displays search results as clickable links.
- Opens the selected search result in the default web browser.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `googlesearch-python` (install using pip)

## Installation

1. Clone the repository or download the source code.

```bash
git clone https://github.com/your-username/raul-isr00t-osint-tool.git
Navigate to the project directory.
cd raulisr00t-osint-tool

Install the required Python packages.
pip install googlesearch-python
```
##Usage

Run the application.
python osint_tool.py

Enter your search query in the input field.
Specify the number of search results you want to retrieve.
Click the "Search" button to perform the search.
Click on any of the displayed results to open the link in your default web browser.
Code Overview
The main components of the application are:

perform_search: Fetches search results based on the user's query and number of results specified.
insert_link: Inserts a clickable link into the results text widget.
open_link: Opens the selected link in the default web browser.
Example
Here's an example of how the application looks:


##Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or create a pull request.

##License
This project is licensed under the MIT License. See the LICENSE file for details.
