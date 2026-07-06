class page:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = page(homepage)
         
     

    def visit(self, url: str) -> None:
        newPage = page(url)
        if self.current is None:
            self.current = newPage
        else:
            print(self.current.val)
            self.current.next = newPage
            newPage.prev= self.current
            self.current = newPage




    def back(self, steps: int) -> str:
        while steps >0 and self.current.prev:
            self.current = self.current.prev
            steps -=1
        return self.current.val

        

    def forward(self, steps: int) -> str:
        while steps >0 and self.current.next:
            self.current = self.current.next
            steps -=1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)