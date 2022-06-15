from cuishell import *
from parsing import parse_object
from exceptions import (
    BadCompoundException, 
    BaseChemicalException,
    ElementNotFoundException
)
from element import activity_row
from reactions import reactcore
from MendeleevTable import from_label
from toolkit import soulbility_table


class StartScene(Scene):
    def main(self):
        conseq_choice([
            ('Химический калькулятор', app['calculator']),
            ('Справочные материалы', app['info']),
            ('О приложении', app['about']),
            ('Выход', exit)
        ])


class AboutScene(Scene):
    def main(self):
        alert('Чё нибудь про нас')


class CalculatorScene(Scene):
    def main(self):
        while True:
            expr = prompt('Введите выражение')

            if not strweight(expr):
                return False
            
            objects = expr.replace(' ', '').split('+')
            if len(objects) != 2:
                alert('Ошибка!')
                continue
            try:
                objects = [
                    parse_object(obj) for obj in objects
                ]
                result = reactcore.construct(*objects, ion=True)
                if result == None:
                    alert('Данная реакция не идёт!')
                    continue
                mol_result, ion_result = result
                print('Реакция успешно прошла!')
                print('Молекулярное уравнение:')
                print(mol_result)
                print('Полное ионное уравнение:')
                print(ion_result)
                print('Краткое ионное уравнение:')
                print(ion_result.to_str(True))
                delay()
            except BadCompoundException:
                alert('Ошибка элемента/соединения')
            except BaseChemicalException:
                alert('Неизвестная ошибка в формуле')
            except BaseException as e:
                raise e
                alert(f'Ошибка неизвестного характера. Сообщение: {e.args[0]}')


class InfoScene(Scene):
    def main(self):
        ch = choice([
            'Поиск информации про элемент',
            'Таблица растворимостей',
            'Ряд активности металлов',
            'Назад'
        ])
        
        if ch == 0:
            symbol = prompt('Введите символ')
            try:
                element = from_label(symbol)
            except ElementNotFoundException: 
                alert(f'Ошибка! Элемент с символом {symbol} не найден!')
                return
            element.describe()
            input()
        elif ch == 1:
            print(soulbility_table)
            input()
        elif ch == 2:
            print(*activity_row, sep=', ')
            input()
        elif ch == 3:
            return False
            
            


app = App({
    'start': StartScene(title='Главное меню'),
    'about': AboutScene(title='О приложении'),
    'calculator': CalculatorScene(title='Химический калькулятор'),
    'info': InfoScene(title='Справочные материалы')
}, 'chemcad_app')

app('start')
