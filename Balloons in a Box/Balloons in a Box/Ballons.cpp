#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <cstring>
#include <valarray>
#define V 6
# define M_PI           3.14159265358979323846  /* pi */

using namespace std;

double calc_volume(double r[V], int n){
    double volume=0.0;
    
    for (int i=0; i<n; i++) {
        volume=volume+(4.0/3.0)*M_PI*pow((r[i]),3);
    }
    return round(volume);
}


int distance_parede(int balon[V][V], int box[2][3], int index){

    int aux[3];
    
    for (int k=0; k<3; k++) {
        aux[k]=min(abs(balon[index][k]-box[0][k]), abs(balon[index][k]-box[1][k]));
    }

    return min(min(aux[0], aux[1]), aux[2]);
}



int distance_balons(int balon[V][V], int index1, int index2){
    int dist_centre;
    dist_centre=pow(balon[index1][0]-balon[index2][0],2)+pow(balon[index1][1]-balon[index2][1],2)+pow(balon[index1][2]-balon[index2][2],2);
    return dist_centre;
}


double minimo(double x, double y){

    if (x>y) {
        return y;
    }
    else{
        return x;
    }
}

int solve(int balon[V][V], int box[2][3], int n, int flag[V], int v_box){
    
    double r[V], dist_centre, auxV;

    
    int myints[] = {0,1,2,3,4,5};
    double volume=0.0;
    memset(r, 0.0, sizeof(double) * V);


    do {
        memset(r, 0.0, sizeof(double) * V);


        for (int i=0; i<n; i++) {
            
            if (flag[myints[i]]!=1) {
                r[myints[i]]=distance_parede(balon, box, myints[i]);
                
                for (int j=0; j<i; j++) {
                    
                    dist_centre=distance_balons(balon, myints[i], myints[j]);
                    
                    if (dist_centre<pow(r[myints[i]]+r[myints[j]],2)) {
                        
                        double auxx=sqrt(dist_centre)-r[myints[j]];
                        
                        if (auxx<0) {
                            r[myints[i]]=0;
                        }
                        else{
                            r[myints[i]]=minimo(distance_parede(balon, box, myints[i]), auxx);
                        }
                    }
                    
                }
            }

        }
        
        auxV=calc_volume(r, n);
        if (auxV>volume) {
            volume=auxV;
        }
        
        
    } while ( std::next_permutation(myints,myints+n) );
   
    return v_box-volume;

    
    
    
}


int main() {
    int n, box[2][3], balon[V][V],flag[V], temp;
    int result=0;
    int v_box;
    int a=1;
    cin>> n;
    
    while (n!=0) {
        memset(box, 0, sizeof(box[0][0]) * 2 * 3);
        memset(balon, 0, sizeof(balon[0][0]) * V * V);
        memset(flag, 0, sizeof(flag[0]) * V);
        for (int j=0; j<2; j++) {
            for (int i=0; i<3; i++) {
                cin>>temp;
                box[j][i]=temp;
            }
        }
        for (int i=0; i<n; i++) {
            for (int k=0; k<3; k++) {
                cin>>temp;
                
                if (temp>max(box[0][k],box[1][k])||temp<min(box[0][k],box[1][k])||temp == box[0][k]||temp == box[1][k]) {
                    flag[i]=1;
                }
                balon[i][k]=temp;
            }
        }
        
        v_box=(abs(box[0][0]- box[1][0]))*(abs(box[0][1]- box[1][1]))*(abs(box[0][2]-box[1][2]));

        valarray<int> myvalarray (flag,V);
        
        if (myvalarray.sum()==n) {
            printf("Box %d: %d\n",a, v_box);
        }

        else{
            result=solve(balon, box, n, flag, v_box);
            printf("Box %d: %d\n",a, result);
        }
        
        
        a+=1;
        cin>> n;
            cout<<"\n";


    }
    return 0;
}
