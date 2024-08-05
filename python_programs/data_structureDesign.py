class NumberStore:
    def __init__(self):
        self.numbers = []
    def add(self, number):
        self.numbers.append(number)
    def get_first_unique(self):
        res = set(self.numbers)
        for i in res:
            result = i
        return result
    
store = NumberStore()
store.add(1)
store.add(2)
store.add(1)


print(store.get_first_unique())

        