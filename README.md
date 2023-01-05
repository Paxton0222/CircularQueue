# CircularQueue (環狀佇列) 課堂作業

這是一個環狀佇列的 Python 實現，你可以單獨把 CircularQueue 類拿出來直接在項目內做使用，類入參就是初始環狀佇列占用記憶體空間的上限

## Property (public)
- size 環狀佇列長度
- front 環狀佇列最前面元素的指針
- rear 環狀佇列最後面元素的指針
- queue 取得環狀佇列本體

## Methods (public)
- enqueue(value: int) 將資料放入環狀佇列
- dequeue() 將資料從環狀佇列刪除
- add() 將 queue 中的 兩筆資料相加以後再存回 queue 內，但是 queue 內 資料少於兩筆的時候，則拋出異常
- sub() 將 queue 中的 兩筆資料相減以後再存回 queue 內，但是 queue 內 資料少於兩筆的時候，則拋出異常
- first() 取得環狀佇列的第一筆資料
- front_to_rear() 顯示環狀佇列前到後的所有元素
