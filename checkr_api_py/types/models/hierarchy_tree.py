import pydantic
import typing


class HierarchyTree(pydantic.BaseModel):
    """
    HierarchyTree
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    children: typing.Optional[typing.List["HierarchyTree"]] = pydantic.Field(
        alias="children", default=None
    )
    """
    List of child hierarchy trees with name, custom_id, tier and their children
    """
    custom_id: str = pydantic.Field(
        alias="custom_id",
    )
    """
    Customer-defined unique ID for the node. Must be unique within your account.
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name for the node. This name will be displayed in the Checkr Dashboard.
    """
    tier: typing.Optional[str] = pydantic.Field(alias="tier", default=None)
    """
    Customer-defined label for this level of the hierarchy. (For example "Department" or "Division")
    """
