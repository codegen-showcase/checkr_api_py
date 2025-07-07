import pydantic
import typing
import typing_extensions


class AccountsCreateBodyUser(typing_extensions.TypedDict):
    """
    AccountsCreateBodyUser
    """

    email: typing_extensions.NotRequired[str]
    """
    Email of the initial Admin user for the Account.
    """

    full_name: typing_extensions.NotRequired[str]
    """
    Full name of the initial Admin user for the Account.
    """


class _SerializerAccountsCreateBodyUser(pydantic.BaseModel):
    """
    Serializer for AccountsCreateBodyUser handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
