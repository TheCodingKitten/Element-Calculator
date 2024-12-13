# Element Explorer
# https://github.com/TheCodingKitten/Element-Explorer
# 
# Reference: https://www.pythonguis.com/tutorials/create-gui-tkinter/
# 

# Import CLI script
import Element_Explorer_CLI as EC

import tkinter as tk
from tkinter import TclError, ttk

def create_table_frame(container):
    frame = ttk.Frame(container)

# Define a dictionary for the element placements on the grid
# Each tuple in the dictionary represents (row, column) for the element
element_positions = {
    "H": (0, 0), "He": (0, 17),
    "Li": (1, 0), "Be": (1, 1), "B": (1, 12), "C": (1, 13), "N": (1, 14), "O": (1, 15), "F": (1, 16), "Ne": (1, 17),
    "Na": (2, 0), "Mg": (2, 1), "Al": (2, 12), "Si": (2, 13), "P": (2, 14), "S": (2, 15), "Cl": (2, 16), "Ar": (2, 17),
    "K": (3, 0), "Ca": (3, 1), "Sc": (3, 2), "Ti": (3, 3), "V": (3, 4), "Cr": (3, 5), "Mn": (3, 6), "Fe": (3, 7), 
    "Co": (3, 8), "Ni": (3, 9), "Cu": (3, 10), "Zn": (3, 11), "Ga": (3, 12), "Ge": (3, 13), "As": (3, 14), 
    "Se": (3, 15), "Br": (3, 16), "Kr": (3, 17),
    "Rb": (4, 0), "Sr": (4, 1), "Y": (4, 2), "Zr": (4, 3), "Nb": (4, 4), "Mo": (4, 5), "Tc": (4, 6), "Ru": (4, 7), 
    "Rh": (4, 8), "Pd": (4, 9), "Ag": (4, 10), "Cd": (4, 11), "In": (4, 12), "Sn": (4, 13), "Sb": (4, 14), 
    "Te": (4, 15), "I": (4, 16), "Xe": (4, 17),
    "Cs": (5, 0), "Ba": (5, 1), "La": (5, 2), "Hf": (5, 3), "Ta": (5, 4), "W": (5, 5), "Re": (5, 6), "Os": (5, 7), 
    "Ir": (5, 8), "Pt": (5, 9), "Au": (5, 10), "Hg": (5, 11), "Tl": (5, 12), "Pb": (5, 13), "Bi": (5, 14), 
    "Po": (5, 15), "At": (5, 16), "Rn": (5, 17),
    "Fr": (6, 0), "Ra": (6, 1), "Ac": (6, 2), "Rf": (6, 3), "Db": (6, 4), "Sg": (6, 5), "Bh": (6, 6), "Hs": (6, 7), 
    "Mt": (6, 8), "Ds": (6, 9), "Rg": (6, 10), "Cn": (6, 11), "Nh": (6, 12), "Fl": (6, 13), "Mc": (6, 14), 
    "Lv": (6, 15), "Ts": (6, 16), "Og": (6, 17),

    # Lanthanides (Row 8 starting from column 2)
    "Ce": (8, 2), "Pr": (8, 3), "Nd": (8, 4), "Pm": (8, 5), "Sm": (8, 6), "Eu": (8, 7), "Gd": (8, 8), 
    "Tb": (8, 9), "Dy": (8, 10), "Ho": (8, 11), "Er": (8, 12), "Tm": (8, 13), "Yb": (8, 14), "Lu": (8, 15),

    # Actinides (Row 9 starting from column 2)
    "Th": (9, 2), "Pa": (9, 3), "U": (9, 4), "Np": (9, 5), "Pu": (9, 6), "Am": (9, 7), "Cm": (9, 8), 
    "Bk": (9, 9), "Cf": (9, 10), "Es": (9, 11), "Fm": (9, 12), "Md": (9, 13), "No": (9, 14), "Lr": (9, 15)
}

def show_element_info(element):
    # Display the information of the element
    info_text.delete("1.0", tk.END)  # Clear previous text
    element_info = EC.element_info("Symbol", element)
    info_text.insert(tk.END, EC.return_element_info(element_info[2]))

def create_table_frame(parent):
    table_frame = tk.Frame(parent)
    
    # Configure the grid to make each row and column expandable
    for i in range(7):  # Number of rows in periodic table layout
        table_frame.grid_rowconfigure(i, weight=1)
    for j in range(18):  # Number of columns in periodic table layout
        table_frame.grid_columnconfigure(j, weight=1)
    
    # Create buttons for each element, which call show_element_info with the element symbol when clicked
    for element, (row, col) in element_positions.items():
        button = tk.Button(table_frame, text=element, font=("Arial", 8),
                           command=lambda el=element: show_element_info(el))
        button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)  # sticky="nsew" makes button fill cell
    
    return table_frame

def create_main_window():
    global info_text  # To access info_text in the show_element_info function

    root = tk.Tk()
    root.title("Periodic Table Tool")
    root.geometry("600x500")  # Set an initial size suitable for smaller screens
    root.resizable(True, True)

    # Main container frame for layout management
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)
    
    # Configure the main frame's grid to manage layout proportions
    main_frame.grid_rowconfigure(0, weight=5, minsize=300)  # Prioritise space for the table
    main_frame.grid_rowconfigure(1, weight=1)  # Reduce the weighting for the information panel
    main_frame.grid_columnconfigure(0, weight=1)  # Single column layout

    # Periodic Table Frame at the top with responsive element buttons
    table_frame = create_table_frame(main_frame)
    table_frame.grid(row=0, column=0, sticky="nsew")

    # Information Panel Frame below the table with fixed height constraints
    info_frame = tk.Frame(main_frame, bg="lightgrey", height=100)  # Set fixed height
    info_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    # Label for element information with smaller font
    info_label = tk.Label(info_frame, text="Element Info", bg="lightgrey", font=("Arial", 10))
    info_label.pack(anchor="n", pady=5)

    # Smaller Text widget for displaying element details
    info_text = tk.Text(info_frame, wrap="word", font=("Arial", 8), height=5)
    info_text.pack(expand=True, fill="both", padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()

