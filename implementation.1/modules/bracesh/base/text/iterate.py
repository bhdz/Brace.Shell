class Visitor(object):
    def visit(target):
        pass

class Iterator(object):
    def __init__(self, root):
        self.it = iter(list(root))
        self.last_it = None
        self.visitor = Visitor()

    def __iter__(self):
        return self

    def next(self):
        try:
            item = next(self.it)
        except StopIteration:
            if self.last_it:
                self.it = self.last_it
                self.last_it = None
                return self.next()
            raise

        try:
            depth_it = Iterator(item)
            self.last_it = self.it
            self.it = depth_it

            return self.next()
        except:
            return item


def test_Iterator():
    struct = [1, 2, 3, [30, 31, 32, 33], 4, 5, [61,62], 13]
    it = Iterator(struct)

    while True:
        try:
            elem = next(it)
            print "elem =", elem
        except StopIteration:
            break

test_Iterator()

class BreadthFirst(Iterator):
    def __init__(self, root):
        self.queue = []

        it = iter(list(root))

        self.enqueue(it)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def __iter__(self):
        return self

    def next(self):
        it = self.dequeue()
        item = next(it)

        try:
            it2 = iter(item)
            self.enqueue(it2)
            self.enqueue(it)
            return self.next()
        except:
            pass

        self.enqueue(it)
        return item

def test_BreadthFirst():
    #struct = [1, 2, [3, 4], [20, [300]], [50, [600], [80, [900]]]]
    struct = [1, 2, [30, 40, 50], 5, 6, 7]
    it = BreadthFirst(struct)
    print ""
    while True:
        try:
            elem = next(it)
            print "elem =", elem
        except StopIteration:
            break

test_BreadthFirst()

class DepthFirst(object):
    def __init__(self, root):
        self.root = root
        self.it = iter(list(root))

    def next(self):
        item = next(self.it)
        try:
            depth_it = iter(list(item))
        except:
            self.visit

    def __iter__(self):
        return self
