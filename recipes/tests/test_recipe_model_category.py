from django.forms import ValidationError
from parameterized import parameterized
from recipes.models import Recipe

from .test_recipe_base import RecipeTestBase

"""Testamos os models que podem mudar o comportamento da aplicação."""


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category Testing'
        )
        return super().setUp()

    def test_recipe_category_str_representation(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_recipe_category_model_name_max_lencth_is_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
