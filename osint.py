import tkinter as tk
from tkinter import scrolledtext
from googlesearch import search
import webbrowser

def perform_search():
    query = entry.get()
    results_text.delete(1.0, tk.END) 
    results_text.insert(tk.END, f"Searching for: {query}\n\n")
    
    try:
        num_results = int(count_entry.get())  
        links = search(query, num_results=num_results)
        for link in links:
            insert_link(link)
    except ValueError:
        results_text.insert(tk.END, "Please enter a valid number for the number of results.\n")
    except Exception as e:
        results_text.insert(tk.END, f"Error occurred: {e}")

def insert_link(link):
    display_text = f"[+] Result: {link}\n"
    results_text.insert(tk.END, display_text)
    start_index = results_text.index(tk.END + f"- {len(display_text)}c")
    end_index = results_text.index(tk.END + "- 1c")
    results_text.tag_add(link, start_index, end_index)
    results_text.tag_bind(link, "<Button-1>", lambda e, link=link: open_link(link))
    results_text.tag_config(link, foreground="blue", underline=True)

def open_link(link):
    webbrowser.open(link)

root = tk.Tk()
root.title("Raulisr00t OSINT-Tool")

bold_font = ("Helvetica", 10, "bold")

entry_label = tk.Label(root, text="Enter your search query:", font=bold_font)
entry_label.pack(pady=15, padx=30)

entry = tk.Entry(root, width=80)
entry.pack(pady=5)

count_label = tk.Label(root, text="How many results do you want to see:", font=bold_font)
count_label.pack(pady=15, padx=30)

count_entry = tk.Entry(root, width=10)
count_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=perform_search)
search_button.pack(pady=15, padx=10)

results_text = scrolledtext.ScrolledText(root, width=100, height=20, bg="lightblue") 
results_text.pack(pady=10)

root.mainloop()
