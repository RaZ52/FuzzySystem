import unittest
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable
from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_system import FuzzySystem


class TestFuzzySystemInput(unittest.TestCase):

    def setUp(self):
        self.fuzzy_system_temp = FuzzyInputVariable('Temp', 0, 40, 100)
        self.fuzzy_system_hum = FuzzyInputVariable('Hum', 20, 100, 100)
        self.fuzzy_system_speed = FuzzyOutputVariable('Speed', 0, 100, 100)
        self.fuzzy_system = FuzzySystem()

    def test_var_input_triangular(self):
        self.assertTrue(self.fuzzy_system_temp.add_triangular('Cold', 10, 10, 25))

    def test_var_input_trapezoidal(self):
        self.assertTrue(self.fuzzy_system_temp.add_trapezoidal('Hot', 10, 20, 30, 40))

    def test_var_output_triangular(self):
        self.assertTrue(self.fuzzy_system_speed.add_triangular('Slow', 0, 0, 50))

    def test_var_output_trapezoidal(self):
        self.assertTrue(self.fuzzy_system_speed.add_trapezoidal('Medium', 20, 40, 60, 80))

    def test_system(self):
        self.fuzzy_system_temp.add_triangular('Cold', 10, 10, 25)
        self.fuzzy_system_hum.add_triangular('Wet', 20, 20, 60)
        self.fuzzy_system_speed.add_triangular('Slow', 0, 0, 50)
        self.fuzzy_system.add_input_variable(self.fuzzy_system_temp)
        self.fuzzy_system.add_input_variable(self.fuzzy_system_hum)
        self.fuzzy_system.add_output_variable(self.fuzzy_system_speed)
        self.fuzzy_system.add_rule(
            {'Temp': 'Cold',
             'Hum': 'Wet'},
            {'Speed': 'Slow'})
        self.assertTrue(self.fuzzy_system.evaluate_output({'Temp': 18, 'Hum': 40}))


if __name__ == "__main__":
    unittest.main()
