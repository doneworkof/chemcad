from MendeleevTable import *
from compound import Compound
from structures import *
from toolkit import count_uppercase
from salt import Salt
from hydroxide import Hydroxide
from acid import Acid
from oxide import Oxide
from simple import Simple
from exceptions import BadCompoundException
import re


def parse_child(el):
    match = re.search(r'\d', el)
    if match == None:
        return from_label(el)
    first_num_idx = match.span()[0]
    label = el[:first_num_idx]
    count = int(el[first_num_idx:])
    return from_label(label) * count


def parse_residue(residue):
    if '(' in residue:
        match = re.search(r'(?<=\))\d', residue)
        count_start_idx = match.span()[0]
        label = residue[1:count_start_idx - 1]
        count = int(residue[count_start_idx:])
        return get_residue_by_label(label) * count
    elif count_uppercase(residue) == 1:
        el = parse_child(residue)
        return get_residue_by_label(el.label) * el.count
    else:
        return get_residue_by_label(residue)

def parse_object(s):
    match = re.search(r'^\d*(?=[A-Z])', s)
    obj_start_idx = match.span()[1]
    count = 1 if obj_start_idx == 0 else int(s[:obj_start_idx])
    obj = s[obj_start_idx:]

    if obj in ['H2O', 'HOH']:
        return H2O * count
    elif count_uppercase(obj) == 1: 
        el = parse_child(obj)
        if el.count != 2 and el.is_paired_simple:
            raise BadCompoundException('This element must have index 2')
        elif el.count != 1 and not el.is_paired_simple:
            raise BadCompoundException('This element must have index 1')
        return Simple(el) * count

    if '(' in obj:
        match = re.search(r'\(', obj)
    else:
        match = re.search(r'(?<=[0-9a-zA-Z])[A-Z]', obj)
    residue_start_idx = match.span()[0]
    main_str = obj[:residue_start_idx]
    residue_str = obj[residue_start_idx:]

    main = parse_child(main_str)
    residue = parse_residue(residue_str)

    required_charge = -residue.get_full_charge()
    if required_charge % main.count != 0:
        raise BadCompoundException()
    main_oxidstate = required_charge // main.count
    main = main(main_oxidstate)

    # Преобразование в Compound с целью контроля
    # Корректности написанного пользователем соединения.
    # Соединения с зарядом != 0 методы from_compound
    # Не пропустят.
    
    comp = Compound(main, residue)
    
    if residue.label == 'O':
        parsed = Oxide.from_compound(comp)
    elif residue.label == 'OH':
        parsed = Hydroxide.from_compound(comp)
    elif main.label == 'H':
        parsed = Acid.from_compound(comp)
    else:
        parsed = Salt.from_compound(comp)

    return parsed * count
