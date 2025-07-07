import pydantic
import typing
import typing_extensions


class Address(typing_extensions.TypedDict):
    """
    Address
    """

    city: typing_extensions.NotRequired[str]
    """
    City.
    """

    country: typing_extensions.NotRequired[str]
    """
    Country.
    
    Format: `ISO 3166-1 alpha-2`
    
    """

    state: typing_extensions.NotRequired[str]
    """
    State.
    """

    street: typing_extensions.NotRequired[str]
    """
    Street address.
    """

    unit: typing_extensions.NotRequired[str]
    """
    House, building or apartment number.
    """

    zipcode: typing_extensions.NotRequired[str]
    """
    5-digit zip code.
    """


class _SerializerAddress(pydantic.BaseModel):
    """
    Serializer for Address handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    unit: typing.Optional[str] = pydantic.Field(alias="unit", default=None)
    zipcode: typing.Optional[str] = pydantic.Field(alias="zipcode", default=None)
