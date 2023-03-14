# mplfinance
This script creates a simple graphical user interface (GUI) for plotting candlestick charts using the tkinter library. The user can select a CSV data file from the "data" directory within the working directory, and the script will plot the last 100 rows of the dataset using the mplfinance library.
This script creates a simple graphical user interface (GUI) for plotting candlestick charts using the tkinter library. The user can select a CSV data file from the "data" directory within the working directory, and the script will plot the last 100 rows of the dataset using the mplfinance library.

The main steps of the script are:

Create the ChartingGUI class, which initializes the tkinter window and widgets.
Define the load_files method, which loads the available CSV files from the "data" directory and populates the dropdown menu.
Define the plot method, which reads the selected CSV file, processes the data, and plots the last 100 rows using mplfinance.
Instantiate the ChartingGUI class and run the tkinter main event loop.
When run, the script will display a GUI window with a dropdown menu to select a CSV file and a "Plot" button. Users can choose a file from the dropdown menu and click "Plot" to display a candlestick chart of the last 100 rows of the dataset. If there is an error during plotting, a message will be printed to the console.
