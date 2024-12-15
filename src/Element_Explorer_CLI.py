# !/usr/bin/env python

# Element Calculator

# Imports
from time import sleep

# Element tuples
Elements = ["NULL", "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson", "Ununennium"]
Symbols = ["NULL", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og", "Uue"]
# Element dictionaries
# Converts input name into atomic number
nameToNumber = {"Hydrogen" : 1, "Helium" : 2, "Lithium" : 3, "Beryllium" : 4, "Boron" : 5, "Carbon" : 6, "Nitrogen" : 7, "Oxygen" : 8, "Fluorine" : 9, "Neon" : 10, "Sodium" : 11, "Magnesium" : 12, "Aluminium" : 13, "Silicon" : 14, "Phosphorus" : 15, "Sulfur" : 16, "Chlorine" : 17, "Argon" : 18, "Potassium" : 19, "Calcium" : 20, "Scandium" : 21, "Titanium" : 22, "Vanadium" : 23, "Chromium" : 24, "Manganese" : 25, "Iron" : 26, "Cobalt" : 27, "Nickel" : 28, "Copper" : 29, "Zinc" : 30, "Gallium" : 31, "Germanium" : 32, "Arsenic" : 33, "Selenium" : 34, "Bromine" : 35, "Krypton" : 36, "Rubidium" : 37, "Strontium" : 38, "Yttrium" : 39, "Zirconium" : 40, "Niobium" : 41, "Molybdenum" : 42, "Technetium" : 43, "Ruthenium" : 44, "Rhodium" : 45, "Palladium" : 46, "Silver" : 47, "Cadmium" : 48, "Indium" : 49, "Tin" : 50, "Antimony" : 51, "Tellurium" : 52, "Iodine" : 53, "Xenon" : 54, "Caesium" : 55, "Barium" : 56, "Lanthanum" : 57, "Cerium" : 58, "Praseodymium" : 59, "Neodymium" : 60, "Promethium" : 61, "Samarium" : 62, "Europium" : 63, "Gadolinium" : 64, "Terbium" : 65, "Dysprosium" : 66, "Holmium" : 67, "Erbium" : 68, "Thulium" : 69, "Ytterbium" : 70, "Lutetium" : 71, "Hafnium" : 72, "Tantalum" : 73, "Tungsten" : 74, "Rhenium" : 75, "Osmium" : 76, "Iridium" : 77, "Platinum" : 78, "Gold" : 79, "Mercury" : 80, "Thallium" : 81, "Lead" : 82, "Bismuth" : 83, "Polonium" : 84, "Astatine" : 85, "Radon" : 86, "Francium" : 87, "Radium" : 88, "Actinium" : 89, "Thorium" : 90, "Protactinium" : 91, "Uranium" : 92, "Neptunium" : 93, "Plutonium" : 94, "Americium" : 95, "Curium" : 96, "Berkelium" : 97, "Californium" : 98, "Einsteinium" : 99, "Fermium" : 100, "Mendelevium" : 101, "Nobelium" : 102, "Lawrencium" : 103, "Rutherfordium" : 104, "Dubnium" : 105, "Seaborgium" : 106, "Bohrium" : 107, "Hassium" : 108, "Meitnerium" : 109, "Darmstadtium" : 110, "Roentgenium" : 111, "Copernicium" : 112, "Nihonium" : 113, "Flerovium" : 114, "Moscovium" : 115, "Livermorium" : 116, "Tennessine" : 117, "Oganesson" : 118, "Ununennium" : 119}
# Convert input symbol into atomic number
symbolToNumber = {"H" : 1, "He" : 2, "Li" : 3, "Be" : 4, "B" : 5, "C" : 6, "N" : 7, "O" : 8, "F" : 9, "Ne" : 10, "Na" : 11, "Mg" : 12, "Al" : 13, "Si" : 14, "P" : 15, "S" : 16, "Cl" : 17, "Ar" : 18, "K" : 19, "Ca" : 20, "Sc" : 21, "Ti" : 22, "V" : 23, "Cr" : 24, "Mn" : 25, "Fe" : 26, "Co" : 27, "Ni" : 28, "Cu" : 29, "Zn" : 30, "Ga" : 31, "Ge" : 32, "As" : 33, "Se" : 34, "Br" : 35, "Kr" : 36, "Rb" : 37, "Sr" : 38, "Y" : 39, "Zr" : 40, "Nb" : 41, "Mo" : 42, "Tc" : 43, "Ru" : 44, "Rh" : 45, "Pd" : 46, "Ag" : 47, "Cd" : 48, "In" : 49, "Sn" : 50, "Sb" : 51, "Te" : 52, "I" : 53, "Xe" : 54, "Cs" : 55, "Ba" : 56, "La" : 57, "Ce" : 58, "Pr" : 59, "Nd" : 60, "Pm" : 61, "Sm" : 62, "Eu" : 63, "Gd" : 64, "Tb" : 65, "Dy" : 66, "Ho" : 67, "Er" : 68, "Tm" : 69, "Yb" : 70, "Lu" : 71, "Hf" : 72, "Ta" : 73, "W" : 74, "Re" : 75, "Os" : 76, "Ir" : 77, "Pt" : 78, "Au" : 79, "Hg" : 80, "Tl" : 81, "Pb" : 82, "Bi" : 83, "Po" : 84, "At" : 85, "Rn" : 86, "Fr" : 87, "Ra" : 88, "Ac" : 89, "Th" : 90, "Pa" : 91, "U" : 92, "Np" : 93, "Pu" : 94, "Am" : 95, "Cm" : 96, "Bk" : 97, "Cf" : 98, "Es" : 99, "Fm" : 100, "Md" : 101, "No" : 102, "Lr" : 103, "Rf" : 104, "Db" : 105, "Sg" : 106, "Bh" : 107, "Hs" : 108, "Mt" : 109, "Ds" : 110, "Rg" : 111, "Cn" : 112, "Nh" : 113, "Fl" : 114, "Mc" : 115, "Lv" : 116, "Ts" : 117, "Og" : 118, "Uue" : 119}

atomicNumberRange = range(1, 120, 1)

def get_user_input():
	print("""
Inputs:
symbol - Atomic symbol (e.g. He)
name - Name of element (e.g. Helium)
number - Atomic number (e.g. 2)
""")

	# Choose element input type
	startQuestion = str(input("Choose input (symbol, name, number, exit): ")).lower()
	return(startQuestion)

def handle_user_input(userinput):
	if userinput == "name":
		nameInput = str(input("Enter name of an element: ")) # User input to nameInput variable
		try:
			atomicNumber = nameToNumber.get(nameInput) # Change input to corresponding Atomic Number
		except:
			print_error("Invalid Element")

	elif userinput == "symbol":
		symbolInput = str(input("Enter symbol of an element: ")) # User input to symbolInput variable
		try:
			atomicNumber = symbolToNumber.get(symbolInput) # Change input to corresponding Atomic Number
		except:
			print_error("Invalid Element")

	elif userinput == "number":
		try:
			atomicNumber = int(input("Enter Atomic Number of an element: ")) # User input to atomicNumber variable
		except TypeError:
			print_error("Invalid Input")
	if atomicNumber not in atomicNumberRange: # Checks if atomic number is valid and restarts script if not
		print(f"ERROR: Input of {atomicNumber} is not an Atomic Number")
	elif userinput == "exit":
		print("Exiting...")
		sleep(0.25)
		exit() 
	else:
		print_error("Invalid Input")

	# Variables
	atomicNumberChange = atomicNumber
	print_element_info(atomicNumber)
	print_electron_layout(atomicNumber)

def print_electron_layout(ElementNumber):
	num2 = ElementNumber - 2 # Remainder after shell 1
	num3 = num2 / 8 # Number of shells
	num4 = num2 % 8 # Remaining electrons in outer most shell
	if ElementNumber == 1 or ElementNumber == 2: # Full inner shell only
		print('\n' "Shell Configuration: ", ElementNumber)
	else: 
		if num4 == 0: # Full inner, full middle(s), full outer shells
			print('\n' "Shell Configuration: 2", int(num3)*"8 ")
		else: # Full inner, full middle(s), not full outer shells
			print('\n' "Shell Configuration: 2", int(num3)*"8 ", end=str(num4))

def element_info(InputType, ElementInput):
	# Print info about element
	if InputType == "Symbol":
		ElementInputNumber = symbolToNumber.get(ElementInput) # Change input to corresponding Atomic Number
		return(Elements[ElementInputNumber], Symbols[ElementInputNumber], ElementInputNumber)

	elif InputType == "Name":
		ElementInputNumber = symbolToNumber.get(ElementInput) # Change input to corresponding Atomic Number
		return(Elements[ElementInputNumber], Symbols[ElementInputNumber], ElementInputNumber)

	elif InputType == "Number": 
		return(Elements[ElementInput], Symbols[ElementInput], ElementInput)

	else:
		return None

def print_element_info(ElementNumber):
	# Print info about element
	print('\n' "Element Name: ", Elements[ElementNumber],
	'\n' "Element Symbol: ", Symbols[ElementNumber],
	'\n' "Atomic Number: ", str(ElementNumber),
	'\n' "Wikipedia link: https://en.wikipedia.org/wiki/{0}".format(Elements[ElementNumber]))

def return_element_info(ElementNumber):
	# Return info about element to print
	return("""Element Name: {0}
Element Symbol: {1}
Atomic Number: {2}
Wikipedia link: https://en.wikipedia.org/wiki/{3}"""
	.format(Elements[ElementNumber], Symbols[ElementNumber], str(ElementNumber), Elements[ElementNumber]))

def print_error(Error):
	print(f"ERROR: {Error}")
	quit()

if __name__ == "__main__":
	while True:
		handle_user_input(get_user_input())
