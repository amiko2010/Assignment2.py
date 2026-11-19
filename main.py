
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.data
            curr = curr.next

    def append(self, data):
        """O(1) სირთულის დამატება სიის ბოლოში"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
        
        if index == self._size:
            self.append(data)
            return

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        
        self._size += 1

    def delete_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        deleted_data = None
        if index == 0:
            deleted_data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            deleted_data = curr.next.data
            curr.next = curr.next.next
            if curr.next is None:
                self.tail = curr

        self._size -= 1
        return deleted_data


class TextEditor:
    def __init__(self):
        self.lines = SinglyLinkedList()
        self.undo_stack = []
        self.redo_stack = []

    def add_line(self, text):
        self.insert_line(len(self.lines), text)

    def insert_line(self, index, text):
        if index < 0 or index > len(self.lines):
            raise IndexError("Index out of bounds")
        
        self.lines.insert_at(index, text)
       
        self.undo_stack.append(("delete", index, text))
      
        self.redo_stack.clear()

    def delete_line(self, index):
        if index < 0 or index >= len(self.lines):
            raise IndexError("Index out of bounds")
        
        deleted_text = self.lines.delete_at(index)
        
        self.undo_stack.append(("insert", index, deleted_text))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return
        
        action, index, text = self.undo_stack.pop()
        
        if action == "insert":
            self.lines.insert_at(index, text)
            self.redo_stack.append(("delete", index, text))
        elif action == "delete":
            deleted_text = self.lines.delete_at(index)
            self.redo_stack.append(("insert", index, deleted_text))

    def redo(self):
        if not self.redo_stack:
            return
        
        action, index, text = self.redo_stack.pop()
        
        if action == "insert":
            self.lines.insert_at(index, text)
            self.undo_stack.append(("delete", index, text))
        elif action == "delete":
            deleted_text = self.lines.delete_at(index)
            self.undo_stack.append(("insert", index, deleted_text))

    def show(self):
        for i, text in enumerate(self.lines, 1):
            print(f"{i}: {text}")



