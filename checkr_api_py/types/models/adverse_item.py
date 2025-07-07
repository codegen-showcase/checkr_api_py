import pydantic
import typing
import typing_extensions

from .adverse_item_assessment import AdverseItemAssessment


class AdverseItem(pydantic.BaseModel):
    """
    AdverseItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    assessment: typing.Optional[AdverseItemAssessment] = pydantic.Field(
        alias="assessment", default=None
    )
    """
    Information about the Assessment of the Adverse Item.
    
    Included only if Assess is enabled for the account.
    
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    object: typing.Optional[typing_extensions.Literal["adverse_item"]] = pydantic.Field(
        alias="object", default=None
    )
    """
    Defines the object type.
    """
    text: typing.Optional[str] = pydantic.Field(alias="text", default=None)
    """
    Human-readable description of the Adverse Item.
    """
