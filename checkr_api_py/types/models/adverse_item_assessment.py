import pydantic
import typing
import typing_extensions

from .rule import Rule


class AdverseItemAssessment(pydantic.BaseModel):
    """
    Information about the Assessment of the Adverse Item.

    Included only if Assess is enabled for the account.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    rule: typing.Optional[Rule] = pydantic.Field(alias="rule", default=None)
    """
    Description of the applied Rule, as defined for your account.
    
    """
    value: typing.Optional[
        typing_extensions.Literal["eligible", "escalated", "review"]
    ] = pydantic.Field(alias="value", default=None)
