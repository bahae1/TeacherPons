class Set:
    def _ _init_ _(self, *args):
        self._dict = {}
        for arg in args:
            self.add(arg)

    def _ _repr_ _(self):
        import string
        elems = map(repr, self._dict.keys(  ))
        elems.sort(  )
        return "%s(%s)" % (self._ _class_ _._ _name_ _, string.join(elems, ', '))

    def extend(self, args):
        """ Add several items at once. """
        for arg in args:
            self.add(arg)

    def add(self, item):
        """ Add one item to the set. """
        self._dict[item] = item

    def remove(self, item):
        """ Remove an item from the set. """
        del self._dict[item]
