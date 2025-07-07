import pydantic
import typing
import typing_extensions


class SelfDisclosureLocation(typing_extensions.TypedDict):
    """
    The location of the incident.
    """

    country: typing_extensions.NotRequired[str]
    """
    2 letter country code. Format: `ISO 3166-1 alpha-2` (`US` by default.)
    
    """

    county: typing_extensions.Required[str]
    """
    Name of the county in which the conviction occurred. (Use the [/counties](#tag/Counties) resource to obtain a list of counties in each state.)
    
    """

    state: typing_extensions.Required[str]
    """
    State where the county is located. Format: `ISO 3166-2:US`.
    
    """


class _SerializerSelfDisclosureLocation(pydantic.BaseModel):
    """
    Serializer for SelfDisclosureLocation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    county: str = pydantic.Field(
        alias="county",
    )
    state: str = pydantic.Field(
        alias="state",
    )
