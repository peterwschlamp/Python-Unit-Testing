class Stack:
    def push(self):
        return True

    def remove(self):
        return True

    def reflect(self, word):
        return word

    def count_ones(self, list_of_binaries):
        ones = list(filter(lambda x : x == 1, list_of_binaries))
        return len(ones)


