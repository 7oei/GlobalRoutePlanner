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

    int pnt[123]={}; //各英文字のポイント
    for(int i=97; i<=122; i++) pnt[i]=1;
    // j, k, qu, x, z
    pnt['j']=3; pnt['k']=3; pnt['q']=3; pnt['x']=3; pnt['z']=3; 
    // c,f,h,l,m,p,v,w,y
    pnt['c']=2; pnt['f']=2; pnt['h']=2; pnt['l']=2; pnt['m']=2; 
    pnt['p']=2; pnt['v']=2; pnt['w']=2; pnt['y']=2; 

    int flg = 0;
    vector<pair<int, string> > pair;
    int p_ans = 0; // 答え
    string word_ans; // 答え

    for(int i=0; i<dic.size(); i++){
        string word = dic[i];
        for(int j=0; j<word.size()/2; j++){
            // word[2*j]が 検索したい文字列に入ってる文字数 < 辞書の単語の文字数 の場合はダメ、次の単語を調べる
            if(alp[word[2*j]] < word[2*j+1]-48) break;
            if(j==word.size()/2-1){
                // 見つかったら
                int p=0;
                string ans = origin[i];
                for(int k=0; k<ans.size(); k++){
                    // ポイント計算
                    if (65 <= ans[k] && ans[k] <= 90) ans[k] = ans[k] + 32; // 小文字を大文字に
                    if(ans[k-1]=='q') continue; // 'qu'の処理. uを無視する
                    p += pnt[ans[k]];
                }
                // ポイント更新
                if (p_ans < (p+1)*(p+1)){
                    p_ans = (p+1)*(p+1);
                    word_ans = ans;
                }
                flg = 1;
            }
        }
    }

    if(flg == 0) cout<< "Not found" << endl;
    else cout << p_ans << " " << word_ans << endl;
    return 0;
}