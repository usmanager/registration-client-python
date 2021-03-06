# coding: utf-8

"""
    Registration-client-api

    Interage com o registration server (eureka) para registar esta instância ou obter servidores com o qual pode comunicar  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.endpoints_api import EndpointsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEndpointsApi(unittest.TestCase):
    """EndpointsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.endpoints_api.EndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_service_endpoint(self):
        """Test case for get_service_endpoint

        Obtém o melhor endpoint para o serviço {service}  # noqa: E501
        """
        pass

    def test_get_service_endpoints(self):
        """Test case for get_service_endpoints

        Obtém todos os endpoints registados em nome do serviço {service}  # noqa: E501
        """
        pass

    def test_register_endpoint(self):
        """Test case for register_endpoint

        Regista o endpoint no servidor eureka  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
