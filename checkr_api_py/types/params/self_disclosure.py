import pydantic
import typing
import typing_extensions

from .self_disclosure_location import (
    SelfDisclosureLocation,
    _SerializerSelfDisclosureLocation,
)


class SelfDisclosure(typing_extensions.TypedDict):
    """
    SelfDisclosure
    """

    date: typing_extensions.Required[str]
    """
    Date of the conviction.
    """

    description: typing_extensions.Required[str]
    """
    Candidate-provided description of their criminal history.
    """

    location: typing_extensions.Required[SelfDisclosureLocation]
    """
    The location of the incident.
    """

    offense_category: typing_extensions.NotRequired[str]
    """
    The criminal charge
    """

    offense_level: typing_extensions.NotRequired[str]
    """
    The level of the offense.
    """

    sentence: typing_extensions.NotRequired[str]
    """
    The sentence imposed.
    """

    time_served: typing_extensions.NotRequired[str]
    """
    The time served.
    """


class _SerializerSelfDisclosure(pydantic.BaseModel):
    """
    Serializer for SelfDisclosure handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    date: str = pydantic.Field(
        alias="date",
    )
    description: str = pydantic.Field(
        alias="description",
    )
    location: _SerializerSelfDisclosureLocation = pydantic.Field(
        alias="location",
    )
    offense_category: typing.Optional[str] = pydantic.Field(
        alias="offense_category", default=None
    )
    offense_level: typing.Optional[str] = pydantic.Field(
        alias="offense_level", default=None
    )
    sentence: typing.Optional[str] = pydantic.Field(alias="sentence", default=None)
    time_served: typing.Optional[str] = pydantic.Field(
        alias="time_served", default=None
    )
