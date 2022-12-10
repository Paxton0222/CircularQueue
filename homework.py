class DequeueEmptyError(Exception):
    """如果Dequeue的時候 Queue 是空的"""
    pass

class EnqueueFullError(Exception):
    """如果Enqueue的時候 Queue 是滿的"""
    pass

class DataNotEnoughError(Exception):
    """如果Queue 中的資料不足一筆"""
    pass

class CircularQueue(object):
    def __init__(self,limit: int = 5):
        self.limit = limit
        self.queue = [None for i in range(limit)] # 創建環狀佇列
        self._front = 0
        self._rear = 0
        self._size = 0
    
    @property
    def size(self): # 取得 size 的值 (getter)
        return self._size

    @size.setter
    def size(self,size): # 更換 size 的值 (setter)
        self._size = size
    
    @property
    def is_empty(self): # 取得 is_empty 的值 (getter)
        return self.front == self.rear
    
    @property
    def is_full(self): # 取得 is_full 的值 (setter)
        return self.rear == self.front
    
    @property
    def front(self): # front 位置 (getter)
        return self._front
    
    @front.setter # front 位置 (setter)
    def front(self,index: int):
        self._front = index
    
    @property
    def rear(self): # rear 位置 (getter)
        return self._rear
    
    @rear.setter # rear 位置 (setter)
    def rear(self,index: int):
        self._rear = index

    def next(self,pointer: int, index: int): # 計算環狀佇列的第 index 筆資料
        return (pointer+index) % self.limit

    def push_front(self): # front 向前推進
        self.front = self.next(self.front,1)
        self.size-=1 # size 減一
    
    def push_rear(self): # rear 向前推進
        self.rear = self.next(self.rear,1)
        self.size+=1 # size 加一
    
    def back_rear(self,rear): # rear 回朔
        self.rear = rear
        self.size-=1 # size 減一

    def enqueue(self, value: int): # 將資料放入環狀佇列
        rear = self.rear # 先紀錄 rear
        self.push_rear() # 先計算欲加入資料的位置
        if self.is_full: # 先檢查環狀佇列是否是滿的
            self.back_rear(rear) # 回推 rear
            raise EnqueueFullError("佇列是滿的，無法執行 Enqueue")
        self.queue[self.rear] = value
    
    def dequeue(self): # 將資料從環狀佇列刪除
        if self.is_empty: # 先檢查環狀佇列是否是空的
            raise DequeueEmptyError("佇列是空的，無法執行 Dequeue")
        self.push_front() # 先計算欲刪除資料所在的位置
        result = self.queue[self.front]
        self.queue[self.front] = None # 刪除資料
        return result
    
    def add(self): # 將 queue 中的 兩筆資料相加以後再存回 queue 內，但是 queue 內 資料少於兩筆的時候，則拋出異常
        if self.size <= 1: # 資料不足於一筆
            raise DataNotEnoughError("資料不足一筆，不能相加")
        
        # 取得環狀佇列前端第一和第二個元素，將其相加，並置換最前面的元素
        first,second = self.queue[self.next(self.front,1)] , self.queue[self.next(self.front,2)]
        self.queue[self.next(self.front,1)] = None
        self.queue[self.next(self.front,2)] = first+second
        self.push_front()

    def sub(self): # 將 queue 中的 兩筆資料相減以後再存回 queue 內，但是 queue 內 資料少於兩筆的時候，則拋出異常
        if self.size <= 1: # 資料不足於一筆
            raise DataNotEnoughError("資料不足一筆，不能相減")
        
        # 取得環狀佇列前端第一和第二個元素，將其相減，並置換最前面的元素
        first,second = self.queue[self.next(self.front,1)] , self.queue[self.next(self.front,2)]
        self.queue[self.next(self.front,1)] = None
        self.queue[self.next(self.front,2)] = first-second
        self.push_front()

    def print_queue(self):
        for i in self.queue:
            print(i, end=" ")
    
    def display(self):
        self.print_queue()
        print()
    
    def front_to_rear(self): # 取出 front -> rear 的資料
        if self.size < 1:
            raise DataNotEnoughError("資料不足一筆，沒有資料可以顯示")
        result = []
        if self.is_empty:
            return result
        else:
            if self.rear > self.front:
                for i in range(self.front+1,self.rear+1):
                    result.append(self.queue[i])
            else:
                i = self.front
                while True:
                    i = (i+1) % self.limit
                    result.append(self.queue[i])
                    if i == self.rear:
                        break
        return result

    def first(self): # 取得環狀佇列的第一筆資料
        if self.size < 1:
            raise DataNotEnoughError("資料不足一筆，沒有第一筆資料")
        return self.queue[self.next(self.front,1)]

    def __str__(self):
        self.display()

    def __repr__(self):
        self.display()

class Homework:
    def __init__(self):
        self.queue = CircularQueue(5)
    
    def enqueue(self, value: int):
        try:
            self.queue.enqueue(value)
        except EnqueueFullError as e:
            print(e)
    
    def dequeue(self):
        try:
            data = self.queue.dequeue()
            print(f"取出之元素為: {data}")
        except DequeueEmptyError as e:
            print(e)
    
    def add(self):
        try:
            self.queue.add()
        except DataNotEnoughError as e:
            print(e)
    
    def sub(self):
        try:
            self.queue.sub()
        except DataNotEnoughError as e:
            print(e)
    
    def list(self):
        try:
            result: list = self.queue.front_to_rear()
            reverse_list = result[::-1]
            print(f"目前佇列的內容 (由 Rear 至 Front) 為: ",end=" ")
            for i in reverse_list:
                print(i,end=" ")
            print()
        except DataNotEnoughError as e:
            print(e)
    
    def front_item(self):
        try:
            first = self.queue.first()
            print(f"位於佇列Front端的一個元素為: {first}")
        except DataNotEnoughError as e:
            print(e)
    
    def exit(self):
        print("程式執行完畢")
        exit()

if __name__ == "__main__":
    homework = Homework()
    while 1:
        try:
            option = input("請輸入你選擇的工作: ")
            if option == "e": # enqueue
                value = input("請輸入數值: ")
                homework.enqueue(int(value))
            elif option == "d": # dequeue
                homework.dequeue()
            elif option == "a": # add
                homework.add()
            elif option == "s": # sub
                homework.sub()
            elif option == "l": # list
                homework.list()
            elif option == "f": # front item
                homework.front_item()
            elif option == "x": # exit
                homework.exit()
            else:
                print("查無此項功能，請重新輸入!")
        except ValueError as e:
            print("輸入數值必須是數字!")