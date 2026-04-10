//Question 1: Quick Sort (Hoare Partition)
Code:

#include <iostream>
using namespace std;

int hoarePartition(int A[], int l, int r) {
    int p = A[l];
    int i = l - 1;
    int j = r + 1;

    while (true) {
        do {
            i++;
        } while (A[i] < p);

        do {
            j--;
        } while (A[j] > p);

        if (i >= j)
            return j;

        swap(A[i], A[j]);
    }
}

void quicksort(int A[], int l, int r) {
    if (l < r) {
        int s = hoarePartition(A, l, r);
        quicksort(A, l, s);
        quicksort(A, s + 1, r);
    }
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    int A[n];

    cout << "Enter " << n << " elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    quicksort(A, 0, n - 1);

    cout << "Sorted array:\n";
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}

//Sample Output:
Enter number of elements: 5
Enter 5 elements:
25 10 30 5 15
Sorted array:
5 10 15 25 30
