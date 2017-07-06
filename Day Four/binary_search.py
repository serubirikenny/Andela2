class BinarySearch(list):
    def __init__(self, a, b):
        arr = [x for x in range(b, (a * b) + 1, b)]
        self.length = len(arr)
        super(BinarySearch, self).__init__(arr)

    def search(self, term):
        found, index = False, 0

        first = 0
        last = len(self) - 1

        count = 0

        if term == self[first]:
            found, index = True, first

        elif term == self[last]:
            found, index = True, last

        if term not in self:
            found, index = True, -1

        while first <= last and not found:
            half = (first + last) // 2
            if self[half] == term:
                found, index = True, half

            else:
                count += 1
                if term < self[half]:
                    last = half - 1
                else:
                    first = half + 1

        return {'count': count, 'index': index}
