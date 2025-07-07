import pydantic
import pytest

from checkr_api_py import AsyncClient, Client
from checkr_api_py.environment import Environment
from checkr_api_py.types import models


def test_create_201_success_all_params():
    """Tests a POST request to the /i9/forms_i9 endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.FormI9

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
    response = client.i9.forms_i9.create(
        candidate_id="3de7e278beb24d14a3785e2dd02cca49",
        email="john.doe@example.com",
        start_date="2023-04-29",
        workflow_type="remote_section_1_only",
        worksite_id="8046067e32ad6b25a9078735",
        authorized_representative_email="lee.perry@domain.com",
        authorized_representative_first_name="Lee",
        authorized_representative_last_name="Perry",
    )
    try:
        pydantic.TypeAdapter(models.FormI9).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /i9/forms_i9 endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.FormI9

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
    response = await client.i9.forms_i9.create(
        candidate_id="3de7e278beb24d14a3785e2dd02cca49",
        email="john.doe@example.com",
        start_date="2023-04-29",
        workflow_type="remote_section_1_only",
        worksite_id="8046067e32ad6b25a9078735",
        authorized_representative_email="lee.perry@domain.com",
        authorized_representative_first_name="Lee",
        authorized_representative_last_name="Perry",
    )
    try:
        pydantic.TypeAdapter(models.FormI9).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /i9/forms_i9/{id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.FormI9

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
    response = client.i9.forms_i9.get(id="string")
    try:
        pydantic.TypeAdapter(models.FormI9).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /i9/forms_i9/{id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.FormI9

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
    response = await client.i9.forms_i9.get(id="string")
    try:
        pydantic.TypeAdapter(models.FormI9).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only():
    """Tests a GET request to the /i9/forms_i9 endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.I9FormsI9ListResponse

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
    response = client.i9.forms_i9.list(order="asc", order_by="full_name")
    try:
        pydantic.TypeAdapter(models.I9FormsI9ListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only():
    """Tests a GET request to the /i9/forms_i9 endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.I9FormsI9ListResponse

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
    response = await client.i9.forms_i9.list(order="asc", order_by="full_name")
    try:
        pydantic.TypeAdapter(models.I9FormsI9ListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /i9/forms_i9 endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.I9FormsI9ListResponse

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
    response = client.i9.forms_i9.list(
        order="asc", order_by="full_name", page=123, per_page=123
    )
    try:
        pydantic.TypeAdapter(models.I9FormsI9ListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /i9/forms_i9 endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.I9FormsI9ListResponse

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
    response = await client.i9.forms_i9.list(
        order="asc", order_by="full_name", page=123, per_page=123
    )
    try:
        pydantic.TypeAdapter(models.I9FormsI9ListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
