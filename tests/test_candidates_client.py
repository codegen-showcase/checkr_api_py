import pydantic
import pytest

from checkr_api_py import AsyncClient, Client
from checkr_api_py.environment import Environment
from checkr_api_py.types import models


def test_update_200_success_all_params():
    """Tests a POST request to the /candidates/{id} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Candidate

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
    response = client.candidates.update(
        id_path="string",
        adjudication="engaged",
        copy_requested=True,
        custom_id="string",
        dob="1970-01-22",
        driver_license_number="F2111655",
        driver_license_state="CA",
        email="john.smith@gmail.com",
        first_name="John",
        geo_ids=["79f943e212cce7de21c054a8"],
        id="e44aa283528e6fde7d542194",
        last_name="Smith",
        metadata={},
        middle_name="Alfred",
        mother_maiden_name="Jones",
        no_middle_name=True,
        object="candidate",
        phone="5555555555",
        postal_address={
            "city": "San Francisco",
            "name": "John Alfred Smith",
            "state": "CA",
            "street": "123 Main Street",
            "street2": "APT A",
            "zipcode": "94108",
        },
        previous_driver_license_number="F1501739",
        previous_driver_license_state="MD",
        report_ids=["532e71cfe88a1d4e8d00000d"],
        ssn="XXX-XX-4645",
        uri="/v1/candidates/e44aa283528e6fde7d542194",
        zipcode="90401",
    )
    try:
        pydantic.TypeAdapter(models.Candidate).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_200_success_all_params():
    """Tests a POST request to the /candidates/{id} endpoint.

    Operation: update
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Candidate

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
    response = await client.candidates.update(
        id_path="string",
        adjudication="engaged",
        copy_requested=True,
        custom_id="string",
        dob="1970-01-22",
        driver_license_number="F2111655",
        driver_license_state="CA",
        email="john.smith@gmail.com",
        first_name="John",
        geo_ids=["79f943e212cce7de21c054a8"],
        id="e44aa283528e6fde7d542194",
        last_name="Smith",
        metadata={},
        middle_name="Alfred",
        mother_maiden_name="Jones",
        no_middle_name=True,
        object="candidate",
        phone="5555555555",
        postal_address={
            "city": "San Francisco",
            "name": "John Alfred Smith",
            "state": "CA",
            "street": "123 Main Street",
            "street2": "APT A",
            "zipcode": "94108",
        },
        previous_driver_license_number="F1501739",
        previous_driver_license_state="MD",
        report_ids=["532e71cfe88a1d4e8d00000d"],
        ssn="XXX-XX-4645",
        uri="/v1/candidates/e44aa283528e6fde7d542194",
        zipcode="90401",
    )
    try:
        pydantic.TypeAdapter(models.Candidate).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_201_success_all_params():
    """Tests a POST request to the /candidates endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.Candidate

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
    response = client.candidates.create(
        email="john.smith@gmail.com",
        copy_requested=True,
        custom_id="HRIS-27",
        dob="1970-01-22",
        driver_license_number="F2111655",
        driver_license_state="CA",
        first_name="John",
        geo_ids=["79f943e212cce7de21c054a8"],
        last_name="Smith",
        metadata={},
        middle_name="Alfred",
        mother_maiden_name="Jones",
        no_middle_name=True,
        object="candidate",
        phone="5555555555",
        postal_address={
            "city": "San Francisco",
            "name": "John Alfred Smith",
            "state": "CA",
            "street": "123 Main Street",
            "street2": "APT A",
            "zipcode": "94108",
        },
        previous_driver_license_number="F1501739",
        previous_driver_license_state="MD",
        report_ids=["532e71cfe88a1d4e8d00000d"],
        ssn="XXX-XX-4645",
        work_locations=[{"city": "San Francisco", "country": "US", "state": "CA"}],
        zipcode="90401",
    )
    try:
        pydantic.TypeAdapter(models.Candidate).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_201_success_all_params():
    """Tests a POST request to the /candidates endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.Candidate

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
    response = await client.candidates.create(
        email="john.smith@gmail.com",
        copy_requested=True,
        custom_id="HRIS-27",
        dob="1970-01-22",
        driver_license_number="F2111655",
        driver_license_state="CA",
        first_name="John",
        geo_ids=["79f943e212cce7de21c054a8"],
        last_name="Smith",
        metadata={},
        middle_name="Alfred",
        mother_maiden_name="Jones",
        no_middle_name=True,
        object="candidate",
        phone="5555555555",
        postal_address={
            "city": "San Francisco",
            "name": "John Alfred Smith",
            "state": "CA",
            "street": "123 Main Street",
            "street2": "APT A",
            "zipcode": "94108",
        },
        previous_driver_license_number="F1501739",
        previous_driver_license_state="MD",
        report_ids=["532e71cfe88a1d4e8d00000d"],
        ssn="XXX-XX-4645",
        work_locations=[{"city": "San Francisco", "country": "US", "state": "CA"}],
        zipcode="90401",
    )
    try:
        pydantic.TypeAdapter(models.Candidate).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_required_only():
    """Tests a GET request to the /candidates/{id} endpoint.

    Operation: get
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Candidate

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
    response = client.candidates.get(id="string", include="reports")
    try:
        pydantic.TypeAdapter(models.Candidate).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_required_only():
    """Tests a GET request to the /candidates/{id} endpoint.

    Operation: get
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Candidate

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
    response = await client.candidates.get(id="string", include="reports")
    try:
        pydantic.TypeAdapter(models.Candidate).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_200_success_all_params():
    """Tests a GET request to the /candidates/{id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Candidate

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
    response = client.candidates.get(id="string", include="reports")
    try:
        pydantic.TypeAdapter(models.Candidate).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /candidates/{id} endpoint.

    Operation: get
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Candidate

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
    response = await client.candidates.get(id="string", include="reports")
    try:
        pydantic.TypeAdapter(models.Candidate).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_required_only():
    """Tests a GET request to the /candidates endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CandidatesListResponse

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
    response = client.candidates.list()
    try:
        pydantic.TypeAdapter(models.CandidatesListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only():
    """Tests a GET request to the /candidates endpoint.

    Operation: list
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CandidatesListResponse

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
    response = await client.candidates.list()
    try:
        pydantic.TypeAdapter(models.CandidatesListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /candidates endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CandidatesListResponse

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
    response = client.candidates.list(
        adjudication="string",
        created_after="1970-01-01T00:00:00",
        created_before="1970-01-01T00:00:00",
        custom_id="string",
        driver_license_number="string",
        email="string",
        full_name="string",
        geo_id="string",
        metadata={},
        page=123.45,
        per_page=123.45,
        program_id="string",
        report_adjudicated_after="1970-01-01T00:00:00",
        report_adjudicated_before="1970-01-01T00:00:00",
        report_adjudicator_email="string",
        report_revised_after="1970-01-01T00:00:00",
        report_revised_before="1970-01-01T00:00:00",
    )
    try:
        pydantic.TypeAdapter(models.CandidatesListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /candidates endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CandidatesListResponse

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
    response = await client.candidates.list(
        adjudication="string",
        created_after="1970-01-01T00:00:00",
        created_before="1970-01-01T00:00:00",
        custom_id="string",
        driver_license_number="string",
        email="string",
        full_name="string",
        geo_id="string",
        metadata={},
        page=123.45,
        per_page=123.45,
        program_id="string",
        report_adjudicated_after="1970-01-01T00:00:00",
        report_adjudicated_before="1970-01-01T00:00:00",
        report_adjudicator_email="string",
        report_revised_after="1970-01-01T00:00:00",
        report_revised_before="1970-01-01T00:00:00",
    )
    try:
        pydantic.TypeAdapter(models.CandidatesListResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
