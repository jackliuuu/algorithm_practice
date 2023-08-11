class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def display(self):
        print(self.queue)

# 创建队列实例
queue = Queue()

# 入队操作
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# 显示队列
queue.display()  # 输出: [10, 20, 30]

# 出队操作
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  # 输出: Dequeued item: 10

# 显示队列
queue.display()  # 输出: [20, 30]

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 已排序的列表
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]

# 要查找的目标
target = 7

# 进行二分查找
index = binary_search(sorted_list, target)

if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found")