//
//  main.cpp
//  x
//
//  Created by Renato Rodrigues on 20/05/17.
//  Copyright © 2017 Renato Rodrigues. All rights reserved.
//


#include <iostream>
#include <sys/time.h>                // for gettimeofday()
#include <vector>

using namespace std;

int main()
{
    struct timeval t1, t;
    long double elapsedTime;
    vector<int> myvector;
    // start timer
    gettimeofday(&t1, NULL);
    t = (struct timeval){0};
    // compute and print the elapsed time in millisec
    //t = (struct timeval){0};
    int i = 0;
    while(t.tv_usec< 11.0){
        gettimeofday(&t, NULL);
        t.tv_usec = t.tv_usec - t1.tv_usec;
        myvector.push_back(t.tv_usec);
        i++;
    }
    return 0;
}





#include <iostream>
#include <sys/time.h>                // for gettimeofday()


int main()
{
    struct timeval t1, t;
    long double elapsedTime;
    // start timer
    gettimeofday(&t1, NULL);
    t = (struct timeval){0};
    // compute and print the elapsed time in millisec
    //t = (struct timeval){0};
    int i = 0;
    while(t.tv_usec< 10.0){
        gettimeofday(&t, NULL);
        t.tv_usec = t.tv_usec - t1.tv_usec;
        i++;
    }
    return 0;
}
