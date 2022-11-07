
# 8 Queens

The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so
that no two queens attack each other. Thus, a solution requires that no two queens share the
same row, column, or diagonal. This solution was created using a genetic algorithm that is capable of finding all possible solutions.


## Explaination 

The chromosome structure consists of an array of integers, with each integer representing the
queen's column represented by the index of the integer in the array. The fitness function calculates the
fitness value of the given chromosome. If the fitness value is 0, then no queens are attacking each
other in that chromosome. The crossover operator takes two chromosomes, splits them, and joins them
at a random point in the range of the chromosome. 

If the locations of the queens in the chromosome match, they are overwritten with a new queen value that does not exist in the chromosome. The
mutation operator chooses a random point in the chromosome to mutate and changes the integer at the
random point to a new random number. If the new number in the chromosome matches that of any
other value in the chromosome, it goes through the chromosome and checks if the value of the
chromosome at each index exists in the temporary array used[]. If it already exists, the program
regenerates a new random number until one is found that does not already exist in the used[] array.


Once all of the values in the chromosome have been cleared of duplicates, the chromosome is
returned. The outputted results consist of the first solution that was found and then the time taken to
compute all possible solutions. 

The user is then given the option to display all the solutions or to stop
the program. If choosing to display all solutions they will be displayed 10 at a time to ensure it does not
cause previous solutions to be hidden.

## Settings

There is three variables that must be set at the top of the program that determine how the program runs.

```
POP_SIZE = 100 # number of chromosomes in the population
NUM_QUEENS = 8 # number of queens in the board
MAX_SOL = 92 # max number of solutions to find (Must be accurate for NUM_QUEENS)
```

The default settings are for 8 queens with a total of 92 possible solutions. It works for any number of queens and solutions but the max solutions but be set matching the maximum number of solutions for the number of queens or the program will throw an error when finding all solutions.

Below is the settings required for 9 queens.
```
POP_SIZE = 100 # number of chromosomes in the population
NUM_QUEENS = 9 # number of queens in the board
MAX_SOL = 352 # max number of solutions to find (Must be accurate for NUM_QUEENS)
```
## Run Locally

Open the project folder in a terminal.

Run the command below to start the program.

```
python Solution.py
```

## Output
The program begins by printing the first solution that is found followed by finding all 92 solutions. 
If the User opts to display all 92 options, then 10 solutions are showed at a time each time the user presses 'enter' button until all 92 boards are displayed.
```
First solution: [5, 1, 6, 0, 2, 4, 7, 3]

. . . . . Q . . 
. Q . . . . . . 
. . . . . . Q .
Q . . . . . . .
. . Q . . . . .
. . . . Q . . .
. . . . . . . Q
. . . Q . . . .

Time to find first solution: 0.3816690444946289 seconds
```

