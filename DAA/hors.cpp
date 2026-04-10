//Question 2: Horspool Pattern Searching
Code:

#include <iostream>
#include <string>
using namespace std;

const int SIZE = 256;
int table[SIZE];

void shiftTable(string P) {
    int m = P.length();

    for (int i = 0; i < SIZE; i++)
        table[i] = m;

    for (int j = 0; j < m - 1; j++)
        table[P[j]] = m - 1 - j;
}

int horspool(string P, string T) {
    int m = P.length();
    int n = T.length();

    shiftTable(P);

    int i = m - 1;

    while (i <= n - 1) {
        int k = 0;

        while (k < m && P[m - 1 - k] == T[i - k])
            k++;

        if (k == m)
            return i - m + 1;
        else
            i = i + table[T[i]];
    }

    return -1;
}

int main() {
    string text, pattern;

    cout << "Enter text: ";
    getline(cin, text);

    cout << "Enter pattern: ";
    getline(cin, pattern);

    int pos = horspool(pattern, text);

    if (pos == -1)
        cout << "Pattern not found";
    else
        cout << "\n";
        cout << "Pattern found at Index: " << pos;
        cout << "\nPattern found at position : " << pos + 1;
        cout << "\n\n";

    return 0;
}

//Sample Output:
Enter text: algorithms are fun
Enter pattern: fun
Pattern found at Index: 15
Pattern found at position : 16
