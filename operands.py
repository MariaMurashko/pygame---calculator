numbers = '0123456789'
operands = {
    '=': 'equals',
    '+': 'plus',
    '-': 'minus',
    '%': 'percent',
    '÷': 'digit',
    'x': 'x',
}
methods = {
    ',': 'add_comma',
    'AC': 'resent',
    '=/-': 'change_sing'
}


def getTypeCommand(text):
    if text in numbers:
        return 'number'
    if text in methods.keys():
        return 'method'
    if text in operands.keys():
        return 'operand'