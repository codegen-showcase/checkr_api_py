import pydantic
import typing
import typing_extensions


class ReportsUpdateBody(typing_extensions.TypedDict):
    """
    ReportsUpdateBody
    """

    adjudication: typing_extensions.NotRequired[typing_extensions.Literal["engaged"]]

    package: typing_extensions.NotRequired[str]
    """
    Slug of the Package.
    
    """


class _SerializerReportsUpdateBody(pydantic.BaseModel):
    """
    Serializer for ReportsUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    adjudication: typing.Optional[typing_extensions.Literal["engaged"]] = (
        pydantic.Field(alias="adjudication", default=None)
    )
    package: typing.Optional[str] = pydantic.Field(alias="package", default=None)
