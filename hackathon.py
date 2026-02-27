<!DOCTYPE html>
<html lang="te">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sudoku Game</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Sudoku Game</h1>
    <div id="board"></div>

    <script src="script.js"></script>
</body>
</html>
/* Basic body styling */
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin-top: 30px;
    background-color: #f2f2f2;
}

/* Sudoku board styling */
#board {
    display: grid;
    grid-template-columns: repeat(9, 40px);
    grid-template-rows: repeat(9, 40px);
    gap: 2px;
    justify-content: center;
    margin: 20px auto;
}

/* Each cell input styling */
#board input {
    width: 38px;
    height: 38px;
    text-align: center;
    font-size: 18px;
    border: 1px solid #333;
    border-radius: 4px;
}

/* Optional: highlight 3x3 subgrid borders */
#board input:nth-child(3n) {
    border-right: 2px solid #000;
}
#board input:nth-child(n+19):nth-child(-n+27),
#board input:nth-child(n+46):nth-child(-n+54),
#board input:nth-child(n+73):nth-child(-n+81) {
    border-bottom: 2px solid #000;
}

/* Button styling if you add check/solve button */
button {
    margin-top: 15px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border-radius: 5px;
    border: none;
    background-color: #4CAF50;
    color: white;
}
button:hover {
    background-color: #45a049;
}
// Get the board div
const board = document.getElementById("board");

// Create 9x9 grid (81 cells)
for (let i = 0; i < 81; i++) {
    let cell = document.createElement("input");
    cell.type = "text";      // Input type
    cell.maxLength = "1";    // Only 1 digit
    cell.addEventListener("input", () => {
        // Only allow numbers 1-9
        if (!/^[1-9]$/.test(cell.value)) {
            cell.value = "";
        }
    });
    board.appendChild(cell);
}

// Optional: Add Check Button functionality
function checkSudoku() {
    const cells = board.querySelectorAll("input");
    let valid = true;

    // Very simple check: all filled cells must be 1-9 (already restricted)
    cells.forEach(cell => {
        if (cell.value !== "" && !/^[1-9]$/.test(cell.value)) {
            valid = false;
        }
    });

    if (valid) alert("All entries are valid digits!");
    else alert("Some entries are invalid!");
}

// Optional: Add Check button dynamically
const checkBtn = document.createElement("button");
checkBtn.innerText = "Check Sudoku";
checkBtn.onclick = checkSudoku;
document.body.appendChild(checkBtn);
// Correct answers array
const answers = [
  "5", "Jupiter", "30", "New Delhi", "3", "15",
  "6", "7", "5", "42", "33", "81",
  "11", "24", "9", "21", "15", "20",
  "5", "17", "25", "9", "19", "48",
  "9", "21", "16", "36", "6", "19"
];