import pydantic
import pytest

from checkr_api_py import AsyncClient, Client
from checkr_api_py.environment import Environment
from checkr_api_py.types import models


def test_list_200_success_required_only():
    """Tests a GET request to the /counties endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CountiesListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        environment=Environment.MOCK_SERVER,
    )
    response = client.counties.list()
    try:
        pydantic.TypeAdapter(models.CountiesListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only():
    """Tests a GET request to the /counties endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CountiesListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.counties.list()
    try:
        pydantic.TypeAdapter(models.CountiesListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /counties endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CountiesListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(
        username="API_USERNAME",
        password="API_PASSWORD",
        environment=Environment.MOCK_SERVER,
    )
    response = client.counties.list(states="string")
    try:
        pydantic.TypeAdapter(models.CountiesListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /counties endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CountiesListResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(
        username="API_USERNAME",
        password="API_PASSWORD",
        environment=Environment.MOCK_SERVER,
    )
    response = await client.counties.list(states="string")
    try:
        pydantic.TypeAdapter(models.CountiesListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
