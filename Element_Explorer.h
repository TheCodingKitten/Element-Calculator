#ifndef ELEMENT_EXPLORER_H
#define ELEMENT_EXPLORER_H

#include <vector>
#include <string>

// Define a structure to hold element data
struct Element
{
	int atomicNumber;
	std::string name;
	std::string symbol;
};

// Function to import data from a CSV file
std::vector<Element> importData(const std::string &filename);

#ifdef CLI_MODE
// Functions specific to CLI mode

// Function to get valid user input for atomic number (CLI only)
int getValidUserInput();

// Function to print the details of an element (CLI only)
void printElementDetails(const Element &e);

#endif // CLI_MODE

// Function for the GUI interface (placeholder)
void runGUI(const std::vector<Element> &elements);

// Function for the CLI interface (used in CLI version)
void runCLI(const std::vector<Element> &elements);

#endif // ELEMENT_EXPLORER_H
