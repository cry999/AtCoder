class Brainfuck:
    def __init__(self):
        self.__pointer = 0
        self.__program = ''

        # 0 番地はバッファに使いたい
        self.next_pointer()

    def next_pointer(self):
        self.__pointer = (self.__pointer+1) % Brainfuck.memory_size()
        self.__program += '>'

    def prev_pointer(self):
        self.__pointer = (self.__pointer-1) % Brainfuck.memory_size()
        self.__program += '<'

    def increment_memory(self):
        self.__program += '+'

    def decrement_memory(self):
        self.__program += '-'

    def read(self):
        self.__program += ','

    def write(self):
        self.__program += '.'

    def move_pointer(self, to: int):
        to %= Brainfuck.memory_size()

        if self.__pointer < to:
            while self.__pointer < to:
                self.increment_memory()
        elif to < self.__pointer:
            while to < self.__pointer:
                self.decrement_memory()

    def zero(self, address: int):
        '''0 -> [address]'''
        self.move_pointer(address)

        self.__program += '['
        self.decrement_memory()
        self.__program += ']'

    def add(self, adr1: int, adr2: int):
        '''
        [adr1] + [adr2] -> [adr2]
        0 -> [adr1]
        '''
        self.move_pointer(adr1)

        self.__program += '['

        self.move_pointer(adr2)
        self.increment_memory()

        self.move_pointer(adr1)
        self.decrement_memory()

        self.__program += ']'

    def copy(self, adr1: int, adr2: int):
        '''[adr1] -> [adr2]'''
        self.zero(0)

        self.move_pointer(adr1)

        # [adr1] -> [adr2], [0]
        self.__program += '['

        self.move_pointer(adr2)
        self.increment_memory()

        self.move_pointer(0)
        self.increment_memory()

        self.move_pointer(adr1)
        self.decrement_memory()

        self.__program += ']'

        # [0] -> [adr1]
        self.add(0, adr1)

    @staticmethod
    def memory_size()->int:
        return 1024

    @staticmethod
    def max_value()->int:
        return 127

    @staticmethod
    def min_value()->int:
        return -128
