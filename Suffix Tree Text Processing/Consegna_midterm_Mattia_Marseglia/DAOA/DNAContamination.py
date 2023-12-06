from SuffixTries import SuffixTree
from Contaminants_Tree import C_Tree

class DNAContamination:

    """this class extend SuffixTree to add a private method"""
    class _SuffixTreePlus(SuffixTree):

        """return the root of the suffix tree"""
        def _getroot(self):
            return self._root

    """ this function build a DNAContamination object; it takes in input the
        string s to verify and the contamination threshold l (the contaminant set C is initially
        empty)"""
    def __init__(self, s, l):
        if not isinstance(s, str):
            raise TypeError("s is not a string")
        self._s = s
        self._l = l
        self._C = C_Tree()

    """ this function adds contaminant c to the set C and saves the degree of
        contamination of s by c"""
    def addContaminant(self, contaminant):
        if not isinstance(contaminant, str):
            raise TypeError("parameter must be a string")
        c = contaminant
        s = self._SuffixTreePlus([c, self._s])
        root = s._getroot()
        index = 0
        real_index = 0
        set = []
        while c != "":
            child_pos = s.Child(root, c)
            condition = s.getNodeMark(child_pos) == (1, 2)
            if condition is False and len(c) > 0:
                c = c[1:]
                real_index += 1
                continue
            while (condition is not False) and len(c) >= self._l:
                label = s.getNodeLabel(child_pos)
                if (len(c) - index) > len(label):
                    index += len(label)
                else:
                    index += len(c) - index
                if c[index:] != "":
                    child_pos = s.Child(child_pos, c[index:])
                    condition = s.getNodeMark(child_pos) == (1, 2)
                else:
                    condition = False
            if index >= self._l:
                possible_up_degree_string = c[:index]
                if self._notin(set, possible_up_degree_string, real_index):
                    set += [(possible_up_degree_string, real_index)]
            if len(c) > 1 and len(c) >= self._l:
                c = c[1:]
                real_index += 1
            else:
                break
            index = 0
        self._C.__setitem__(len(set), contaminant)

    """ check if substring must be insered in the util set"""
    def _notin(self, sub, to_ins, real_index):
        for index, s in enumerate(sub):
            if len(s[0]) > len(to_ins) and to_ins in s[0] and (s[1]+len(s[0])) >= real_index:
                return False
        return True

    """ this function returns the k contaminants with larger degree of
        contamination among the added contaminants."""
    def getContaminants(self, k):
        list = []
        if not self._C.is_empty():
            tmp_pos = self._C.find_position(self._C.find_max()[0])
            list += [tmp_pos.element()._value]
            for i in range(k-1):
                tmp_pos = self._C.before(tmp_pos)
                list += [tmp_pos.element()._value]
        return list



