import unittest

from homework import (CircularQueue, DataNotEnoughError, DequeueEmptyError,
                      EnqueueFullError)


class CircularQueueTest(unittest.TestCase):
    def test_enqueue_full_error(self):
        q = CircularQueue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        print(q.queue,q.front,q.rear)
        self.assertRaises(EnqueueFullError, q.enqueue,5)

    def test_dequeue_empty_error(self):
        q = CircularQueue(5)
        self.assertRaises(DequeueEmptyError,q.dequeue)

    def test_enqueue(self): # 測試新增資料
        q = CircularQueue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual([None,1,2,3,4],q.queue)
        self.assertEqual(q.size,4)
    
    def test_dequeue(self): # 測試移除資料，並且測試返回是否正確
        q = CircularQueue(5)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual([None,1,2,None,None],q.queue)
        self.assertEqual(q.rear,2)
        self.assertEqual(q.front,0)
        result = q.dequeue()
        self.assertEqual([None,None,2,None,None],q.queue)
        self.assertEqual(q.front,1)
        self.assertEqual(result,1) # 測試返回值是否正確
    
    def test_add_data_not_enough_error(self): # 測試相加資料但是資料不足二筆
        q = CircularQueue(5)
        q.enqueue(1)
        self.assertRaises(DataNotEnoughError,q.add)
    
    def test_sub_data_not_enough_error(self): # 測試相減資料但是資料不足二筆
        q = CircularQueue(5)
        q.enqueue(1)
        self.assertRaises(DataNotEnoughError,q.sub)
    
    def test_add_data(self): # 測試相加資料
        q = CircularQueue(5)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual([None,1,2,None,None],q.queue)
        self.assertEqual(q.size,2)
        self.assertEqual(q.front,0)
        self.assertEqual(q.rear,2)
        q.add()
        self.assertEqual([None,None,3,None,None],q.queue)
        self.assertEqual(q.front,1)
        self.assertEqual(q.rear,2)
        self.assertEqual(q.size,1)
    
    def test_sub_data(self): # 測試相減資料
        q = CircularQueue(5)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual([None,1,2,None,None],q.queue)
        self.assertEqual(q.size,2)
        self.assertEqual(q.front,0)
        self.assertEqual(q.rear,2)
        q.sub()
        self.assertEqual([None,None,-1,None,None],q.queue)
        self.assertEqual(q.front,1)
        self.assertEqual(q.rear,2)
        self.assertEqual(q.size,1)

if __name__ == '__main__':
    unittest.main()