from heapq import heapify, heappush, heappop
class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char        
        self.freq = freq         
        self.left = None          
        self.right = None        

class HuffmanTree:
    def __init__(self, frequencies):
        self.frequencies = frequencies

    
    def _insert(self, node: HuffmanNode):
        '''private method to insert new nodes'''
        pass

    def _build_tree(self):
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
            heappush((new_freq, new_node))
        return heappop(q)




