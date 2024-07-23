from heapq import heapify, heappush, heappop
class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char        
        self.freq = freq         
        self.left = None          
        self.right = None 

    def __lt__(self, other):
        return self.freq < other.freq     

class HuffmanTree:
    def __init__(self, frequencies):
        self.frequencies = frequencies
        self.root = self._build_tree()
        self.encodings = self._build_encodings() 

    def _build_tree(self):
        '''private method to build a H-tree'''
        q = [(f, HuffmanNode(c, f)) for c, f in self.frequencies.items()]
        heapify(q)
        # merge nodes until one remains (the root)
        while len(q) > 1:
            # take 2 lowest freqency nodes
            freq1, node1 = heappop(q)
            freq2, node2 = heappop(q)

            # merge them, combine the freq
            new_freq = freq1 + freq2
            new_node = HuffmanNode('', freq1 + freq2)

            new_node.left = node1
            new_node.right = node2
            heappush(q, (new_freq, new_node))
        return heappop(q)[1]
     
    def _build_encodings(self):
        '''private method to build an encodings dict'''
        encodings = {}
        def dfs(node, path):
            if node is None:
                return
            if node.left is None and node.right is None:
                encodings[node.char] = path
                return
            dfs(node.left, path + '0')
            dfs(node.right, path + '1')

        dfs(self.root, '')
        return encodings    


