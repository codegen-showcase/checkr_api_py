import pydantic
import pytest

from checkr_api_py import AsyncClient, Client
from checkr_api_py.environment import Environment
from checkr_api_py.types import models


def test_create_200_success_all_params():
    """Tests a POST request to the /candidates/{candidate_id}/postal_address endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CandidatePostalAddress

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
    response = client.candidates.postal_address.create(
        candidate_id="string",
        data={
            "city": "Santa Monica",
            "name": "John Smith",
            "object": "postal_address",
            "state": "CA",
            "street": "123 Main St",
            "street2": "Apt A",
            "zipcode": "90401",
        },
    )
    try:
        pydantic.TypeAdapter(models.CandidatePostalAddress).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /candidates/{candidate_id}/postal_address endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CandidatePostalAddress

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
    response = await client.candidates.postal_address.create(
        candidate_id="string",
        data={
            "city": "Santa Monica",
            "name": "John Smith",
            "object": "postal_address",
            "state": "CA",
            "street": "123 Main St",
            "street2": "Apt A",
            "zipcode": "90401",
        },
    )
    try:
        pydantic.TypeAdapter(models.CandidatePostalAddress).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /candidates/{candidate_id}/postal_address endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CandidatePostalAddress

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
    response = client.candidates.postal_address.list(candidate_id="string")
    try:
        pydantic.TypeAdapter(models.CandidatePostalAddress).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /candidates/{candidate_id}/postal_address endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CandidatePostalAddress

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
    response = await client.candidates.postal_address.list(candidate_id="string")
    try:
        pydantic.TypeAdapter(models.CandidatePostalAddress).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
