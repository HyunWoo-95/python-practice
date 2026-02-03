class Node:
    # 칸에 있는 데이터, 다음 칸의 데이터만 가짐
    def __init__(self, data):
        self.data = data
        self.next = None


# node = Node(5)
# print(node.data, node.next)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # linked list의 가장 끝에 있는 노드에 새로운 노드를 연결

    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index != index:
            cur = cur.next
            cur_index += 1
        return cur

    def insert_node(self, index, value):
        new_node = Node(value)  # [12] 데이터가 있는 위치에 [7] 삽입
        if index == 0:
            new_node.next = self.head

            self.head = new_node
            return

        prev_node = self.get_node(index - 1)  # 새로운 데이터를 넣고자 하는 위치의 바로 앞의 데이터가 인덱스가 필요 -> [3]

        next_node = prev_node.next  # [3] -> [12]를 저장

        prev_node.next = new_node  # [3] - > [7]
        new_node.next = next_node  # [7] -> [12]

    def delete_node(self, index):
        # 인덱스가 0일 경우 에러가 발생해 head의 위치를 다음 노드로 이동 후 진행
        if index == 0:
            self.head = self.head.next
            return
        # 입력받은 인덱스의 바로 앞의 노드를 기억 후 입력된 인덱스의 +1의 노드로 바로 연결
        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        prev_node.next = index_node.next


linked_list = LinkedList(3)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()

print(linked_list.get_node(1).data)  # - > 12를 들고 있는 노드 반환 [3] -> [12] -[8]

linked_list.insert_node(1, 7)  # [3] -> [7] -> [12] -> [8]
linked_list.print_all()
