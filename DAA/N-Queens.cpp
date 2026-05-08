code:

#include <iostream>
#include <cstdlib>
using namespace std;

int x[20];
int totalCount = 0;

bool Place(int k, int i) {
    for (int j = 1; j < k; j++) {
        if (x[j] == i || abs(x[j] - i) == abs(j - k))
            return false;
    }
    return true;
}

void NQueens(int k, int n) {
    for (int i = 1; i <= n; i++) {
        if (Place(k, i)) {
            x[k] = i;
            if (k == n) {
                totalCount++;
                cout << totalCount << ". ";
                for (int j = 1; j <= n; j++) {
                    cout << "(" << x[j] << "," << j << ")";
                    if (j < n) cout << ",";
                }
                cout << endl;
            } else {
                NQueens(k + 1, n);
            }
        }
    }
}

int main() {
    int n;
    cout << "Enter the number of queens: ";
    cin >> n;
    cout << "\n";
    NQueens(1, n);
    if (totalCount == 0) {
       cout << "No solution exists for " << n << " queens." << endl;
    } else {
       cout << "\nCan be placed in " << totalCount << " ways."<< endl;
    }
    cout << "\n";
    return 0;
}

//sample case:
Enter the number of queens: 5

1. (1,1),(3,2),(5,3),(2,4),(4,5)
2. (1,1),(4,2),(2,3),(5,4),(3,5)
3. (2,1),(4,2),(1,3),(3,4),(5,5)
4. (2,1),(5,2),(3,3),(1,4),(4,5)
5. (3,1),(1,2),(4,3),(2,4),(5,5)
6. (3,1),(5,2),(2,3),(4,4),(1,5)
7. (4,1),(1,2),(3,3),(5,4),(2,5)
8. (4,1),(2,2),(5,3),(3,4),(1,5)
9. (5,1),(2,2),(4,3),(1,4),(3,5)
10. (5,1),(3,2),(1,3),(4,4),(2,5)

Can be placed in 10 ways.
