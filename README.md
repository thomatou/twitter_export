# B-I-N-G-O

A Bingo card contain 25 squares arranged in a 5x5 grid (five columns and five
rows). Each space in the grid contains a number between 1 and 75. The center
space is marked "FREE" and is automatically filled.

As the game is played, numbers are drawn. If the player's card has that number,
that space on the grid is filled.

A player wins BINGO by completing a row, column, or diagonal of filled spaces.

Your job is to complete the function that takes a bingo card and array of drawn
numbers and return 'true' if that card has achieved a win.

A bingo card will be 25 element array. With the string 'FREE' as the center
element (index 12). Although developers are unscrupulous, they will pass valid
data to your function.

# Solution by Thomas

The main function is defined in `index.js`. `tests.js` imports this function and tests it on 7 cases, using the constraints of the problem definition (i.e. assuming valid data will be passed to the function). Running `node tests.js` should return true, true, true, true, false, true, false.

* Assumption 1: `bingoCard` is a 1-D array containing numbers.
* Assumption 2: `drawnNumbers` is a 1-D array containing numbers, with no limit on length of the array.

# Logic

To keep track of the tally of drawn numbers in each row, column, and diagonal, we first define a dictionary `solution` with keys "columns", "rows", and "diagonals", whose values are arrays of integers of length 5, 5, and 2, respectively. The tally of drawn numbers in column `i` is maintained in the `i`-th element of `solution.columns`.

The idea is to iterate through the `bingoCard` and, for each number on it, check if it belongs to `drawnNumbers`. Since we're not given an upper bound for the length of `drawnNumbers`, we first convert it to a `Set()` to ensure constant look-up time on every iteration of the for loop.

If this condition is met, then we increment our counters for this row and column, and diagonal if applicable.

On every iteration, we check if any of our current tallies are greater than 4, in which case we return true (bingo!). 

The function will return false if, after iterating through all the numbers on the bingoCard, all tallies are smaller than 5.

# Big-O analysis

Time complexity: O(1). The for loop is always limited to the 25 numbers on the `bingoCard`, and the look up in `drawnNumbers` is also constant since we use a set.

Space complexity: O(k), where k is the length of `drawnNumbers`, since we create a set with the elements from drawnNumbers. The dictionary we create is of fixed size, since it is based on the fixed size of the `bingoCard`, so doesn't contribute here.

Could be turned into a O(k) time, O(1) space complexity solution by performing look up on the original array `drawnNumbers` instead of creating a set.
