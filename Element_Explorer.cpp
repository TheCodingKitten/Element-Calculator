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

int main(int argc, char *argv[])
{
	// Set default filename, but allow overriding from command-line argument
	string datafile = (argc > 1) ? argv[1] : "Elements.csv";

	// Import data from the CSV file
	vector<Element> elements = importData(datafile);
	if (elements.empty())
	{
		cerr << "Error: No data loaded from the file." << endl;
		return 1;
	}

	// Get valid user input for atomic number
	int userInput = getValidUserInput();

	// Check if the input corresponds to an element (userInput is atomic number)
	// Since atomic numbers start from 1, use that directly to access the element
	bool found = false;
	for (const auto &e : elements)
	{
		if (e.atomicNumber == userInput)
		{
			printElementDetails(e);
			found = true;
			break;
		}
	}

	if (!found)
	{
		cerr << "Error: Atomic number " << userInput << " not found in the dataset." << endl;
	}

	return 0;
}
