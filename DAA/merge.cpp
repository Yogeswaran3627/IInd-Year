//Question 1: Merge Sort Algorithm
Code:

#include <iostream>
using namespace std;

void merge(int A[], int l, int m, int r) {
    int p = m - l + 1;
    int q = r - m;

    int* B = new int[p];
    int* C = new int[q];

    for (int i = 0; i < p; i++)
        B[i] = A[l + i];

    for (int j = 0; j < q; j++)
        C[j] = A[m + 1 + j];

    int i = 0, j = 0, k = l;

    while (i < p && j < q) {
        if (B[i] <= C[j]) {
            A[k] = B[i];
            i++;
        } else {
            A[k] = C[j];
            j++;
        }
        k++;
    }

    while (i < p) {
        A[k] = B[i];
        i++;
        k++;
    }

    while (j < q) {
        A[k] = C[j];
        j++;
        k++;
    }

    delete[] B;
    delete[] C;
}

void mergeSort(int A[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergeSort(A, l, m);
        mergeSort(A, m + 1, r);

        merge(A, l, m, r);
    }
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    int* A = new int[n];

    cout << "Enter elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    mergeSort(A, 0, n - 1);

    cout << "Sorted array:\n";
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    cout << endl;

    delete[] A;
    return 0;
}

//Sample Output:
Enter number of elements: 6
Enter elements:
12 11 13 5 6 7
Sorted array:
5 6 7 11 12 13
