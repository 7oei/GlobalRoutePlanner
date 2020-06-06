// ./anagram words
// woodsは検索したい文字列

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <stdio.h>
#include <algorithm>

int main(int argc, char* argv[]){
    using namespace std;

    // エラー処理
    if(argc != 2){
        cerr << "input ./getline input.txt" << endl;
        return 1;
    }

    // 検索する単語
    string s = argv[1];
    for(int i=0; i<s.size(); i++){ //大文字を小文字に変換
        if (65 <= s[i] && s[i] <= 90){
            s[i] = s[i] + 32;
        }
    }
    sort(s.begin(), s.end()); // sort

    ifstream ifs("sample_sorted.txt", ios::in); // 読み込み

    // エラー処理
    if(!ifs){
        cerr << "Error: file not opened." << endl;
        return 1;
    }

    string tmp, st;
    vector<string> dic, origin; //dicはsort後の単語、originはsort前の単語
    int i=0;
    while(getline(ifs, tmp, ',')){ //カンマ区切りで読み込み
        if(i%2==0) dic.push_back(tmp);
        else origin.push_back(tmp);
        i++;
    }

    auto iter = lower_bound(dic.begin(), dic.end(), s); //二分探索
    if (dic[iter - dic.begin()] == s){ //sと同じだったら
        cout << origin[iter - dic.begin()] << endl;
        return 1;
    }
    cout<< "Not found" << endl;
    return 0;
}