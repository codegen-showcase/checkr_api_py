import typing
import typing_extensions

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models, params


class AccountsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        client_id: str,
        company: params.AccountsCreateBodyCompany,
        name: str,
        purpose: typing_extensions.Literal[
            "business", "employment", "insurance", "tenant"
        ],
        user: params.AccountsCreateBodyUser,
        default_compliance_city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_compliance_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oauth_authorize: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Create a new Account

        Creates a customer Account associated with your [Partner Application](#section/Checkr-Partners).
        Only Checkr Partners are authorized to use this endpoint.


        POST /accounts

        Args:
            default_compliance_city: Fallback compliance city if candidate location is not provided.

            default_compliance_state: Fallback compliance state if candidate location is not provided. Format: `ISO 3166-2:US`.

            oauth_authorize: Allows skipping of the /oauth/authorize call
            client_id: Client credentials provided as part of your Partner Application.
            company: AccountsCreateBodyCompany
            name: Name of Account displayed in the Dashboard.
            purpose: Permissible purpose to run background checks. Determines which background checks the Account is credentialed for.

            user: AccountsCreateBodyUser
            request_options: Additional options to customize the HTTP request

        Returns:
            Account details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.accounts.create(
            client_id="56269e3411a549fd07ed8d92",
            company={
                "city": "San Francisco",
                "dba_name": "Acme",
                "incorporation_state": "CA",
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
        )
        ```
        """
        _json = to_encodable(
            item={
                "default_compliance_city": default_compliance_city,
                "default_compliance_state": default_compliance_state,
                "oauth_authorize": oauth_authorize,
                "client_id": client_id,
                "company": company,
                "name": name,
                "purpose": purpose,
                "user": user,
            },
            dump_with=params._SerializerAccountsCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/accounts",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )


class AsyncAccountsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        client_id: str,
        company: params.AccountsCreateBodyCompany,
        name: str,
        purpose: typing_extensions.Literal[
            "business", "employment", "insurance", "tenant"
        ],
        user: params.AccountsCreateBodyUser,
        default_compliance_city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        default_compliance_state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        oauth_authorize: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Account:
        """
        Create a new Account

        Creates a customer Account associated with your [Partner Application](#section/Checkr-Partners).
        Only Checkr Partners are authorized to use this endpoint.


        POST /accounts

        Args:
            default_compliance_city: Fallback compliance city if candidate location is not provided.

            default_compliance_state: Fallback compliance state if candidate location is not provided. Format: `ISO 3166-2:US`.

            oauth_authorize: Allows skipping of the /oauth/authorize call
            client_id: Client credentials provided as part of your Partner Application.
            company: AccountsCreateBodyCompany
            name: Name of Account displayed in the Dashboard.
            purpose: Permissible purpose to run background checks. Determines which background checks the Account is credentialed for.

            user: AccountsCreateBodyUser
            request_options: Additional options to customize the HTTP request

        Returns:
            Account details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.accounts.create(
            client_id="56269e3411a549fd07ed8d92",
            company={
                "city": "San Francisco",
                "dba_name": "Acme",
                "incorporation_state": "CA",
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
        )
        ```
        """
        _json = to_encodable(
            item={
                "default_compliance_city": default_compliance_city,
                "default_compliance_state": default_compliance_state,
                "oauth_authorize": oauth_authorize,
                "client_id": client_id,
                "company": company,
                "name": name,
                "purpose": purpose,
                "user": user,
            },
            dump_with=params._SerializerAccountsCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/accounts",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Account,
            request_options=request_options or default_request_options(),
        )
