class ListStartingFromOne:
    def __init__(self, list):
        self.values = list

    def __setitem__(self, key, value):
        self.values[key-1] = value

    def __getitem__(self, key):
        return self.values[key-1]

if __name__ == '__main__':
    weird_list = ListStartingFromOne([1, 2, 3, 5])
    print(weird_list.__getitem__(2))
    weird_list.__setitem__(4, 4)
    print(weird_list.__getitem__(4))
