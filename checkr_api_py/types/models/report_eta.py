import pydantic
import typing


class ReportEta(pydantic.BaseModel):
    """
    ReportEta
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    estimate_generated_at: typing.Optional[str] = pydantic.Field(
        alias="estimate_generated_at", default=None
    )
    """
    Time at which the prediction was created.
    
    """
    estimated_completion_time: typing.Optional[str] = pydantic.Field(
        alias="estimated_completion_time", default=None
    )
    """
    Date at which the report is predicted to be finished. Despite the date-time format, we only estimate to the date. The time is not relevant.
    
    """
