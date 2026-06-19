class Page:
    def __init__(self, url=None, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Page(homepage)

    def visit(self, url: str) -> None:
        new_page = Page(url)
        self.curr.next = new_page
        new_page.prev = self.curr
        self.curr = new_page


    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                return self.curr.url
        return self.curr.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                return self.curr.url
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)