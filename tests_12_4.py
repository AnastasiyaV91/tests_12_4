import logging
import unittest                                  # Импортируем библиотеку unittest
from runner import Runner                        # Импортируем из модуля runner класс Runner
from rt_with_exceptions import Runner            # Импортируем из модуля rt_with_exceptions
                                                   # класс Runner

logging.basicConfig(level=logging.INFO,                                 # Настройка логирования
                    filemode="w",
                    filename="runner_tests.log",
                    encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s"
                    )

class RunnerTest(unittest.TestCase):
    is_frozen = False                            # Добавляем значение is_frozen для пропуска тестов
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")   # Декоратор - если is_frozen = False, то
                                                                            # тест выполняется
    def test_walk(self):                         # Создаем метод test_walk
        try:                                     # Оборачиваем код в блок try-except
            run1 = Runner("Test_1", speed=-5)        # Создаем объект run1 класса Runner (из модуля runner)
            i = 1                                    # Объявляем переменную для цикла while
            while i <= 10:                           # Цикл вызывает функцию walk из класса Runner
                                                       # (из модуля runner) 10 раз
                run1.walk()
                i += 1                               # С каждым проходом увеличиваем переменную i на единицу
            self.assertEqual(run1.distance, 50)  # Методом assertEqual сравниваем distance объекта run1
                                                         # со значением 50
            logging.info('"test_walk" выполнен успешно')  # Если тест пройден, сообщение записывается
                                                            # в файл runner_tests.log
        except ValueError as e:  # Если возникает исключение, то записываем информацию в файл runner_tests.log
            logging.warning("Неверная скорость для Runner: %s", e, exc_info=True)
            # exc_info=True - позволяет дополнить полную трессировку в файл runner_tests.log

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор - если is_frozen = False, то
                                                                           # тест выполняется
    def test_run(self):                          # Создаем метод test_run
        try:                                     # Оборачиваем код в блок try-except
            run2 = Runner(name=10, speed="Test_2")         # Создаем объект run2 класса Runner (из модуля runner)
            j = 1                                    # Объявляем переменную j для цикла while
            while j <= 10:                           # Цикл вызывает функцию run из класса Runner (из модуля runner) 10 раз
                run2.run()
                j += 1                               # С каждым проходом увеличиваем переменную j на единицу
            self.assertEqual(run2.distance, 100)   # Методом assertEqual сравниваем distance объекта run2
                                                             # со значением 100
            logging.info('"test_run" выполнен успешно')  # Если тест пройден, сообщение записывается
                                                            # в файл runner_tests.log
        except TypeError as e:  # Если возникает исключение, то записываем информацию в файл runner_tests.log
            logging.warning("Неверный тип данных для объекта Runner: %s", e, exc_info=True)
            # exc_info=True - позволяет дополнить полную трессировку в файл runner_tests.log
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")  # Декоратор - если is_frozen = False, то
                                                                           # тест выполняется
    def test_challenge(self):                    # Создаем метод test_challenge
        run3 = Runner("Test_3")                  # Создаем объектs run3 класса Runner (из модуля runner)
        run4 = Runner("Test_3")                  # Создаем объектs run4 класса Runner (из модуля runner)
        l = 1                                    # Объявляем переменную l для цикла while
        while l <= 10:                           # Цикл вызывает функцию run из класса Runner (из модуля runner) 10 раз
            run3.run()
            run4.walk()
            l += 1                               # С каждым проходом увеличиваем переменную l на единицу
        self.assertNotEqual(run3.distance, run4.distance)  # Методом assertNotEqual сравниваем distance объектов run3 и
                                                           # run4, и убеждаемся в их неравенстве

if __name__ == "__main__":                       # Для запуска используем юнит-тест "main"
    unittest.main()