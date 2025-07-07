import pydantic
import typing
import typing_extensions


class AccountsCreateBodyCompany(typing_extensions.TypedDict):
    """
    AccountsCreateBodyCompany
    """

    city: typing_extensions.NotRequired[str]
    """
    City where company is headquartered.
    """

    dba_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Name of Company displayed in Checkr emails and branded web pages.
    """

    incorporation_state: typing_extensions.NotRequired[typing.Optional[str]]
    """
    State where company is incorporated. Format: `ISO 3166-2:US`.
    
    """

    incorporation_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "association",
            "co-ownership",
            "corporation",
            "joint-venture",
            "limited-partnership",
            "llc",
            "llp",
            "non-profit",
            "partnership",
            "s-corporation",
            "sp",
            "trusteeship",
        ]
    ]
    """
    Type of incorporation.
    """

    industry: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Industry that company operates in. Format: `NAICS 2017 Code`.
    
    """

    phone: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Company phone number.
    """

    state: typing_extensions.NotRequired[str]
    """
    State where company is headquartered. Format: `ISO 3166-2:US`.
    
    """

    street: typing_extensions.NotRequired[str]
    """
    Street address where company is headquartered.
    """

    tax_id: typing_extensions.NotRequired[str]
    """
    Company Tax ID number.
    """

    website: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Company website.
    """

    zipcode: typing_extensions.NotRequired[str]
    """
    Zipcode where company is headquartered.
    """


class _SerializerAccountsCreateBodyCompany(pydantic.BaseModel):
    """
    Serializer for AccountsCreateBodyCompany handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    dba_name: typing.Optional[str] = pydantic.Field(alias="dba_name", default=None)
    incorporation_state: typing.Optional[str] = pydantic.Field(
        alias="incorporation_state", default=None
    )
    incorporation_type: typing.Optional[
        typing_extensions.Literal[
            "association",
            "co-ownership",
            "corporation",
            "joint-venture",
            "limited-partnership",
            "llc",
            "llp",
            "non-profit",
            "partnership",
            "s-corporation",
            "sp",
            "trusteeship",
        ]
    ] = pydantic.Field(alias="incorporation_type", default=None)
    industry: typing.Optional[str] = pydantic.Field(alias="industry", default=None)
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    tax_id: typing.Optional[str] = pydantic.Field(alias="tax_id", default=None)
    website: typing.Optional[str] = pydantic.Field(alias="website", default=None)
    zipcode: typing.Optional[str] = pydantic.Field(alias="zipcode", default=None)
