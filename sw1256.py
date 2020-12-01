import sys

sys.stdin = open("sw1256.txt", "r")


class Node(object):
    """
    Node Class
    """
    
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    """
    docstring
    """
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            
            curr_node = curr_node.children[char]
        
        curr_node.data = string
    
    def find_N_suffix(self, N):
        curr_node = self.head

        stack = []
        count = 0

        stack.append(curr_node)

        while stack:
            curr_node = stack.pop()
            if curr_node.data != None:
                count += 1
            if count == N:
                return curr_node.data
            for char, child in sorted(curr_node.children.items(), reverse=True):
                
                stack.append(child)
        
        return 0



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    String = input()

    trie = Trie()

    for i in range(len(String)):
       trie.insert(String[i:])

    result = trie.find_N_suffix(n)

    print(result) 
