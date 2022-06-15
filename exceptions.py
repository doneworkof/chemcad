class BaseChemicalException(Exception):
  '''Базовый класс химических исключений'''


class ForbiddenOxidstateException(BaseChemicalException):
  '''Неверная степень окисления элемента'''


class ForbiddenChargeException(BaseChemicalException):
  '''Неверный заряд иона'''


class IncorrectNumberException(BaseChemicalException):
    '''Неверный номер элемента'''


class ElementNotFoundException(BaseChemicalException):
    '''Элемент не найден'''


class ForbiddenOperationException(BaseChemicalException):
    '''Запрещённая химическая операция (Ba * Cl, Zn + 5)'''


class BadCompoundException(BaseChemicalException):
    '''Ошибка при преобразовании Compound в другой тип'''


class BadOxideException(BaseChemicalException):
    '''Ошибка при образовании основания или кислоты для оксида другого характера'''

__all__ = [
    'BaseChemicalException',
    'ForbiddenChargeException',
    'IncorrectNumberException',
    'ElementNotFoundException',
    'ForbiddenOperationException',
    'BadCompoundException',
    'BadOxideException'
]