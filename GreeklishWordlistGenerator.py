# -*- coding: utf-8 -*-
dictionary = {
    u'αι': ['e', 'ai'],
    u'ει': ['i', 'ei'],
    u'οι': ['i', 'oi'],
    u'ου': ['u', 'ou'],

    u'αυ': ['av', 'ab'],
    u'ευ': ['ev', 'eb'],
    u'μπ': ['mp', 'b'],
    u'ντ': ['nt', 'd'],

    u'α': ['a'],
    u'β': ['b', 'v'],
    u'γ': ['g'],
    u'δ': ['d'],
    u'ε': ['e'],
    u'ζ': ['z'],
    u'η': ['i', 'h'],
    u'θ': ['th', '8'],
    u'ι': ['i'],
    u'κ': ['k'],
    u'λ': ['l'],
    u'μ': ['m'],
    u'ν': ['n'],
    u'ξ': ['ks', 'x'],
    u'ο': ['o'],
    u'π': ['p'],
    u'ρ': ['r'],
    u'σ': ['s'],
    u'ς': ['s'],
    u'τ': ['t'],
    u'υ': ['y', 'u'],
    u'φ': ['f'],
    u'χ': ['x'],
    u'ψ': ['ps', 'y'],
    u'ω': ['w', 'o'],

}
#define a tree node
class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
#define a tree structure
class Tree:
    def __init__(self):
        self.root = TreeNode('')
    #returns all posible paths, from root to leaves
    def mytraverse(self,treenode, path,res):
        path = path + treenode.data
        for item in treenode.children:
            if item.children is not None and item.children:
                self.mytraverse(item, path,res)
            else:
                #print(path + item.data + "\n")  # print(path+tree.name+"\n")
                res.extend([path + item.data])

    #return all leaf nodes of the tree
    def get_leaf_nodes(self):
        leafs = []
        def _get_leaf_nodes( node):
            if node is not None:
                if len(node.children) == 0:
                    leafs.append(node)
                for n in node.children:
                    _get_leaf_nodes(n)
        _get_leaf_nodes(self.root)

        return leafs

    #add new nodes, to all leaf nodes
    def addtoAll(self, nodelist):
        leafs = self.get_leaf_nodes()
        for x in leafs:
            for node in nodelist:
                x.add_child(TreeNode(node.data))

    #print current leaf nodes
    def print_leaf_nodes(self):
        print("*********leaves *************************")
        for leaf in self.get_leaf_nodes():
            print(leaf.data)
        print("*********leaves *************************")

#iterator that returns corresponding result letter, using dictionary
def rearenge_it(dictionary,value):
    myiter = iter(xrange(0, len(value), 1))
    for i in myiter:
        first = value[i]
        if i < len(value) - 1:
            second = value[i + 1]
            if first + second in dictionary:
                #for i in dictionary[first + second]:
                #    yield  [i]
                yield dictionary[first + second]
                next(myiter, None)
            else:
                if first in dictionary:
                    yield dictionary[first]
                else:
                    yield [first]
        else:
            if first in dictionary:
                yield dictionary[first]
            else:
                yield [first]

#returns all possible representations of a string
def getMutations(dictionary,value):
    tr2 = Tree()
    res = []
    for y in rearenge_it(dictionary,unicode(value,"utf-8")):
        n = []
        for z in y:
            n.extend([TreeNode(z)])
        tr2.addtoAll(n)
    tr2.mytraverse(tr2.root, '', res)
    return res
#clean string from special vowels
def cleanString(input):
    # type: (object) -> object
    input = input.replace('ά', 'α')
    input = input.replace('έ', 'ε')
    input = input.replace('ή', 'η')
    input = input.replace('ί', 'ι')
    input = input.replace('ϊ', 'ι')
    input = input.replace('ό', 'ο')
    input = input.replace('ύ', 'υ')
    input = input.replace('ϋ', 'υ')
    input = input.replace('ώ', 'ω')
    return input

def test_project(input):
    input = cleanString(input)
    print("source: " + input + "\n")
    mutations = getMutations(dictionary,input)
    #print(mutations)
    print("result:")
    for idx,word in enumerate(mutations):
        print(str(idx) + ": " +word)

import codecs
if __name__ == '__main__':
    input_file =  "wordlist_grek.txt"
    output_file = "wordlist_greklish.txt"
    #test_project("γράψε μία πρόταση, εδώ πέρα")
    with codecs.open(input_file, 'r', encoding='utf8') as f:
        for line in f:
            word = line.split(None, 1)[0].encode('utf-8')
            word = cleanString(word)
            mutations = getMutations(dictionary, word)
            for idx, word in enumerate(mutations):
                with codecs.open(output_file, 'a', encoding='utf8') as fout:
                    fout.write(word+"\r\n")
                #print(str(idx) + ": " + word)