import pydantic
import typing
import typing_extensions


class I9WorksitesUpdateBody(typing_extensions.TypedDict):
    """
    I9WorksitesUpdateBody
    """

    city: typing_extensions.NotRequired[str]
    """
    City of Worksite.
    """

    name: typing_extensions.NotRequired[str]
    """
    Worksite name.
    """

    state: typing_extensions.NotRequired[str]
    """
    State of Worksite.
    """

    street_line1: typing_extensions.NotRequired[str]
    """
    Line one of Worksite address.
    """

    street_line2: typing_extensions.NotRequired[str]
    """
    Line two of Worksite address.
    """

    zip_code: typing_extensions.NotRequired[str]
    """
    ZIP Code of Worksite.
    """

    everify_status: typing_extensions.NotRequired[
        typing_extensions.Literal["active", "inactive"]
    ]
    """
    Worksite E-Verify Status.
    """


class _SerializerI9WorksitesUpdateBody(pydantic.BaseModel):
    """
    Serializer for I9WorksitesUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street_line1: typing.Optional[str] = pydantic.Field(
        alias="street_line1", default=None
    )
    street_line2: typing.Optional[str] = pydantic.Field(
        alias="street_line2", default=None
    )
    zip_code: typing.Optional[str] = pydantic.Field(alias="zip_code", default=None)
    everify_status: typing.Optional[typing_extensions.Literal["active", "inactive"]] = (
        pydantic.Field(alias="everify_status", default=None)
    )
