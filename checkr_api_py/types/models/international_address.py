import pydantic
import typing


class InternationalAddress(pydantic.BaseModel):
    """
    InternationalAddress
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    City
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Country
    
    Format: `ISO 3166-1 alpha-2`
    
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State or Province abbreviation
    """
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    """
    Street address
    """
    unit: typing.Optional[str] = pydantic.Field(alias="unit", default=None)
    """
    House, building or apartment number.
    """
    zipcode: typing.Optional[str] = pydantic.Field(alias="zipcode", default=None)
    """
    Postal code
    """
