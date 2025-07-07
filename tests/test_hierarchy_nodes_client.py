import pydantic
import pytest

from checkr_api_py import AsyncClient, Client
from checkr_api_py.environment import Environment


def test_create_201_success_all_params():
    """Tests a POST request to the /hierarchy/nodes endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : str

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
    response = client.hierarchy.nodes.create(
        nodes=[
            {
                "custom_id": "zpy8orej4r614ize",
                "name": "Acme Staffing",
                "packages": ["driver_pro", "tasker_pro"],
                "parent_custom_id": "parent custom id",
                "tier": "department",
            }
        ]
    )
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /hierarchy/nodes endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : str

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
    response = await client.hierarchy.nodes.create(
        nodes=[
            {
                "custom_id": "zpy8orej4r614ize",
                "name": "Acme Staffing",
                "packages": ["driver_pro", "tasker_pro"],
                "parent_custom_id": "parent custom id",
                "tier": "department",
            }
        ]
    )
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
