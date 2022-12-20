#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MOD 1000000007

char rps_oppo(char s){
    if(s=='R') return 'P';
    else if(s=='P') return 'S';
    else            return 'R';
}

char state_char(int i){
    if(i==0) return 'R';
    else if(i==1) return 'P';
    else          return 'S';
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin>>n;
    vector<char> INstate(n);
    vector<vector<int>> INmat(n,vector<int>(3,0));
    for(int i=0;i<n;i++){
        cin>>INstate[i];
        cin>>INmat[i][0]>>INmat[i][1]>>INmat[i][2];
    }
    
    vector<char> OUTstate(n+10);
    vector<vector<int>> OUTmat(n+10,vector<int>(3,-1));

    // Here I Reverse all the states first          - (1)
    for(int i=0;i<n;i++){
        OUTstate[i]=rps_oppo(INstate[i]);
    }

    // for INPUT if start state is ----> R(p)->S  with S state number 4
    // Then OUTPUT matrix will have R in state 4 as (1)
    // Now for OUTPUT mat --> start state is S and S(r)-> state 4 which has R in it.

    map<char,int> mp;
    mp['R']=0;
    mp['P']=1;
    mp['S']=2;


    int currst1,currst2,nextst1,nextst2;
    for(int j=0;j<n;j++){
        currst1=j,currst2=0;
        for(int i=0;i<300;i++){                 // RUN FOR 300 R0UNDS ONLY AS THERE WILL BE REPITITIONS
            nextst1=INmat[currst1][mp[OUTstate[currst2]]];
            nextst1--;
            if(OUTmat[currst2][mp[INstate[currst1]]]==-1){
                OUTmat[currst2][mp[INstate[currst1]]]=nextst1;
                nextst2=nextst1;        
                // if the transition is already filled then don't update nextst2!!
                // stay in the previous transition only
            }
            currst1=nextst1;
            currst2=nextst2;
        }
    }

    for(int i=0;i<n;i++){
        if(OUTmat[i][0]==-1) OUTmat[i][0]=0;
        if(OUTmat[i][1]==-1) OUTmat[i][1]=0;
        if(OUTmat[i][2]==-1) OUTmat[i][2]=0;
    }

    // PRINT STATE TRANSITIONS
    // vector<char> ar1,ar2;
    // for(int j=0;j<n;j++){
    //     currst1=j,currst2=0;
    //     for(int i=0;i<17;i++){
    //         nextst1=INmat[currst1][mp[OUTstate[currst2]]];
    //         nextst1--;
    //         nextst2=OUTmat[currst2][mp[INstate[currst1]]];
    //         ar1.push_back(INstate[currst1]);
    //         ar2.push_back(OUTstate[currst2]);
    //         // printf("%s\t%s\n",INstate[currst1],OUTstate[currst2]);
    //         currst1=nextst1;
    //         currst2=nextst2;
    //     }
    //     for(int i=0;i<ar1.size();i++){
    //         cout<<ar1[i]<<" ";
    //     }
    //     cout<<"\n";
    //     for(int i=0;i<ar2.size();i++){
    //         cout<<ar2[i]<<" ";
    //     }
    //     cout<<"\n\n";
    //     ar1.clear();ar2.clear();
    // }
    // PRINT STATE TRANSITIONS

    cout<<n<<"\n";
    for(int i=0;i<n;i++){
        cout<<OUTstate[i]<<" ";
        cout<<OUTmat[i][0]+1<<" "<<OUTmat[i][1]+1<<" "<<OUTmat[i][2]+1<<"\n";
    }

    return 0;
}