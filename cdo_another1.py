def nonconformant_eq_operator():
    a = ''
    if a == None:
        print("a eq None")

def conformant_eq_operator():
    from sys import intern
    greeting = "It's a beautiful day in the neighbourhood."
    a = intern(greeting)
    b = intern(greeting)
    if a == b:
        return True

def nonconformant_is_operator():
    a = [1, 2, 3]
    b = a.copy()
    if a is b :
        return True

def conformant_is_operator():
    from sys import intern
    greeting = "It's a beautiful day in the neighbourhood."
    a = intern(greeting)
    if a is None:
        return True

MY_CONSTANT = 'foo'
def conformant_is_operator2(const):
    if const is MY_CONSTANT:
        return True

def nonconformant_noteq_operator():
    a = "Thisisstring"
    if a != None:
        print(True)

def conformant_noteq_operator():
    a = "Thisisstring"
    b = "This is string"
    if a != b:
        print(True)

def nonconformant_isnot_operator():
    a = [1, 2, 3]
    b = a.copy()
    if a is not b :
        return True

def conformant_isnot_operator():
    a = "Thisisstring"
    if a is not None:
        print(True)

a = "Thisisstring"
def conformant_isnot_operator2(const):
    if const is not a:
        print(True)

## Added against false positive detected at :
## https://github.com/biopython/biopython/blob/92c07ce7dce91078edc9b77fb71dbbe5646565bb/Bio/SearchIO/BlatIO.py#L601
def conformant_is_operator_2():
    a = None
    if a is None:
        print("a eq None")


def conformant_compare_strings():
    return should_open_window = event["start"] == "True"


import enum
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3

def conformant_enum():
    print (Animal.dog is Animal.dog)


class Operator(OperatorBase):
    """
    Abstract.
    """
    def __init__(self, *operands: [OperatorBase, DataCallable]):
        self.operands = operands

    def __call__(self, data: dict) -> bool:
        raise MethodOverrideRequired(self.__class__, "__call__")

    def __eq__(self, other):
        if type(self) is type(other):
            if set(self.operands) == set(other.operands):
                return True
        return False

    def serialize(self):
        return {self.__class__.__name__: [o.serialize() for o in self.operands]}


def non_conformant_with_assignment_operator():
    firstElement = True

    for item in glExtensions :
        if firstElement == True :
            f.write("        : m_%s(false)\n" % item)
            firstElement = False
        else :
            f.write("        , m_%s(false)\n" % item)
