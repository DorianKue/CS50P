# Coin Toss Simulator
#### Description:

This is my final project for the course "CS50’s Introduction to Programming with Python".
It's a Python program or script, that simulates a series of coin tosses, based on user input and then analyzes the results to determine the odds, or rather probability of the various outcomes.
The program provides insight into the distribution of heads and tails, calculates the percentage of each outcome and estimates the odds of repeating the same outcome in future coin tosses
using a mathematical approach.

#### Features
###### User interaction:
The program prompts the user for an input of how many times they want to flip a coin.
###### Coin toss simulation:
It generates a random coin toss result based on the input of the user.
###### Result analysis:
Then the program analyzes the results to determine the count and the percentage of heads and tails.
###### Odds calculation:
the binomial coefficient formula is used to calculate the probability of that same outcome happening again.
###### Saving results:
Optionally, the user is asked if they want to save the simulation results to a CSV file for further use.


#### Usage
###### Running the program:
Simply execute project.py in a Python environment.
After which you enter the number of coin flips you want the program to perform when prompted. Make sure to enter a positive number.
Then the program will display the count and percentage of heads and tails as well as the probability of repeating that same outcome.
Optionally you can save the results to a CSV file when prompted, by entering 'yes' or 'y'.
If you don't want the results to be saved, simply enter 'no' or 'n' when prompted.


#### Requirements:
- Ensure that Python **3.x** is installed on your system.
- Modules: random, csv, sys, os, math


#### Example:
>$ python project.py
>
>How many times would you like to flip the coin? 50
>
>Heads: 17 times which is 34.00%
>
>Tails: 33 times which is 66.0%
>
>The odds of this outcome are 0.87%
>
>Would you like to save these results? y/n




#### Future implementations:
Ideally i want to add the functionality, that the user can compare current results with previous, or historical results and do even more calculations based on that. However i felt that this was too much for the scope of this final project.

I also want to turn it into a simple Discord Bot using discord.py, which i will have to learn.


##### Notes:
The script itself should contain clear enough docstrings and comments to explain everything that you need to know.
