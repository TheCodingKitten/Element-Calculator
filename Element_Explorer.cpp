// Element Explorer
// https://github.com/TheCodingKitten/Element-Explorer
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <limits>

using namespace std;

// Define a structure to hold element data
struct Element
{
	int atomicNumber;
	string name;
	string symbol;
};

// Function to get user input with validation
int getValidUserInput()
{
	int userInput;
	while (true)
	{
		cout << "Enter the atomic number of the element to display: ";
		cin >> userInput;

		// Check for invalid input (non-numeric or out of range)
		if (cin.fail() || userInput <= 0 || userInput > 118)
		{
			cin.clear();										 // Clear the error flag
			cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
			cout << "Invalid input. Please enter a valid atomic number between 1 and 118." << endl;
		}
		else
		{
			return userInput; // Return valid input
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
	return elements;
}

// Function to print element details
void printElementDetails(const Element &e)
{
	cout << "Element details:" << endl;
	cout << "Atomic Number: " << e.atomicNumber << endl;
	cout << "Name: " << e.name << endl;
	cout << "Symbol: " << e.symbol << endl;
}

// CLI Interface
void runCLI(const vector<Element> &elements)
{
	// Get valid user input for atomic number
	int userInput = getValidUserInput();

	// Check if the input corresponds to an element (userInput is atomic number)
	bool elementFound = false;
	for (const auto &e : elements)
	{
		if (e.atomicNumber == userInput)
		{
			printElementDetails(e);
			elementFound = true;
			break;
		}
	}

	if (!elementFound)
	{
		cerr << "Error: Atomic number " << userInput << " not found in the dataset." << endl;
	}
}

// GUI Interface (Placeholder for now)
void runGUI(const vector<Element> &elements)
{
	// In the future, you can integrate a GUI framework here
	// For now, we'll just output a placeholder message
	cout << "GUI mode is not implemented yet." << endl;

	// Example: Display first few elements (you can later integrate actual GUI code)
	for (const auto &e : elements)
	{
		// cout << e.atomicNumber << ": " << e.name << " (" << e.symbol << ")" << endl;
		string null = e.name;
	}
}

int main(int argc, char *argv[])
{
	string mode = "cli";			  // Default mode is CLI
	string datafile = "Elements.csv"; // Default file name

	// Check for --help flag and display help message
	for (int i = 1; i < argc; ++i)
	{
		string arg = argv[i];
		if (arg == "--help" || arg == "-h")
		{
			cout << "Usage: Element_Explorer [options] [datafile]\n\n"
				 << "Options:\n"
				 << "  --cli           Run the program in Command-Line Interface mode (default mode).\n"
				 << "  --gui           Run the program in Graphical User Interface mode (not implemented yet).\n"
				 << "  --help          Display this help message.\n\n"
				 << "Arguments:\n"
				 << "  [datafile]      Path to the CSV file containing element data. Default is 'Elements.csv'.\n";
			return 0; // Exit after displaying help
		}
	}

	// Process command-line arguments
	for (int i = 1; i < argc; ++i)
	{
		string arg = argv[i];
		if (arg == "--cli" || arg == "-c")
		{
			mode = "cli"; // Set mode to CLI (although it's the default)
		}
		else if (arg == "--gui" || arg == "-g")
		{
			mode = "gui"; // Set mode to GUI
		}
		else
		{
			datafile = arg; // Assume it's the datafile
		}
	}

	// Import data from the CSV file
	vector<Element> elements = importData(datafile);
	if (elements.empty())
	{
		cerr << "Error: No data loaded from the file." << endl;
		return 1;
	}

	// Run the appropriate mode (CLI or GUI)
	if (mode == "cli")
	{
		runCLI(elements); // Run the CLI version
	}
	else if (mode == "gui")
	{
		runGUI(elements); // Run the GUI version
	}
	else
	{
		cerr << "Invalid mode specified. Use --cli or --gui." << endl;
		return 1;
	}

	return 0;
}
