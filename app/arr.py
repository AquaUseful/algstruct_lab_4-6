import array
import random


class BinsearchArray:
    def __init__(self, size, typecode="I", fillgrow=10):
        self._size = size
        self._fillgrow = fillgrow
        self._typecode = typecode
        self.regenerate()

    def regenerate(self)->None:
        self._arr = array.array(self._typecode)
        self._arr.append(random.randrange(1, self._fillgrow + 1))
        for _ in range(self._size - 1):
            el = self._arr[-1] + random.randrange(1, self._fillgrow + 1)
            #el = self._arr[-1] + 10
            self._arr.append(el)
        # print(self._arr.tolist())

    def search_binary_unoptimal(self, key):
        left = 0
        right = self._size - 1
        while left <= right:
            i = (left + right) // 2
            if (self._arr[i] == key):
                return (True, i)
            elif (self._arr[i] > key):
                right = i - 1
            else:
                left = i + 1
        return (False, i)

    def search_binary_optimal(self, key):
        left = 0
        right = self._size - 1
        while left < right:
            i = (left + right) // 2
            if key <= self._arr[i]:
                right = i
            else:
                left = i + 1
        return (self._arr[right] == key, right)

    def search_binary_interpolate(self, key):
        left = 0
        right = self._size - 1

        while ((self._arr[left] < key) and (self._arr[right] > key)):
            i = left + ((key - self._arr[left])*(right - left)
                        ) // (self._arr[right] - self._arr[left])

            if self._arr[i] < key:
                left = i + 1
            elif self._arr[i] > key:
                right = i - 1
            else:
                return (True, i)

        if (self._arr[right] == key):
            return (True, right)
        elif (self._arr[left] == key):
            return (True, left)
        return (False, 0)

    def search_binary_sequental(self, key: int):
        pos = 0
        jmp = self._size // 2
        while (jmp > 0):
            while (((pos + jmp) < self._size) and (self._arr[pos + jmp] <= key)):
                pos += jmp
            jmp //= 2
        return (self._arr[pos] == key, pos)

    def search_sequental(self, key):
        self._arr.append(key + 1)
        index = 0
        while self._arr[index] < key:
            index += 1
        found = self._arr[index] == key
        self._arr.pop()
        return (found, index)

    def get_max(self):
        return self._arr[-1]
