import pydantic
import typing
import typing_extensions


class WorkLocation(typing_extensions.TypedDict):
    """
    WorkLocation
    """

    city: typing_extensions.NotRequired[str]
    """
    Name of the city
    """

    country: typing_extensions.NotRequired[str]
    """
    The country in ISO-3166 alpha-2 format.
    """

    state: typing_extensions.Required[str]
    """
    The two letter state code.
    """


class _SerializerWorkLocation(pydantic.BaseModel):
    """
    Serializer for WorkLocation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    state: str = pydantic.Field(
        alias="state",
    )
