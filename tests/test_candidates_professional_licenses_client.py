import pydantic
import pytest

from checkr_api_py import AsyncClient, Client
from checkr_api_py.environment import Environment
from checkr_api_py.types import models


def test_create_200_success_all_params():
    """Tests a POST request to the /candidates/{candidate_id}/professional_licenses endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.ProfessionalLicense

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
    response = client.candidates.professional_licenses.create(
        candidate_id="string",
        data={
            "expiration_date": "2033-01-30",
            "id": "e44aa283528e6fde7d542194",
            "issuer_name": "Medical Board of California",
            "issuer_region": "CA",
            "license_number": "A 12345",
            "license_type": "Physician",
            "certification_document_id": "string",
        },
    )
    try:
        pydantic.TypeAdapter(models.ProfessionalLicense).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /candidates/{candidate_id}/professional_licenses endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.ProfessionalLicense

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
    response = await client.candidates.professional_licenses.create(
        candidate_id="string",
        data={
            "expiration_date": "2033-01-30",
            "id": "e44aa283528e6fde7d542194",
            "issuer_name": "Medical Board of California",
            "issuer_region": "CA",
            "license_number": "A 12345",
            "license_type": "Physician",
            "certification_document_id": "string",
        },
    )
    try:
        pydantic.TypeAdapter(models.ProfessionalLicense).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /candidates/{candidate_id}/professional_licenses endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CandidatesProfessionalLicensesListResponse

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
    response = client.candidates.professional_licenses.list(candidate_id="string")
    try:
        pydantic.TypeAdapter(
            models.CandidatesProfessionalLicensesListResponse
        ).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /candidates/{candidate_id}/professional_licenses endpoint.

    Operation: list
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CandidatesProfessionalLicensesListResponse

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
    response = await client.candidates.professional_licenses.list(candidate_id="string")
    try:
        pydantic.TypeAdapter(
            models.CandidatesProfessionalLicensesListResponse
        ).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_200_success_all_params():
    """Tests a DELETE request to the /candidates/{candidate_id}/professional_licenses/{license_id} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.CandidatesProfessionalLicensesDeleteResponse

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
    response = client.candidates.professional_licenses.delete(
        candidate_id="string", license_id="string"
    )
    try:
        pydantic.TypeAdapter(
            models.CandidatesProfessionalLicensesDeleteResponse
        ).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_delete_200_success_all_params():
    """Tests a DELETE request to the /candidates/{candidate_id}/professional_licenses/{license_id} endpoint.

    Operation: delete
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.CandidatesProfessionalLicensesDeleteResponse

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
    response = await client.candidates.professional_licenses.delete(
        candidate_id="string", license_id="string"
    )
    try:
        pydantic.TypeAdapter(
            models.CandidatesProfessionalLicensesDeleteResponse
        ).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
