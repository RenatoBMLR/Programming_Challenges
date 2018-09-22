//
//  main.c
//  Hasmat
//
//  Created by Renato Rodrigues on 19/03/17.
//  Copyright © 2017 Renato Rodrigues. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    
    long long n, m;
    while (cin>>n>>m){
        if(n<m)cout<<m-n<<endl;
        else cout<<n-m<<endl;
    }
    return 0;
    
    
}
