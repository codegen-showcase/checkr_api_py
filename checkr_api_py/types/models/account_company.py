import pydantic
import typing
import typing_extensions


class AccountCompany(pydantic.BaseModel):
    """
    Company details
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    City where company is headquartered.
    """
    dba_name: typing.Optional[str] = pydantic.Field(alias="dba_name", default=None)
    """
    Doing-Business-As name of Company displayed in Checkr emails and branded web pages.
    
    """
    incorporation_state: typing.Optional[str] = pydantic.Field(
        alias="incorporation_state", default=None
    )
    """
    Incorporation state. Format: `ISO 3166-2:US`.
    
    """
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
    """
    Type of incorporation.
    """
    industry: typing.Optional[str] = pydantic.Field(alias="industry", default=None)
    """
    Industry that company operates in, as NAICS code (see https://www.naics.com)
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Registered company name.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    Company phone number.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State where company is headquartered. Format: `ISO 3166-2:US`.
    
    """
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    """
    Street address where company is headquartered.
    """
    tax_id: typing.Optional[str] = pydantic.Field(alias="tax_id", default=None)
    """
    Company Tax ID number.
    """
    website: typing.Optional[str] = pydantic.Field(alias="website", default=None)
    """
    Company's official corporate website.
    """
    zipcode: typing.Optional[str] = pydantic.Field(alias="zipcode", default=None)
    """
    Zipcode where company is headquartered.
    """
