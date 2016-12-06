//
//  main.cpp
//  diffs
//
//  Created by Austin Balarin on 11/19/16.
//  Copyright © 2016 Austin Balarin. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    long long a, b;
    while(cin >> a >> b)
            if(a > b)
                cout << a-b << endl;
            else
                cout << b-a << endl;

    return 0;
}
