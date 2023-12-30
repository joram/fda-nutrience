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

from openapi_client.models.branded_food_item import BrandedFoodItem

class TestBrandedFoodItem(unittest.TestCase):
    """BrandedFoodItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandedFoodItem:
        """Test BrandedFoodItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandedFoodItem`
        """
        model = BrandedFoodItem()
        if include_optional:
            return BrandedFoodItem(
                fdc_id = 534358,
                available_date = '8/18/2018',
                brand_owner = 'Kar Nut Products Company',
                data_source = 'LI',
                data_type = 'Branded',
                description = 'NUT 'N BERRY MIX',
                food_class = 'Branded',
                gtin_upc = '077034085228',
                household_serving_full_text = '1 ONZ',
                ingredients = 'PEANUTS (PEANUTS, PEANUT AND/OR SUNFLOWER OIL). RAISINS. DRIED CRANBERRIES (CRANBERRIES, SUGAR, SUNFLOWER OIL). SUNFLOWER KERNELS AND ALMONDS (SUNFLOWER KERNELS AND ALMONDS, PEANUT AND/OR SUNFLOWER OIL).',
                modified_date = '8/18/2018',
                publication_date = '4/1/2019',
                serving_size = 28,
                serving_size_unit = 'g',
                preparation_state_code = 'UNPREPARED',
                branded_food_category = 'Popcorn, Peanuts, Seeds & Related Snacks',
                trade_channel = ["CHILD_NUTRITION_FOOD_PROGRAMS","GROCERY"],
                gpc_class_code = 50161800,
                food_nutrients = [
                    openapi_client.models.food_nutrient.FoodNutrient(
                        id = 167514, 
                        amount = 0, 
                        data_points = 49, 
                        min = 73.73, 
                        max = 91.8, 
                        median = 90.3, 
                        type = 'FoodNutrient', 
                        nutrient = openapi_client.models.nutrient.Nutrient(
                            id = 1005, 
                            number = '305', 
                            name = 'Carbohydrate, by difference', 
                            rank = 1110, 
                            unit_name = 'g', ), 
                        food_nutrient_derivation = openapi_client.models.food_nutrient_derivation.FoodNutrientDerivation(
                            id = 75, 
                            code = 'LCCD', 
                            description = 'Calculated from a daily value percentage per serving size measure', 
                            food_nutrient_source = openapi_client.models.food_nutrient_source.FoodNutrientSource(
                                id = 9, 
                                code = '12', 
                                description = 'Manufacturer's analytical; partial documentation', ), ), 
                        nutrient_analysis_details = openapi_client.models.nutrient_analysis_details.NutrientAnalysisDetails(
                            sub_sample_id = 343866, 
                            amount = 0, 
                            nutrient_id = 1005, 
                            lab_method_description = '10.2135/cropsci2017.04.0244', 
                            lab_method_original_description = '', 
                            lab_method_link = 'https://doi.org/10.2135/cropsci2017.04.0244', 
                            lab_method_technique = 'DOI for Beans', 
                            nutrient_acquisition_details = [
                                openapi_client.models.nutrient_acquisition_details.NutrientAcquisitionDetails(
                                    sample_unit_id = 321632, 
                                    purchase_date = '12/2/2005', 
                                    store_city = 'TRUSSVILLE', 
                                    store_state = 'AL', )
                                ], ), )
                    ],
                food_update_log = [
                    openapi_client.models.food_update_log.FoodUpdateLog(
                        fdc_id = 534358, 
                        available_date = '8/18/2018', 
                        brand_owner = 'Kar Nut Products Company', 
                        data_source = 'LI', 
                        data_type = 'Branded', 
                        description = 'NUT 'N BERRY MIX', 
                        food_class = 'Branded', 
                        gtin_upc = '077034085228', 
                        household_serving_full_text = '1 ONZ', 
                        ingredients = 'PEANUTS (PEANUTS, PEANUT AND/OR SUNFLOWER OIL). RAISINS. DRIED CRANBERRIES (CRANBERRIES, SUGAR, SUNFLOWER OIL). SUNFLOWER KERNELS AND ALMONDS (SUNFLOWER KERNELS AND ALMONDS, PEANUT AND/OR SUNFLOWER OIL).', 
                        modified_date = '8/18/2018', 
                        publication_date = '4/1/2019', 
                        serving_size = 28, 
                        serving_size_unit = 'g', 
                        branded_food_category = 'Popcorn, Peanuts, Seeds & Related Snacks', 
                        changes = 'Nutrient Added, Nutrient Updated', 
                        food_attributes = [
                            openapi_client.models.food_attribute.FoodAttribute(
                                id = 25117, 
                                sequence_number = 1, 
                                value = 'Moisture change: -5.0%', 
                                food_attribute_type = openapi_client.models.food_attribute_food_attribute_type.FoodAttribute_FoodAttributeType(
                                    id = 1002, 
                                    name = 'Adjustments', 
                                    description = 'Adjustments made to foods, including moisture and fat changes.', ), )
                            ], )
                    ],
                label_nutrients = openapi_client.models.branded_food_item_label_nutrients.BrandedFoodItem_labelNutrients(
                    fat = openapi_client.models.branded_food_item_label_nutrients_fat.BrandedFoodItem_labelNutrients_fat(
                        value = 8.9992, ), 
                    saturated_fat = openapi_client.models.branded_food_item_label_nutrients_saturated_fat.BrandedFoodItem_labelNutrients_saturatedFat(
                        value = 0.9996, ), 
                    trans_fat = openapi_client.models.branded_food_item_label_nutrients_trans_fat.BrandedFoodItem_labelNutrients_transFat(
                        value = 0, ), 
                    cholesterol = openapi_client.models.branded_food_item_label_nutrients_trans_fat.BrandedFoodItem_labelNutrients_transFat(
                        value = 0, ), 
                    sodium = , 
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
                        value = 140, ), )
            )
        else:
            return BrandedFoodItem(
                fdc_id = 534358,
                data_type = 'Branded',
                description = 'NUT 'N BERRY MIX',
        )
        """

    def testBrandedFoodItem(self):
        """Test BrandedFoodItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()