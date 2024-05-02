#include <iostream>
#include <cstring>

using namespace std;

#define MAX_N 8  // Maximum allowed board size (N should be <= MAX_N)

int board[MAX_N][MAX_N];

// Function to print the board configuration
void printSolution(int board[MAX_N][MAX_N], int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to check if queen can be placed on board[row][col]
bool isPossible(int row, int col, int slashDiagonal[MAX_N][MAX_N], int backSlashDiagonal[MAX_N][MAX_N], bool rowLook[MAX_N], bool slashDiagonalLook[], bool backSlashDiagonalLook[], int N) {
    if (slashDiagonalLook[slashDiagonal[row][col]] ||
        backSlashDiagonalLook[backSlashDiagonal[row][col]] ||
        rowLook[row]) {
        return false;
    }
    return true;
}

// Recursive utility function to solve N Queen problem
bool solveNQueensUtil(int board[MAX_N][MAX_N], int col, int slashDiagonal[MAX_N][MAX_N], int backSlashDiagonal[MAX_N][MAX_N], bool rowLook[MAX_N], bool slashDiagonalLook[], bool backSlashDiagonalLook[], int N) {
    // Base case: If all queens are placed
    if (col >= N) {
        return true;
    }

    // Try placing a queen in each row in the current column
    for (int i = 0; i < N; i++) {
        if (isPossible(i, col, slashDiagonal, backSlashDiagonal, rowLook, slashDiagonalLook, backSlashDiagonalLook, N)) {
            // Place a queen on the board
            board[i][col] = 1;
            rowLook[i] = true;
            slashDiagonalLook[slashDiagonal[i][col]] = true;
            backSlashDiagonalLook[backSlashDiagonal[i][col]] = true;

            // Recursively solve the rest of the problem
            if (solveNQueensUtil(board, col + 1, slashDiagonal, backSlashDiagonal, rowLook, slashDiagonalLook, backSlashDiagonalLook, N)) {
                return true;
            }

            // Backtrack if needed
            board[i][col] = 0;
            rowLook[i] = false;
            slashDiagonalLook[slashDiagonal[i][col]] = false;
            backSlashDiagonalLook[backSlashDiagonal[i][col]] = false;
        }
    }

    // If the queen cannot be placed in any row in this column, return false
    return false;
}

// Function to solve the N Queens problem using Branch and Bound
bool solveNQueens(int N) {
    // Validate N value
    if (N < 1 || N > MAX_N) {
        cout << "Invalid board size! N should be between 1 and " << MAX_N << endl;
        return false;
    }

    // Initialize the board and helper arrays
    memset(board, 0, sizeof(board));
    int slashDiagonal[MAX_N][MAX_N], backSlashDiagonal[MAX_N][MAX_N];
    bool rowLook[MAX_N] = {false};
    bool slashDiagonalLook[2 * MAX_N - 1] = {false};
    bool backSlashDiagonalLook[2 * MAX_N - 1] = {false};

    // Initialize the slash and backslash diagonals
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            slashDiagonal[r][c] = r + c;
            backSlashDiagonal[r][c] = r - c + (N - 1);
        }
    }

    // Start solving from the first column
    if (!solveNQueensUtil(board, 0, slashDiagonal, backSlashDiagonal, rowLook, slashDiagonalLook, backSlashDiagonalLook, N)) {
        cout << "No solution found for N = " << N << endl;
        return false;
    }

    // Print the solution
    cout << "N-Queens solution for N = " << N << ":\n";
    printSolution(board, N);
    return true;
}

// Main function
int main() {
    int N;

    cout << "Enter the size of the chessboard (N): ";
    cin >> N;

    // Validate the size of the chessboard
    if (N < 1 || N > MAX_N) {
        cout << "Invalid size! Please enter a size between 1 and " << MAX_N << endl;
        return 1;
    }

    // Solve the N-Queens problem
    solveNQueens(N);

    return 0;
}
