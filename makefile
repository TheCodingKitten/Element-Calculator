# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -std=c++17 -Wall -Wextra

# Source files
SRCS = Element_Explorer.cpp

# Output executables
EXE_WIN = Element_Explorer.exe
EXE_LINUX = Element_Explorer

# Targets
all: linux windows

linux: $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(EXE_LINUX)

windows: $(SRCS)
	$(CXX) $(CXXFLAGS) $(SRCS) -static-libgcc -static-libstdc++ -o $(EXE_WIN)

clean:
	rm  .\$(EXE_LINUX) .\$(EXE_WIN)
