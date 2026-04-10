//Question 1: Selection Sort Algorithm
Code:

#include<iostream>
using namespace std;
int main() {
   int n, temp, min;
   cout << "Enter the no.of elements: ";
   cin >> n;
   int a[n];
   cout << "Enter the elements:\n";
   for (int i = 0; i < n; i++)
      cin >> a[i];
   cout << "Before sort:\n";
   for (int i = 0; i < n; i++)
      cout << a[i] << " ";
   cout << "\n";
   for (int i = 0; i < n - 1; i++) {
      min = i;
      for (int j = i + 1; j < n; j++) {
         if (a[j] < a[min])
            min = j;
      }
      if (min != i) {
         temp = a[i];
         a[i] = a[min];
         a[min] = temp;
      }
   }
   cout << "\nSorted array:\n";
   for (int i = 0; i < n; i++)
      cout << a[i] << " ";
   cout << "\n";
   cout << "\n";
   return 0;
}

//Sample Output:
Enter the no.of elements: 4
Enter the elements:
44 11 33 22
Before sort:
44 11 33 22
Sorted array:
11 22 33 44
