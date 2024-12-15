// Element Explorer
// https://github.com/TheCodingKitten/Element-Explorer
//

#define CLI_MODE
#include "Element_Explorer.h"

using namespace std;

// Convert case function. upperFirst can be supplied as true, it is false by default
string convertCase(string input, bool upperFirst = false)
{
	// Convert the entire string to lowercase
	transform(input.begin(), input.end(), input.begin(), ::tolower);

	// Convert first letter to uppercase if upperFirst is true
	if (upperFirst)
	{
		// Capitalize the first character if the string is not empty
		if (!input.empty())
		{
			input[0] = toupper(input[0]);
		}
	}

	return input;
}

// Function to get user input with validation
tuple<string, variant<int, string>> getValidUserInput(int totalElements)
{
	// Get user selction for input: Atomic Number, Symbol or Name
	string userSelection;

	while (true)
	{
		cout << "Choose input type: [A]tomic Number, [N]ame, [S]ymbol: ";
		getline(cin, userSelection);

		userSelection = convertCase(userSelection, true);

		// Check for valid user selection
		if (validSelections.find(userSelection) != validSelections.end())
		{
			// For valid input selection, return user selection and a default empty value (string) or int
			if (userSelection == "A" || userSelection == "Atomic number" || userSelection == "Number")
			{
				int atomicNumber;
				cout << "Enter the atomic number of an element: ";
				cin >> atomicNumber;

				// Validate atomic number
				if (cin.fail() || atomicNumber <= 0 || atomicNumber > totalElements)
				{
					cin.clear();
					cin.ignore(numeric_limits<streamsize>::max(), '\n');
					cout << "Invalid atomic number. Please try again." << endl;
					continue;
				}

				return make_tuple(userSelection, atomicNumber); // Return atomic number
			}

			else if (userSelection == "N" || userSelection == "Name")
			{
				string elementInput;

				// Ask user for input
				cout << "Enter the name of an element: ";
				cin >> elementInput;

				elementInput = convertCase(elementInput, true);

				return make_tuple(userSelection, elementInput);
			}

			else if (userSelection == "S" || userSelection == "Symbol")
			{
				string elementInput;

				// Ask user for input
				cout << "Enter the symbol of an element: ";
				cin >> elementInput;

				elementInput = convertCase(elementInput, true);

				return make_tuple(userSelection, elementInput);
			}
		}
		else
		{
			// Clear invalid input and prompt again
			cin.clear(); // Clear any stream errors
			// cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
			cout << "Invalid input. Please enter a valid input." << endl;
			continue;
		}
	}
}

// Function to import data from the CSV file
vector<Element> importData(const string &filename)
{
	vector<Element> elements;
	ifstream file(filename);

	if (!file.is_open())
	{
		cerr << "Error: Could not open file " << filename << endl;
		return elements; // Return an empty vector if file cannot be opened
	}

	// Log start of file loading
	clog << "Loading elements from " << filename << endl;

	string line;
	while (getline(file, line))
	{
		stringstream ss(line);
		string atomicNumberStr, name, symbol;

		// Extract the atomic number, name, and symbol
		getline(ss, atomicNumberStr, ',');
		getline(ss, name, ',');
		getline(ss, symbol, ',');

		// Convert atomic number to integer
		int atomicNumber = stoi(atomicNumberStr);

		// Add the Element to the vector
		elements.push_back({atomicNumber, name, symbol});
	}

	file.close();
	int totalElements = elements.size();
	clog << "Loaded " << totalElements << " elements from " << filename << endl; // Print
	return elements;
}

// Function to print element details
void printElementDetails(const Element &currentElement)
{
	cout << endl
		 << "Element details:" << endl
		 << "Atomic Number: " << currentElement.atomicNumber << endl
		 << "Name: " << currentElement.name << endl
		 << "Symbol: " << currentElement.symbol << endl
		 << endl;
}

