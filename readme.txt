檔案格式說明

單位：以下單位都是 公尺

1. 節點

n1,0,0

表示  
"節點名稱",x軸 folat,y軸 float
節點名稱要以n開頭

2. 桿件

m7,n1,n2,0.18,0.2

表示
"桿件名稱","起始結點名稱","終點結點名稱",內徑 float, 外徑 float
桿件名稱要以 m 開頭 後面接數字
(外徑-內徑) 用來算斷面


3. 一定要先有節點資料才能有桿件資料


4. 節點桿件資料的 檔案名稱(*.txt) 以及 檔案名稱(*.ini)放在 config.ini 裡 

6. 執行順序
	取得 config.ini -> 取得 nodes 與 members (學號IN.ini or 學號IN.txt) -> 計算 -> 存檔 (學號OUT.txt or 學號OUT.txt)


執行方法

python3 main.py