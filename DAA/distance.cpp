//Question 1: Closest Pair of Points (Brute Force)
Code:

#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int n;
    cout << "Enter number of points: ";
    cin >> n;
    double x[n], y[n];
    cout << "Enter the points (x y):\n";
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }
    double min_dist = INFINITY;
    int index1 = 0;
    int index2 = 0;
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            double d = sqrt(pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2));
            if (d < min_dist) {
                min_dist = d;
                index1 = i;
                index2 = j;
            }
        }
    }
    cout << "\nClosest pair: (" << x[index1] << ", " << y[index1] << ") and ("
         << x[index2] << ", " << y[index2] << ")" << endl;
    cout << "Minimum distance = " << min_dist << endl;
    cout << "\n";
    return 0;
}

//Sample Output:
Enter number of points: 3
Enter the points (x y):
1 2
10 15
2 3
Closest pair: (1, 2) and (2, 3)
Minimum distance = 1.41421
