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
        self.decodings = self._build_decodings()

    def _build_tree(self):
        '''private method to build a H-tree'''
        q = [(f, HuffmanNode(c, f)) for c, f in self.frequencies.items()]
        heapify(q)
        # merge nodes until one remains (the root)
        while len(q) > 1:
            # take the 2 lowest freqency nodes
            freq1, node1 = heappop(q)
            freq2, node2 = heappop(q)

            # merge them, combine the frequencies
            new_freq = freq1 + freq2
            new_node = HuffmanNode('', freq1 + freq2)

            new_node.left = node1
            new_node.right = node2
            heappush(q, (new_freq, new_node))
        # return the root of the tree
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

    def _build_decodings(self):
        '''private method to build a decodings dict'''
        return { encoding : char for char, encoding in self.encodings.items() } 
    
    def encode(self, data):
        return ''.join([self.encodings[char] for char in data])
    
    def decode(self, data):
        decoded_message = []
        current_node = self.root

        for bit in data:
            if bit == '0':
                current_node = current_node.left
            elif bit == '1':
                current_node = current_node.right

            if current_node.left is None and current_node.right is None:
                decoded_message.append(current_node.char)
                current_node = self.root

        return ''.join(decoded_message)