# swagger-client
Interage com o registration server (eureka) para registar esta instância ou obter servidores com o qual pode comunicar

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EndpointsApi(swagger_client.ApiClient(configuration))
service = 'service_example' # str | Service name

try:
    # Obtém o melhor endpoint para o serviço {service}
    api_response = api_instance.get_service_endpoint(service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_service_endpoint: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:1906/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EndpointsApi* | [**get_service_endpoint**](docs/EndpointsApi.md#get_service_endpoint) | **GET** /services/{service}/endpoint | Obtém o melhor endpoint para o serviço {service}
*EndpointsApi* | [**get_service_endpoints**](docs/EndpointsApi.md#get_service_endpoints) | **GET** /services/{service}/endpoints | Obtém todos os endpoints registados em nome do serviço {service}
*EndpointsApi* | [**register_endpoint**](docs/EndpointsApi.md#register_endpoint) | **POST** /register | Regista o endpoint no servidor eureka


## Documentation For Models

 - [Endpoint](docs/Endpoint.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



