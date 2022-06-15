'''import sys

import main2

sys.exit(0)'''

from MendeleevTable import *
from MendeleevTable import elements_list
from structures import *
from simple import Simple
from toolkit import *
from hydroxide import Hydroxide
from acid import Acid
from salt import Salt
from reactions import r, IonReactionResult
from oxide import Oxide
from compound import Compound
from ion import Ion
from parsing import parse_object



# Описание элемента Cu
Cu(2).describe()

'''
Элемент Cu
Тип: Металл
Порядковый номер: 29
Расположение(период, группа, подгруппа): (4, 1, 0)
Возможные степени окисления: 0.0, 1.0, 2.0, 3.0, 4.0
Атомная масса: 63.546
Электроотрицательность: 1.9
Простое вещество имеет индекс 2: Нет
'''



# Простое вещество
Simple(H)
# >>> H2
Simple(Cu)
# >>> Cu

# Кислота
Acid(SO4)
# >>> H2SO4

# Оксид
Oxide(Al)
# >>> Al2O3

# Гидроксид
Hydroxide(Fe(3))
# >>> Fe(OH)3

# Соль
Salt(Mg, Cl(-1))
# >>> MgCl2

# Соединение
# (Для создания гидроксогрупп, кислотных остатков...)
c = Compound(S(6), 4 * O(-2))
c.to_str(full=True)
# >>> SO4(2-)




# Первая реакция
a = Hydroxide(Cu)
b = H2SO4

# Молекулярное уравнение
r(a, b)
# >>> Cu(OH)2 + H2SO4 -> CuSO4 + 2H2O

# Вторая реакция
c = Salt(Na, SO3)
d = HBr

mol, ion = r(c, d, ion=True)

# Молекулярное уравнение
mol
# >>> Na2SO3 + 2HBr -> 2NaBr + H2SO3

# Полное ионное
ion
# >>> 2Na(+) + SO3(2-) + 2H(+) + 2Br(-) -> 2Na(+) + 2Br(-) + H2SO3(0)

# Краткое ионное
ion.to_str(short=True)
# >>> SO3(2-) + 2H(+) -> H2SO3(0)


# Проверка на растворимость
is_soulable(Cu, SO4)
# >>> True

# Парсинг
parse_object('Na2SO3').to_str(full=True)
# >>> Na2SO3(0)

# Парсинг с ошибкой
parse_object('CaCl')
# >>> Error!

