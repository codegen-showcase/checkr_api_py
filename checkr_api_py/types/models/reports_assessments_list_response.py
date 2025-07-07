import pydantic
import typing
import typing_extensions

from .assessment import Assessment


class ReportsAssessmentsListResponse(pydantic.BaseModel):
    """
    ReportsAssessmentsListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: typing.Optional[int] = pydantic.Field(alias="count", default=None)
    """
    The total number of assessments for the specified Report.
    
    """
    data: typing.Optional[typing.List[Assessment]] = pydantic.Field(
        alias="data", default=None
    )
    object: typing.Optional[typing_extensions.Literal["list"]] = pydantic.Field(
        alias="object", default=None
    )
