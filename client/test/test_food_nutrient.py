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

from openapi_client.models.food_nutrient import FoodNutrient  # noqa: E501

class TestFoodNutrient(unittest.TestCase):
    """FoodNutrient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FoodNutrient:
        """Test FoodNutrient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FoodNutrient`
        """
        model = FoodNutrient()  # noqa: E501
        if include_optional:
            return FoodNutrient(
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
                        ], )
            )
        else:
            return FoodNutrient(
                id = 167514,
        )
        """

    def testFoodNutrient(self):
        """Test FoodNutrient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
