class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_item

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# 创建队列实例
queue = Queue()

# 入队操作
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# 显示队列
queue.display()  # 输出: 10 20 30

# 出队操作
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  # 输出: Dequeued item: 10

# 显示队列
queue.display()  # 输出: 20 30
