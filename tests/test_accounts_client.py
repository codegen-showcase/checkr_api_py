import pydantic
import pytest

from checkr_api_py import AsyncClient, Client
from checkr_api_py.environment import Environment
from checkr_api_py.types import models


def test_create_201_success_all_params():
    """Tests a POST request to the /accounts endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Account

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
    response = client.accounts.create(
        client_id="56269e3411a549fd07ed8d92",
        company={
            "city": "San Francisco",
            "dba_name": "Acme",
            "incorporation_state": "CA",
            "incorporation_type": "association",
            "industry": "72",
            "phone": "206-555-0100",
            "state": "CA",
            "street": "123 Main Street",
            "tax_id": "123456789",
            "website": "https://www.example.com",
            "zipcode": "94107",
        },
        name="Acme Corporation",
        purpose="employment",
        user={"email": "user@example.com", "full_name": "Jeanette Hughes"},
        default_compliance_city="San Francisco",
        default_compliance_state="CA",
        oauth_authorize=True,
    )
    try:
        pydantic.TypeAdapter(models.Account).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /accounts endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Account

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
    response = await client.accounts.create(
        client_id="56269e3411a549fd07ed8d92",
        company={
            "city": "San Francisco",
            "dba_name": "Acme",
            "incorporation_state": "CA",
            "incorporation_type": "association",
            "industry": "72",
            "phone": "206-555-0100",
            "state": "CA",
            "street": "123 Main Street",
            "tax_id": "123456789",
            "website": "https://www.example.com",
            "zipcode": "94107",
        },
        name="Acme Corporation",
        purpose="employment",
        user={"email": "user@example.com", "full_name": "Jeanette Hughes"},
        default_compliance_city="San Francisco",
        default_compliance_state="CA",
        oauth_authorize=True,
    )
    try:
        pydantic.TypeAdapter(models.Account).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
