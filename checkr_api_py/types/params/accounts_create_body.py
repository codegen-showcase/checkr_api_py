import pydantic
import typing
import typing_extensions

from .accounts_create_body_company import (
    AccountsCreateBodyCompany,
    _SerializerAccountsCreateBodyCompany,
)
from .accounts_create_body_user import (
    AccountsCreateBodyUser,
    _SerializerAccountsCreateBodyUser,
)


class AccountsCreateBody(typing_extensions.TypedDict):
    """
    AccountsCreateBody
    """

    client_id: typing_extensions.Required[str]
    """
    Client credentials provided as part of your Partner Application.
    """

    company: typing_extensions.Required[AccountsCreateBodyCompany]

    default_compliance_city: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Fallback compliance city if candidate location is not provided.
    
    """

    default_compliance_state: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Fallback compliance state if candidate location is not provided. Format: `ISO 3166-2:US`.
    
    """

    name: typing_extensions.Required[str]
    """
    Name of Account displayed in the Dashboard.
    """

    oauth_authorize: typing_extensions.NotRequired[bool]
    """
    Allows skipping of the /oauth/authorize call
    """

    purpose: typing_extensions.Required[
        typing_extensions.Literal["business", "employment", "insurance", "tenant"]
    ]
    """
    Permissible purpose to run background checks. Determines which background checks the Account is credentialed for.
    
    """

    user: typing_extensions.Required[AccountsCreateBodyUser]


class _SerializerAccountsCreateBody(pydantic.BaseModel):
    """
    Serializer for AccountsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    client_id: str = pydantic.Field(
        alias="client_id",
    )
    company: _SerializerAccountsCreateBodyCompany = pydantic.Field(
        alias="company",
    )
    default_compliance_city: typing.Optional[str] = pydantic.Field(
        alias="default_compliance_city", default=None
    )
    default_compliance_state: typing.Optional[str] = pydantic.Field(
        alias="default_compliance_state", default=None
    )
    name: str = pydantic.Field(
        alias="name",
    )
    oauth_authorize: typing.Optional[bool] = pydantic.Field(
        alias="oauth_authorize", default=None
    )
    purpose: typing_extensions.Literal[
        "business", "employment", "insurance", "tenant"
    ] = pydantic.Field(
        alias="purpose",
    )
    user: _SerializerAccountsCreateBodyUser = pydantic.Field(
        alias="user",
    )
