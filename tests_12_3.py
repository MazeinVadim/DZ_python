import unittest
from suite_12_3 import RunnerTest, TournamentTest

# Создание объекта TestSuite
test_suite = unittest.TestSuite()

# Добавление тестов RunnerTest и TournamentTest в TestSuite
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Создание объекта TextTestRunner с аргументом verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запуск тестов
runner.run(test_suite)