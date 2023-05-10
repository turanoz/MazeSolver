

# Maze Solver

This is a Python script that solves mazes using the command prompt. The input maze is provided as a text file, and the output is also saved to a text file.

## Usage

To use the script, navigate to the directory containing the `yolbul.py` file using the command prompt. Then, run the following command:

```
py yolbul.py input_file_path output_file_path
```

where `input_file_path` is the path to the input maze file, and `output_file_path` is the desired path to the output file.

For example, if you want to solve the maze in the file `girdi.txt` and save the solution to `cikti.txt`, you would run the following command:

```
py yolbul.py girdi.txt cikti.txt
```

## Input format

The input maze should be provided as a text file. The maze should be rectangular, with each cell represented by a single character. The following characters are used to represent different types of cells:

- `.`: an empty cell
- `#`: a wall
- `S`: the start cell
- `E`: the end cell

For example, the following is a valid input maze:

```
##########
#S.......#
#.####...#
#.#..#...#
#.#..#...#
#.#..#...#
#.#..#...#
#.....#..#
########E#
```

## Output format

The output of the script is a text file that shows the solution path through the maze. The solution path is represented by the `*` character. For example, the solution to the above maze would be:

```
##########
#S*******#
#*####***#
#.#..#***#
#.#..#***#
#.#..#***#
#.#..#***#
#*****#..#
########E#
```

If no solution can be found, the output file will be empty.

## Additional notes

- The script uses a depth-first search algorithm to solve the maze.
- The script assumes that the maze has exactly one start cell (`S`) and one end cell (`E`).
- The script does not check the validity of the input maze (e.g., whether it is rectangular, whether it has a valid start and end cell, etc.). It is the responsibility of the user to ensure that the input maze is valid.