// Find element details
Element findElementInfo(const vector<Element> &elements, const string &userSelection, const variant<int, string> &userInput)
{
	// Iterate through the elements vector to find a match based on user selection
	for (const auto &currentElement : elements)
	{
		// Check if searching by atomic number
		if (userSelection == "A")
		{
			int atomicNumber = get<int>(userInput); // Get the atomic number from the variant
			if (currentElement.atomicNumber == atomicNumber)
			{
				return currentElement; // Return the element if atomic number matches
			}
		}
		// Check if searching by name
		else if (userSelection == "N")
		{
			string name = get<string>(userInput); // Get the name from the variant
			if (currentElement.name == name)
			{
				return currentElement; // Return the element if name matches
			}
		}
		// Check if searching by symbol
		else if (userSelection == "S")
		{
			string symbol = get<string>(userInput); // Get the symbol from the variant
			if (currentElement.symbol == symbol)
			{
				return currentElement; // Return the element if symbol matches
			}
		}
	}

	// If no match is found, return an invalid element (could be an element with default values)
	return {-1, "", ""}; // Return an "invalid" element with default values (invalid atomic number, empty name, and empty symbol)
}

// CLI Interface
void runCLI(const vector<Element> &elements)
{
	// Get valid user input for atomic number
	auto [userSelection, userInput] = getValidUserInput(elements.size());

	// Return element variable
	Element returnElement;

	if (userSelection == "A")
	{
		// If user selected atomic number, search by atomic number
		int atomicNumber = get<int>(userInput);
		returnElement = findElementInfo(elements, "A", atomicNumber);
	}
	else if (userSelection == "N")
	{
		// If user selected name, search by name
		string elementName = get<string>(userInput);
		returnElement = findElementInfo(elements, "N", elementName);
	}
	else if (userSelection == "S")
	{
		// If user selected symbol, search by symbol
		string elementSymbol = get<string>(userInput);
		returnElement = findElementInfo(elements, "S", elementSymbol);
	}

	// Check if the element was found
	if (returnElement.atomicNumber != -1) // Valid element found
	{
		printElementDetails(returnElement); // Print the element details
	}
	else
	{
		cout << "Element not found." << endl; // Element not found
	}
}

// GUI Interface (Placeholder for now)
void runGUI(const vector<Element> &elements)
{
	// In the future, you can integrate a GUI framework here
	cout << "GUI mode is not implemented yet." << endl;

	// Placeholder
	for (const auto &currentElement : elements)
	{
		// cout << e.atomicNumber << ": " << e.name << " (" << e.symbol << ")" << endl;
		string null = currentElement.name; // Placeholder
	}
}

// Function to process flags, including --cli and --gui
void processElementFlag(int &i, const string &arg, const vector<Element> &elements, int argc, char *argv[], string &mode)
{
	if (arg == "--cli" || arg == "-c")
	{
		mode = "cli";
	}
	else if (arg == "--gui" || arg == "-g")
	{
		mode = "gui";
	}
	else if (i + 1 < argc) // Check that there's a value after the flag
	{
		string userInput = argv[i + 1]; // Get the user input following the flag
		Element foundElement;

		if (arg == "--name" || arg == "-n")
		{
			foundElement = findElementInfo(elements, "N", userInput);
		}
		else if (arg == "--symbol" || arg == "-s")
		{
			foundElement = findElementInfo(elements, "S", userInput);
		}
		else if (arg == "--atomic-number" || arg == "-a")
		{
			try
			{
				int atomicNumber = stoi(userInput); // Convert string to integer
				foundElement = findElementInfo(elements, "A", atomicNumber);
			}
			catch (const std::invalid_argument &e)
			{
				cerr << "Error: Invalid atomic number value provided." << endl;
				return;
			}
			catch (const std::out_of_range &e)
			{
				cerr << "Error: Atomic number out of range." << endl;
				return;
			}
		}

		// Check if an element was found and print details
		if (foundElement.atomicNumber != -1)
		{
			printElementDetails(foundElement);
			mode = "none";
		}
	}
}

int main(int argc, char *argv[])
{
	string mode = "cli";			  // Create variable and set default mode
	string datafile = "Elements.csv"; // Create variable and set default file name

	// Import data from the CSV file
	vector<Element> elements = importData(datafile);
	if (elements.empty())
	{
		cerr << "Error: No data loaded from the file." << endl;
		return 1;
	}

	// Process command-line arguments (flags and values)
	for (int i = 1; i < argc; i++)
	{
		string arg = argv[i];

		// Process the element flag input and mode flags
		processElementFlag(i, arg, elements, argc, argv, mode);
	}

	// Run the appropriate mode (CLI or GUI)
	if (mode != "none")
	{
		if (mode == "cli")
		{
			clog << "Running CLI..." << endl;
			runCLI(elements); // Run the CLI version
		}
		else
		{
			clog << "Running GUI..." << endl;
			runGUI(elements); // Run the GUI version
		}
	}

	return 0;
}
