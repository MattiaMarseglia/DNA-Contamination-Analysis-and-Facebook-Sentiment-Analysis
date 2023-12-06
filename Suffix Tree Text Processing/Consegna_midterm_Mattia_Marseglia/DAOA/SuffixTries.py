class SuffixTree:

    """unit structure of the SuffixTree"""
    class _node:
        def __init__(self, children: "" = {}, membership_strings = (), start: int = None, stop: int = None, parent = None):
            self._membership_strings = membership_strings
            self._start = start
            self._stop = stop
            self._children = children
            self._parent = parent
            if parent is None or parent._node._start is None or parent._node._stop is None:
                self._depth_parent = 0
            else:
                self._depth_parent = parent._node._depth_parent + parent._node._stop - parent._node._start

    """wrap of the node"""
    class Position:
        # construct of the class that wrap private class _node
        def __init__(self, container, node):
            self._container = container
            self._node = node

        # return the value inside the node
        def element(self):
            if len(self._node._membership_strings) > 0:
                strings = self._container.text
                string = strings[int(self._node._membership_strings[0])-1]
                return string[self._node._start: self._node._stop]
            else:
                return ""

        # check if two position are equal
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    """check if the position p is validate, also for the considering tree"""
    def _validate(self, p):
        "Return the node contained in p if the Position is valid."
        if not isinstance(p, self.Position):
            raise TypeError('p deve essere di tipo Position')
        if p._container is not self:
            raise ValueError('p non appartiene a questo contenitore')
        return p._node

    """Return Position instance for given node (or None if no node)."""
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    """ this function creates a Suffix Tree starting from the tuple S of strings; each node
        of the tree, except the root, is marked with a reference to those strings in S for which
        there is a suffix going through node u; moreover, the substring associated to each
        node must not be explicitly represented in the tree (to this aim, S can be assumed to
        be an immutable object)"""
    def __init__(self, text: "" = []):
        self.text = text
        self._root = self.Position(self, self._node(parent=None))
        self._validate(self._root)._children = {}
        for s in text:
            for i in range(len(s)):
                self._ST_insert(self._root, s[-i-1:], len(s)-i-1, text.index(s)+1)

    """insert a suffix inside the SuffixTree, it belong to init function to initialize the tree"""
    def _ST_insert(self, root, suffix, start, mem_string):
        """insert of a suffix in the SuffixTree"""
        if suffix != "":
            """calculate eventually child from the parameter root"""
            hypothetical_child = self._validate(root)._children.get(suffix[0])
            """if there is a child that have prefixmatch with the suffix:"""
            if hypothetical_child:
                """extract the node from future _parent"""
                effective_child = self._validate(hypothetical_child)
                trans_child = {}
                """take the integral label from the child"""
                child_label = hypothetical_child.element()
                """calculate max prefix that match between node and suffix:"""
                prefix_length = self._max_Prefix_Match(child_label, suffix)
                if prefix_length == len(child_label):
                    if mem_string not in effective_child._membership_strings:
                        effective_child._membership_strings += (mem_string,)
                    self._ST_insert(hypothetical_child, suffix[prefix_length:], start+prefix_length, mem_string)
                    return
                new_left_child = child_label[prefix_length:] or "$"
                new_right_child = suffix[prefix_length:]
                if new_right_child == "":
                    new_right_child = "$"
                new_stop = effective_child._stop
                if effective_child._children:
                    trans_child = effective_child._children
                effective_child._children = {}
                """change new correct label for node to split (become internal)"""
                effective_child._label = child_label[0: prefix_length]
                effective_child._stop = effective_child._start + prefix_length
                effective_child._children.update(
                    {new_left_child[0]: self._make_position(
                                                            self._node(
                                                                        children=trans_child,
                                                                        membership_strings=effective_child._membership_strings,
                                                                        start=effective_child._start + prefix_length,
                                                                        stop=new_stop,
                                                                        parent=hypothetical_child,))}
                )
                effective_child._children.update(
                    {new_right_child[0]: self._make_position(
                                                            self._node(
                                                                        children={},
                                                                        membership_strings=(mem_string,),
                                                                        start=start + prefix_length,
                                                                        stop=start + len(suffix),
                                                                        parent=hypothetical_child,
                                                            )
                    )}
                )

                if mem_string not in effective_child._membership_strings:
                    effective_child._membership_strings += (mem_string, )
                """change for children his _parent"""
                new__parent = effective_child._children.get(new_left_child[0])
                _children_to_update = self._validate(new__parent)._children
                for child in _children_to_update:
                    self._validate(_children_to_update.get(child))._parent = new__parent

            else:
                if root == self._root:
                    self._validate(root)._children.update(
                        {suffix[0]: self._make_position(
                                                        self._node(
                                                                    children={},
                                                                    membership_strings=(mem_string,),
                                                                    start=start,
                                                                    stop=start + len(suffix),
                                                                    parent=root
                                                        )
                        )}
                    )
                else:
                    if self._validate(root)._children == {}:
                        new_left_child = "$"
                        self._validate(root)._children.update(
                            {new_left_child[0]: self._make_position(
                                                                    self._node(
                                                                                children={},
                                                                                membership_strings=(mem_string,),
                                                                                start=self._validate(root)._stop,
                                                                                stop=self._validate(root)._stop,
                                                                                parent=root
                                                                    )
                            )}
                        )
                    self._validate(root)._children.update(
                        {suffix[0]: self._make_position(
                                                        self._node(
                                                                    children={},
                                                                    membership_strings=(mem_string,),
                                                                    start=start,
                                                                    stop=len(suffix) + start,
                                                                    parent=root
                                                        )
                        )}
                    )
        else:
            Dollar_child_pos = self._validate(root)._children.get("$")
            if Dollar_child_pos:
                Dollar_child_node = self._validate(Dollar_child_pos)
                if mem_string not in Dollar_child_node._membership_strings:
                    Dollar_child_node._membership_strings += (mem_string, )

    """return the most length match between two string"""
    def _max_Prefix_Match(self, str1, str2):
        if len(str1) > len(str2):
            for_iter = len(str2)
        else:
            for_iter = len(str1)
        split_length = 0
        for i in range(for_iter):
            if str1[i] == str2[i]:
                split_length += 1
            else:
                break
        return split_length

    """ this function returns the substring that labels the node of T to which
        position P refers (it throws an exception if P is invalid)"""
    def getNodeLabel(self, p):
        self._validate(p)
        return p.element()

    """ this function returns the substring associated to the path in T from the root to
        the node to which position P refers (it throws an exception if P is invalid)"""
    def pathString(self, p):
        self._validate(p)
        if p == self._root:
            return ""
        else:
            return self.pathString(self._validate(p)._parent) + self.getNodeLabel(p)

    """ this function returns the length of substring associated to the path in T
        from the root to the node to which position P refers (it throws an exception if P is
        invalid)"""
    def getNodeDepth(self, p):
        node = self._validate(p)
        return node._depth_parent + node._stop - node._start

    """ this function returns the mark of the node u of T to which position P refers
        (it throws an exception if P is invalid)"""
    def getNodeMark(self, p):
        node = self._validate(p)
        return node._membership_strings

    """ this function returns the position of the child u of the node of T to which position P
        refers such that
            ○ either s is a prefix of the substring labeling u,
            ○ or the substring labeling u is a prefix of s,
        if it exists, and it returns None otherwise (it throws an exception if P is invalid or s is
        empty)."""
    def Child(self, p, s):
        node = self._validate(p)
        if s == "":
            raise ValueError("string is empty")
        child = node._children.get(s[0])
        if child is not None:
            label = child.element()
            match = self._max_Prefix_Match(label, s)
            if (match == len(label) or match == len(s)) and match != 0:
                return child
        else:
            return None

    """ #stamp of suffix tree (if you want to stamp) 
    def ST_print(self, root=None, count=1) -> str:
        if None == root:
            root=self._root
        tmp = self._validate(root)._children
        for i in tmp:
            a = self._validate(root)._children.get(i)
            print(count.__str__(), end="")
            print("st level son:", end="")
            if root.element() is not None:
                r_label = root.element()
                if r_label == "":
                    r_label += "$"
                print("of level " + (count-1).__str__() + " from elem " + r_label + ": ", end="")
            print(a.element())
            print(self._validate(a)._membership_strings.__str__())
            print(self._validate(a)._start.__str__() + ": " + self._validate(a)._stop.__str__())
            if self._validate(a)._children != {}:
                sons = self._validate(a)._children
                for son in sons:
                    son_label = sons.get(son).element()
                    if son_label == "":
                        son_label += "$"
                    print((count + 1).__str__() + "st level son from level " + (count).__str__() + " from elem " + a.element() + ": " +  son_label)
                    print(self._validate(sons.get(son))._membership_strings.__str__())
                    print(self._validate(sons.get(son))._start.__str__() + ": " + self._validate(sons.get(son))._stop.__str__())
                    self.ST_print(sons.get(son), count+2)"""



