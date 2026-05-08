code:

#include <iostream>
using namespace std;

int n, W;
int item[20], w[20], v[20];
float ratio[20];

int maxProfit = 0;
int bestSet[20];
int include[20];

float bound(int level, int weight, int profit) {
    if (weight >= W)
        return 0;

    float ub = profit;

    if (level + 1 < n) {
        ub += (W - weight) * ratio[level + 1];
    }

    return ub;
}

void knapsack(int level, int weight, int profit) {
    if (weight <= W && profit > maxProfit) {
        maxProfit = profit;
        for (int i = 0; i < n; i++)
            bestSet[i] = include[i];
    }

    if (level == n - 1)
        return;

    float ub = bound(level, weight, profit);

    if (ub <= maxProfit)
        return; // prune

    include[level + 1] = 1;
    knapsack(level + 1,
             weight + w[level + 1],
             profit + v[level + 1]);

    include[level + 1] = 0;
    knapsack(level + 1, weight, profit);
}

int main() {
    cout << "Enter number of items: ";
    cin >> n;

    cout << "\nEnter item, weight, value, value/weight:\n";
    for (int i = 0; i < n; i++) {
        cin >> item[i] >> w[i] >> v[i] >> ratio[i];
    }

    cout << "\nEnter knapsack capacity: ";
    cin >> W;

    knapsack(-1, 0, 0);

    cout << "\nSelected items:\n";
    for (int i = 0; i < n; i++) {
        if (bestSet[i] == 1) {
            cout << "Item " << item[i]
                 << " (W=" << w[i]
                 << ", V=" << v[i] << ")\n";
        }
    }

    cout << "\nMaximum Profit = " << maxProfit << endl;

    return 0;
}

//sample case:
Enter number of items: 4

Enter item, weight, value, value/weight:
1 4 40 10
2 7 42 6
3 5 25 5
4 3 12 4

Enter knapsack capacity: 10

Selected items:
Item 1 (W=4, V=40)
Item 3 (W=5, V=25)

Maximum Profit = 65
