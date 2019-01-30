from unittest import TestCase

from tasks import add


class TestAdd(TestCase):

    def test_add_with_correct_values(self):
        result = add.delay(1, 3)
        self.assertEqual(4, result.get())

    def test_add_with_incorrect_values_raises_type_error(self):
        self.assertRaises(add.delay("d", "d"))
