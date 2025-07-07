import pydantic
import pytest

from checkr_api_py import AsyncClient, Client
from checkr_api_py.environment import Environment
from checkr_api_py.types import models


def test_create_200_success_all_params():
    """Tests a POST request to the /reports/{report_id}/adverse_actions endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.AdverseAction

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
    response = client.reports.adverse_actions.create(
        adverse_item_ids=["string"],
        report_id="string",
        medium={
            "email": {"priority": 1.0, "required": True},
            "postal": {"priority": 0.0, "required": False},
        },
        post_notice_scheduled_at="2016-10-07T12:34:00Z",
    )
    try:
        pydantic.TypeAdapter(models.AdverseAction).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /reports/{report_id}/adverse_actions endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.AdverseAction

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
    response = await client.reports.adverse_actions.create(
        adverse_item_ids=["string"],
        report_id="string",
        medium={
            "email": {"priority": 1.0, "required": True},
            "postal": {"priority": 0.0, "required": False},
        },
        post_notice_scheduled_at="2016-10-07T12:34:00Z",
    )
    try:
        pydantic.TypeAdapter(models.AdverseAction).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
