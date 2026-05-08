//Question 1: Merge Sort Algorithm
Code:

#include <iostream>
using namespace std;

static void merge(int B[], int sizeB, int C[], int sizeC, int A[]) {
    int i = 0, j = 0, k = 0;
        
    while (i < sizeB && j < sizeC) {
        if (B[i] <= C[j])
            A[k++] = B[i++];
        else
            A[k++] = C[j++];
    }

    while (i < sizeB)
        A[k++] = B[i++];
            
    while (j < sizeC)
        A[k++] = C[j++];
}

static void mergeSort(int A[], int n) {
    if (n <= 1)
        return;

    int mid = n / 2;
    int sizeB = mid;
    int sizeC = n - mid;

    int* B = new int[sizeB];
    int* C = new int[sizeC];

    for (int i = 0; i < mid; i++)
        B[i] = A[i];
    for (int i = mid; i < n; i++)
        C[i - mid] = A[i];

    mergeSort(B, sizeB);
    mergeSort(C, sizeC);
    merge(B, sizeB, C, sizeC, A);

    // In C++, we must manually free memory created with 'new'
    delete[] B;
    delete[] C;
}


int main() {
    cout << "Enter the number of elements in the array: ";
    int size;
    cin >> size;
    int A[size];
    cout << "Enter the elements of the array:\n";
    for (int i = 0; i < size; i++)
        cin >> A[i];
    int n = size;
    

    cout << "\nArray Elements :\n" << endl;
    for (int i = 0; i < n; i++)
        cout << A[i] << "  ";

    cout << "\n\nSorted..!\n" << endl;
    mergeSort(A, n);

    for (int i = 0; i < n; i++)
        cout << A[i] << "  ";
    cout << endl;

    return 0;
}


//Sample Output:
Enter number of elements: 6
Enter elements:
12 11 13 5 6 7
Sorted array:
5 6 7 11 12 13
