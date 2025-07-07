import pydantic
import typing
import typing_extensions

from .assessment_result import AssessmentResult
from .ruleset import Ruleset


class Assessment(pydantic.BaseModel):
    """
    Information about an Assessment of the Report.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Assessment was created.
    
    <b>Note: </b>This timestame is accurate to the millisecond.
    
    """
    results: typing.Optional[typing.List[AssessmentResult]] = pydantic.Field(
        alias="results", default=None
    )
    ruleset: typing.Optional[Ruleset] = pydantic.Field(alias="ruleset", default=None)
    """
    Information about a Ruleset.
    
    """
    value: typing.Optional[
        typing_extensions.Literal["eligible", "escalated", "review"]
    ] = pydantic.Field(alias="value", default=None)
