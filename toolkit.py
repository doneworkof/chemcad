import pandas as pd
from exceptions import BadCompoundException

soulbility_table = pd.read_csv('sbtable.csv', index_col=0)


def gcd(*args):
    border = min(args)
    val = 1
    for i in range(2, border + 1):
        for arg in args:
            if arg % i != 0:
                break
        else:
            val = i
    return val


def lcm(a, b): # А почему не math.lcm? тебе не понять))
    return a * b // gcd(a, b)


def dessolve_objects(arr: list) -> list:
    '''Выполняет диссоциацию объектов списка'''
    result = []
    for obj in arr:
        result += obj.dessolve()
    return result


def int_to_oxidstate(n: int) -> str:
    '''Преобразует число в отформатированную строку с зарядом'''
    if n == 0:
        return '0'
    n_sign = '-' if n < 0 else '+'
    n_abs = abs(n)
    if n_abs == 1:
        return n_sign
    return f'{n_abs}{n_sign}'


def create_coef(main_el1, main_el2) -> tuple:
    fch1 = main_el1.get_full_charge()
    fch2 = main_el2.get_full_charge()
    k = lcm(fch1, fch2)
    c1 = k // fch1
    c2 = k // fch2
    return c1, c2


def count_uppercase(s: str) -> int:
    '''Подсчитывает количество символов в верхнем регистре'''
    return sum([1 for ch in s if ch.isupper()])


def check_compound(comp):
    '''Проверяет объект Compound на корректность'''
    if comp.oxidstate != 0 or len(comp.elements) != 2:
        raise BadCompoundException()


def index_balance(oxidstate1: int, oxidstate2: int) -> tuple:
    '''Уравнивает индексы для 2-х объектов'''
    idx1 = abs(oxidstate2)
    idx2 = oxidstate1
    g = gcd(idx1, idx2)
    return idx1 // g, idx2 // g


def optimized_int(n: int) -> str:
    '''Преобразует число в оптимизированную для формул строку'''
    if n > 1:
        return str(n)
    return ''


def group_to_str(s: str, times: int) -> str:
    if times == 1:
        return s
    else:
        return f'({s}){times}'


def is_soulable(metal, addition) -> bool:
    '''Определяет растворимость соединения'''
    
    metal_label = metal(count=1).to_str(True)
    addit_label = addition(count=1).to_str(True) 
    column = soulbility_table[metal_label]
    
    if addit_label not in column:
        return False
    
    status = column[addit_label]
    
    if status == 'Р':
        return True
    elif status == 'М' and metal_label in ['Ca(2+)', 'Sr(2+)']:
        return True
    else:
        return False


def obj_to_str(obj, full=False) -> str:
    '''Преобразует объект в удобночитаеую строку'''
    if obj.oxidstate == 0 and not full:
        return obj.label
    return f'{obj.label}({int_to_oxidstate(obj.oxidstate)})'

