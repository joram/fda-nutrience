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

from openapi_client.models.survey_food_item import SurveyFoodItem

class TestSurveyFoodItem(unittest.TestCase):
    """SurveyFoodItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SurveyFoodItem:
        """Test SurveyFoodItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SurveyFoodItem`
        """
        model = SurveyFoodItem()
        if include_optional:
            return SurveyFoodItem(
                fdc_id = 337985,
                datatype = 'Survey (FNDDS)',
                description = 'Beef curry',
                end_date = '12/31/2014',
                food_class = 'Survey',
                food_code = '27116100',
                publication_date = '4/1/2019',
                start_date = '1/1/2013',
                food_attributes = [
                    openapi_client.models.food_attribute.FoodAttribute(
                        id = 25117, 
                        sequence_number = 1, 
                        value = 'Moisture change: -5.0%', 
                        food_attribute_type = openapi_client.models.food_attribute_food_attribute_type.FoodAttribute_FoodAttributeType(
                            id = 1002, 
                            name = 'Adjustments', 
                            description = 'Adjustments made to foods, including moisture and fat changes.', ), )
                    ],
                food_portions = [
                    openapi_client.models.food_portion.FoodPortion(
                        id = 135806, 
                        amount = 1, 
                        data_points = 9, 
                        gram_weight = 91, 
                        min_year_acquired = 2011, 
                        modifier = '10205', 
                        portion_description = '1 cup', 
                        sequence_number = 1, 
                        measure_unit = openapi_client.models.measure_unit.MeasureUnit(
                            id = 999, 
                            abbreviation = 'undetermined', 
                            name = 'undetermined', ), )
                    ],
                input_foods = [
                    openapi_client.models.input_food_survey.InputFoodSurvey(
                        id = 18146, 
                        amount = 1.5, 
                        food_description = 'Spices, curry powder', 
                        ingredient_code = 2015, 
                        ingredient_description = 'Spices, curry powder', 
                        ingredient_weight = 9.45, 
                        portion_code = '21000', 
                        portion_description = '1 tablespoon', 
                        sequence_number = 6, 
                        survey_flag = 0, 
                        unit = 'TB', 
                        input_food = openapi_client.models.survey_food_item.SurveyFoodItem(
                            fdc_id = 337985, 
                            datatype = 'Survey (FNDDS)', 
                            description = 'Beef curry', 
                            end_date = '12/31/2014', 
                            food_class = 'Survey', 
                            food_code = '27116100', 
                            publication_date = '4/1/2019', 
                            start_date = '1/1/2013', 
                            food_attributes = [
                                openapi_client.models.food_attribute.FoodAttribute(
                                    id = 25117, 
                                    sequence_number = 1, 
                                    value = 'Moisture change: -5.0%', 
                                    food_attribute_type = openapi_client.models.food_attribute_food_attribute_type.FoodAttribute_FoodAttributeType(
                                        id = 1002, 
                                        name = 'Adjustments', 
                                        description = 'Adjustments made to foods, including moisture and fat changes.', ), )
                                ], 
                            food_portions = [
                                openapi_client.models.food_portion.FoodPortion(
                                    id = 135806, 
                                    amount = 1, 
                                    data_points = 9, 
                                    gram_weight = 91, 
                                    min_year_acquired = 2011, 
                                    modifier = '10205', 
                                    portion_description = '1 cup', 
                                    sequence_number = 1, 
                                    measure_unit = openapi_client.models.measure_unit.MeasureUnit(
                                        id = 999, 
                                        abbreviation = 'undetermined', 
                                        name = 'undetermined', ), )
                                ], 
                            input_foods = [
                                openapi_client.models.input_food_survey.InputFoodSurvey(
                                    id = 18146, 
                                    amount = 1.5, 
                                    food_description = 'Spices, curry powder', 
                                    ingredient_code = 2015, 
                                    ingredient_description = 'Spices, curry powder', 
                                    ingredient_weight = 9.45, 
                                    portion_code = '21000', 
                                    portion_description = '1 tablespoon', 
                                    sequence_number = 6, 
                                    survey_flag = 0, 
                                    unit = 'TB', 
                                    retention_factor = openapi_client.models.retention_factor.RetentionFactor(
                                        id = 235, 
                                        code = 3460, 
                                        description = 'VEG, ROOTS, ETC, SAUTEED', ), )
                                ], 
                            wweia_food_category = openapi_client.models.wweia_food_category.WweiaFoodCategory(
                                wweia_food_category_code = 3002, 
                                wweia_food_category_description = 'Meat mixed dishes', ), ), 
                        retention_factor = openapi_client.models.retention_factor.RetentionFactor(
                            id = 235, 
                            code = 3460, 
                            description = 'VEG, ROOTS, ETC, SAUTEED', ), )
                    ],
                wweia_food_category = openapi_client.models.wweia_food_category.WweiaFoodCategory(
                    wweia_food_category_code = 3002, 
                    wweia_food_category_description = 'Meat mixed dishes', )
            )
        else:
            return SurveyFoodItem(
                fdc_id = 337985,
                description = 'Beef curry',
        )
        """

    def testSurveyFoodItem(self):
        """Test SurveyFoodItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
