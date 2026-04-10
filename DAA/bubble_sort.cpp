//Question 1: Optimized Bubble Sort
Code:

#include<iostream>
using namespace std;
int main(){
   int n;
   cout << "Enter no.of Elements: ";
   cin >> n;
   int arr[n];
   cout << "Enter " << n << " Elements: \n";
   for (int i=0;i<n;i++)
      cin >> arr[i];
   cout << "\nBefore sort:\n";
   for ( int i=0 ; i < n ; i++)
      cout << arr[i] << " ";
   for (int i=0 ; i < n-1 ; i++){
      bool swap = false;
      for (int j=0 ; j < n-i-1 ; j++){
         if (arr[j] > arr[j+1]){
            int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
            swap = true;
         }
      }
      if (!swap)
         break;
   }
   cout << "\n\nsorted array:\n";
   for (int i = 0 ; i < n ; i++){
      cout << arr[i] <<" ";
   }
   cout << "\n\n";
   return 0;
}

//Sample Output:
Enter no.of Elements: 5
Enter 5 Elements:
50 10 40 20 30

Before sort:
50 10 40 20 30

sorted array:
10 20 30 40 50
