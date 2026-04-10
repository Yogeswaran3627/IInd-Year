//Question 1: Naive Pattern Searching
Code:

#include <iostream>
#include <string>
using namespace std;
int main() {
    string text, pattern;
    bool found = false;
    cout << "Enter text: ";
    getline(cin,text);
    cout << "Enter pattern: ";
    getline(cin,pattern);
    int n = 0;
    while (text[n] != '\0') {
       n++;
    }
    int m = 0;
    while (pattern[m] != '\0') {
       m++;
    }
    for (int i = 0; i <= n - m; i++) {
        int j;
        for (j = 0; j < m; j++) {
            if (text[i + j] != pattern[j]) {
                break;
            }
        }
        if (j == m) {
            cout << "\nPattern found at index: " << i << endl;
            cout << "\nPosition of a letter: " << i+1 << endl;
            found = true;
            break;
        }
    }
    if (!found) {
        cout << "Pattern not found" << endl;
    }
    return 0;
}

//Sample Output:
Enter text: Hello World
Enter pattern: World
Pattern found at index: 6
Position of a letter: 7
