## PROBLEM URL: https://leetcode.com/problems/design-browser-history/



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        current = self.current
        while current.prev and steps:
            current = current.prev
            steps -= 1
        return current.value

    def forward(self, steps: int) -> str:
        current = self.current
        while current.next and steps:
            current = current.next
            steps -= 1
        return current.value


if __name__ == "__main__":
    # Create a BrowserHistory object with the homepage
    browser_history = BrowserHistory("homepage.com")
    
    # Visit new pages
    browser_history.visit("page1.com")
    browser_history.visit("page2.com")
    browser_history.visit("page3.com")
    
    # Go back in history
    print(browser_history.back(1))
    print(browser_history.back(1))
    
    # Go forward in history
    print(browser_history.forward(1))
