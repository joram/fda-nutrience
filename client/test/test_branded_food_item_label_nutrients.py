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

from openapi_client.models.branded_food_item_label_nutrients import BrandedFoodItemLabelNutrients

class TestBrandedFoodItemLabelNutrients(unittest.TestCase):
    """BrandedFoodItemLabelNutrients unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandedFoodItemLabelNutrients:
        """Test BrandedFoodItemLabelNutrients
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandedFoodItemLabelNutrients`
        """
        model = BrandedFoodItemLabelNutrients()
        if include_optional:
            return BrandedFoodItemLabelNutrients(
                fat = openapi_client.models.branded_food_item_label_nutrients_fat.BrandedFoodItem_labelNutrients_fat(
                    value = 8.9992, ),
                saturated_fat = openapi_client.models.branded_food_item_label_nutrients_saturated_fat.BrandedFoodItem_labelNutrients_saturatedFat(
                    value = 0.9996, ),
                trans_fat = openapi_client.models.branded_food_item_label_nutrients_trans_fat.BrandedFoodItem_labelNutrients_transFat(
                    value = 0, ),
                cholesterol = openapi_client.models.branded_food_item_label_nutrients_trans_fat.BrandedFoodItem_labelNutrients_transFat(
                    value = 0, ),
                sodium = openapi_client.models.branded_food_item_label_nutrients_trans_fat.BrandedFoodItem_labelNutrients_transFat(
                    value = 0, ),
                carbohydrates = openapi_client.models.branded_food_item_label_nutrients_carbohydrates.BrandedFoodItem_labelNutrients_carbohydrates(
                    value = 12.0008, ),
                fiber = openapi_client.models.branded_food_item_label_nutrients_fiber.BrandedFoodItem_labelNutrients_fiber(
                    value = 1.988, ),
                sugars = openapi_client.models.branded_food_item_label_nutrients_sugars.BrandedFoodItem_labelNutrients_sugars(
                    value = 7.9996, ),
                protein = openapi_client.models.branded_food_item_label_nutrients_protein.BrandedFoodItem_labelNutrients_protein(
                    value = 4.0012, ),
                calcium = openapi_client.models.branded_food_item_label_nutrients_calcium.BrandedFoodItem_labelNutrients_calcium(
                    value = 19.88, ),
                iron = openapi_client.models.branded_food_item_label_nutrients_iron.BrandedFoodItem_labelNutrients_iron(
                    value = 0.7196, ),
                potassium = openapi_client.models.branded_food_item_label_nutrients_potassium.BrandedFoodItem_labelNutrients_potassium(
                    value = 159.88, ),
                calories = openapi_client.models.branded_food_item_label_nutrients_calories.BrandedFoodItem_labelNutrients_calories(
                    value = 140, )
            )
        else:
            return BrandedFoodItemLabelNutrients(
        )
        """

    def testBrandedFoodItemLabelNutrients(self):
        """Test BrandedFoodItemLabelNutrients"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
