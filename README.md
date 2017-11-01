# Project 5: Map displaying volleyball court locations in Eugene #
### Author: Shohei Etzel, sse@uoregon.edu ###

### Summary ###
A flask server implemented with Leaflet and MapQuest API plugins that displays a series of map markers derived from a text file parsed and received in JSON format.

### Features ###
The map will initially show up for the Eugene area.
Map markers mark volleyball court location around Eugene
A marker with an address will show for any map location that the user clicks on.

### Running ###
Go to folder you want to download on the command line.

Type 'git clone https://github.com/shoheietzel/proj5-maps' to download

To start the server, go to the main repository and type commands 'make install' (for first time users) and then 'make start' into the terminal. To stop the server, type 'make stop'

### Data format ###
The .txt is formatted as such

{name of location}; {lattitude}; {longitude}; {address}; {sports}

The lines are parsed line by line, and split by the semicolons.
There must be five entries in each line.
