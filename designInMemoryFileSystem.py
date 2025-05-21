from typing import List
'''
Seems fairly easy:
Use a trie, the things separated by / tell you how to move through it
Let's get to work!
'''

class Node:
    def __init__(self):
        self.children = {}
        self.content = ""
        self.isFile = False
class FileSystem:
    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        node, name = self._traverse(path)
        if node.isFile:
            return [name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path, create=True)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node, name = self._traverse(filePath, create=True)
        node.isFile = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node, _ = self._traverse(filePath)
        return node.content

    # standard trie traversal
    def _traverse(self, path: str, create: bool = False) -> (Node, str):
        parts = [p for p in path.split('/') if p]
        node = self.root
        
        for i, part in enumerate(parts):
            if part not in node.children:
                node.children[part] = Node()
            node = node.children[part]
            
        name = parts[-1] if parts else ""
        return node, name
