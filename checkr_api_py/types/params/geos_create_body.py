import pydantic
import typing
import typing_extensions


class GeosCreateBody(typing_extensions.TypedDict):
    """
    GeosCreateBody
    """

    city: typing_extensions.NotRequired[str]
    """
    A major city within the input state.
    """

    name: typing_extensions.Required[str]
    """
    Human-readable name of the Geo.
    """

    state: typing_extensions.Required[str]
    """
    US state for the Geo.
    """


class _SerializerGeosCreateBody(pydantic.BaseModel):
    """
    Serializer for GeosCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    name: str = pydantic.Field(
        alias="name",
    )
    state: str = pydantic.Field(
        alias="state",
    )
