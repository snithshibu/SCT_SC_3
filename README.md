# SCT_SD_Task 3
<b>Problem Statement:</b> Create a program that solves sudoku puzzles automatically. The Program should take an input grid representing and unsolved Sudoku puzzle and use an algorithm to fill in the missing numbers.<br><br>
<b>Pre-requisites:</b> Should know how to play Sudoku<br><br>
<b>Coding Language Used:</b> Python<br><br>
<b>Logic that can be used:</b> Naive Approach, Backtracking<br><br>
<b>Cons of Naive Approach/Why Backtracking is better:</b> <p>The Naive Approach is basically picking an empty square, trying all combinations, finding the right combination, and then moving to the next empty square. Issue with this approach is computation takes a long time, as there are 81 squares and possible combinations is 9^81, which is a huge number. Another issue is it doesn't always assure an accurate answer.</p> <p>With backtracking, if there is any issue with the numbers we solved, we go back to the previous step and check for other solutions. This is a more recursive step until we get our right answer. Therefore, backtracking is a much better alternative.</p>
