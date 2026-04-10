//Question 1: Floyd-Warshall Algorithm (All-Pairs Shortest Path)
Code:

#include <iostream>
using namespace std;

#define INF 99999
#define MAX 100

void floyd(int W[MAX][MAX], int n) {
    int D[MAX][MAX];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            D[i][j] = W[i][j];
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (D[i][k] != INF && D[k][j] != INF) {
                    if (D[i][k] + D[k][j] < D[i][j]) {
                        D[i][j] = D[i][k] + D[k][j];
                    }
                }
            }
        }
    }

    cout << "\nShortest distance matrix:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (D[i][j] == INF)
                cout << "INF  ";
            else
                cout << D[i][j] << "    ";
        }
        cout << endl;
    }
}

int main() {
    int n;
    int W[MAX][MAX];

    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter weight matrix:\n";
    cout << "(Use " << INF << " for no edge)\n";

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> W[i][j];
        }
    }

    floyd(W, n);

    return 0;
}

//Sample Output:
Enter number of vertices: 3
Enter weight matrix:
(Use 99999 for no edge)
0 5 99999
99999 0 3
99999 99999 0
Shortest distance matrix:
0 5 8
INF 0 3
INF INF 0
