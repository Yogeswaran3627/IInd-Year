code:

#include <iostream>
using namespace std;

struct Node {
    char data;
    float freq;
    Node *left, *right;
};

Node* create(char data, float freq) {
    Node* temp = new Node();
    temp->data = data;
    temp->freq = freq;
    temp->left = temp->right = NULL;
    return temp;
}

void findMin(Node* arr[], int n, int &min1, int &min2) {
    min1 = min2 = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == NULL) continue;
        if (min1 == -1 || arr[i]->freq < arr[min1]->freq) {
            min2 = min1;
            min1 = i;
        } else if (min2 == -1 || arr[i]->freq < arr[min2]->freq) {
            min2 = i;
        }
    }
}

void print(Node* root, string code) {
    if (!root) return;
    if (!root->left && !root->right)
        cout << root->data << " = " << code << endl;
    print(root->left, code + "0");
    print(root->right, code + "1");
}

int main() {
    int n;
    cout << "Enter the number of characters: ";
    cin >> n;

    Node* arr[100];
    cout << "Enter character and frequency pairs (e.g., b 0.1):" << endl;
    for (int i = 0; i < n; i++) {
        char c;
        float f;
        cin >> c >> f;
        arr[i] = create(c, f);
    }

    int current_nodes = n;
    while (true) {
        int min1, min2;
        findMin(arr, current_nodes, min1, min2);

        if (min2 == -1) break;

        // Create internal node with sum of frequencies
        Node* temp = create('$', arr[min1]->freq + arr[min2]->freq);
        temp->left = arr[min1];
        temp->right = arr[min2];

        arr[min1] = NULL;
        arr[min2] = NULL;
        arr[current_nodes++] = temp;
    }

    cout << "\nOutput :\n";
    Node* root = arr[current_nodes - 1];
    print(root, "");
    cout << "\n";
    return 0;
}


//sample case:
Enter the number of characters: 5
Enter character and frequency pairs (e.g., b 0.1):
A 0.35
B 0.21
C 1
D 0.6
- 0.1

Output :
C = 0
D = 10
- = 1100
B = 1101
A = 111
