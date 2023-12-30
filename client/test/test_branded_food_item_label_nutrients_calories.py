# coding: utf-8

"""
    Food Data Central API

    The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.   To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on [Data Type Documentation](https://fdc.nal.usda.gov/data-documentation.html). This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.      Additional details about the API including rate limits, access, and licensing are available on the [FDC website](https://fdc.nal.usda.gov/api-guide.html)

    The version of the OpenAPI document: 1.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.branded_food_item_label_nutrients_calories import BrandedFoodItemLabelNutrientsCalories

class TestBrandedFoodItemLabelNutrientsCalories(unittest.TestCase):
    """BrandedFoodItemLabelNutrientsCalories unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandedFoodItemLabelNutrientsCalories:
        """Test BrandedFoodItemLabelNutrientsCalories
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandedFoodItemLabelNutrientsCalories`
        """
        model = BrandedFoodItemLabelNutrientsCalories()
        if include_optional:
            return BrandedFoodItemLabelNutrientsCalories(
                value = 140
            )
        else:
            return BrandedFoodItemLabelNutrientsCalories(
        )
        """

    def testBrandedFoodItemLabelNutrientsCalories(self):
        """Test BrandedFoodItemLabelNutrientsCalories"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
