# 1472. Design Browser History

class Node:
    def __init__(self, url=None):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:

    # start at homepage
    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    # visit another page/pages, the data will be added to history
    def visit(self, url: str) -> None:
        self.new_node = Node(url)
        self.curr.next = self.new_node
        self.new_node.prev = self.curr
        self.curr = self.curr.next

    # go back to previously visited pages
    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.url

    # go forward in history
    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.url

obj = BrowserHistory('Google')
obj.visit('Leetcode')
obj.visit('YouTube')
obj.visit('LinkedIn')
print(obj.back(2))  # Leetcode
print(obj.forward(1))  # YouTube
obj.visit('Twitter')
obj.visit('Angelist')
print(obj.back(3))  # Leetcode because the history of visiting LinkedIn got erased when we went to Twitter after
# going back to YouTube
