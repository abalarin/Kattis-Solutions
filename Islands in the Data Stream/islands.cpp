#include <iostream>
#include <string>
#include <sstream>
using namespace std;


int Treestruct(int *A, int x, int J, int islands);
int main() {
	int runs, seqNum[13];
	cin >> runs;

	int seq;
	string word;
	for (int i = 0; i < runs; i++) {
		cout << "Enter Num" << endl;

		int count = 0;
		while (cin >> seq) {
			if (count != 0) {
				int j = count - 1;
				seqNum[j] = seq;
			}
				count++;
			if (count == 13) break;
		}
		for (int j = 0; j < sizeof(seqNum); j++) {
			cout << seqNum[j] << endl;
		}
		cout << Treestruct(seqNum, 0, 0, 0) << endl;
	}

	system("pause");
}

int Treestruct(int *A, int x, int J, int islands) {
	cout << A[0] << endl;
	while(x != (sizeof(A) - 2)) {
		if (A[x] < A[x + 1]) {
			cout << A[x];
			Treestruct(A, x++, J++, islands++);
		}
		else if (x == (x + 1)) {
			x++;
		}
		else if (x < J) {
			return islands;
		}
		else {
			x++;
		}
	}
