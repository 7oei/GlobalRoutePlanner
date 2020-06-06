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

    string s = argv[1]; // 検索する単語
    int alp[123]={}; // 各文字の現れた数をカウント
    // sの全ての文字について
    for(int i=0; i<s.size(); i++){ 
        if (65 <= s[i] && s[i] <= 90) s[i] = s[i] + 32; //大文字を小文字に変換
        alp[s[i]] ++; // カウント
    }


    // 辞書読み込み
    ifstream ifs("sample_sorted2.txt", ios::in);
    // エラー処理
    if(!ifs){
        cerr << "Error: file not opened." << endl;
        return 1;
    }

    string tmp;
    vector<string> dic; //処理後の単語(e1h1l2o1)、
    vector<string> origin; //originは処理前の単語(hello)
    
    int i=0;
    while(getline(ifs, tmp, ',')){
        if(i%2==0) dic.push_back(tmp); //e1h1l2o1
        else origin.push_back(tmp); //hello
        i++;
    }

    int flg = 0;
    // 全ての辞書の処理後の単語について ex) e1h1l2o1
    for(int i=0; i<dic.size(); i++){
        string word = dic[i];
        for(int j=0; j<word.size()/2; j++){
            // word[2*j]が 検索したい文字列に入ってる文字数 < 辞書の単語の文字数 の場合はダメ、次の単語を調べる
            if(alp[word[2*j]] < word[2*j+1]-48)  break;
            if(j==word.size()/2-1){
                // ループが最後まで行き着いたら出力
                cout<< origin[i] <<endl;
                flg = 1;
            } 
        }
    }
    // 一個も無かったら
    if(flg == 0) cout<< "Not found" << endl;
    return 0;

}