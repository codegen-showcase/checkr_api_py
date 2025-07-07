import pydantic
import typing
import typing_extensions


class GeosUpdateBody(typing_extensions.TypedDict):
    """
    GeosUpdateBody
    """

    city: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Updates the Geo with the input city.
    """


class _SerializerGeosUpdateBody(pydantic.BaseModel):
    """
    Serializer for GeosUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
