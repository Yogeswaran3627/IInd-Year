code:

#include <iostream>
using namespace std;

// Lomuto Partition (using first element as pivot)
int lomutoPartition(int A[], int l, int r) {
    int p = A[l];   // pivot
    int s = l;

    for (int i = l + 1; i <= r; i++) {
        if (A[i] < p) {
            s++;
            swap(A[s], A[i]);
        }
    }

    swap(A[l], A[s]); // place pivot in correct position
    return s;
}

// Quickselect function
int quickselect(int A[], int l, int r, int k) {
    int s = lomutoPartition(A, l, r);

    if (s == l + k - 1)
        return A[s];

    else if (s > l + k - 1)
        return quickselect(A, l, s - 1, k);

    else
        return quickselect(A, s + 1, r, k - (s - l + 1));
}

int main() {
    int n, k;

    cout << "Enter number of elements: ";
    cin >> n;

    int A[n];

    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++)
        cin >> A[i];

    cout << "\n";
    cout << "Enter k (kth smallest element): ";
    cin >> k;

    int result = quickselect(A, 0, n - 1, k);

    cout << k << "th smallest element is: " << result;
    cout << "\n\n";
    return 0;
}


//sample case:
Enter number of elements: 5
Enter elements:
56
25
49
67
31

Enter k (kth smallest element): 4
4th smallest element is: 56
