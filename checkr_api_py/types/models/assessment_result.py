import pydantic
import typing
import typing_extensions

from .assessed_object import AssessedObject
from .rule import Rule


class AssessmentResult(pydantic.BaseModel):
    """
    The result of assessing one or more items on the report.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    assessed_objects: typing.Optional[typing.List[AssessedObject]] = pydantic.Field(
        alias="assessed_objects", default=None
    )
    rule: typing.Optional[Rule] = pydantic.Field(alias="rule", default=None)
    """
    Description of the applied Rule, as defined for your account.
    
    """
    value: typing.Optional[
        typing_extensions.Literal["eligible", "escalated", "review"]
    ] = pydantic.Field(alias="value", default=None)
