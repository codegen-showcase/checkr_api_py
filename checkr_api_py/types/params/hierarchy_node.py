import pydantic
import typing
import typing_extensions


class HierarchyNode(typing_extensions.TypedDict):
    """
    HierarchyNode
    """

    custom_id: typing_extensions.Required[str]
    """
    Customer-defined unique ID for the node. Must be unique within your account. <b>Note: </b>Custom IDs may contain only letters, numbers, spaces, hyphens, colons, ampersands, and/or underscores.
    """

    name: typing_extensions.Required[str]
    """
    The name for the node. This name will be displayed in the Checkr Dashboard.
    """

    packages: typing_extensions.NotRequired[typing.List[str]]
    """
    List of slugs for packages that are visible to this node (through either direct assignment to the node, or assignment to one of the node's ancestors). Only provided if "include=packages" is included in the query.
    """

    parent_custom_id: typing_extensions.NotRequired[str]
    """
    The `custom_id` for the parent of this node. If not provided, this node will be placed at the top level of the hierarchy. <b>Note: </b>If provided, this node must be a valid and previously loaded `custom_id`, and may contain only letters, numbers, spaces, hyphens, colons, ampersands, and/or underscores.
    """

    tier: typing_extensions.NotRequired[str]
    """
    Customer-defined label for this level of the hierarchy. (For example "Department" or "Division".)
    """


class _SerializerHierarchyNode(pydantic.BaseModel):
    """
    Serializer for HierarchyNode handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_id: str = pydantic.Field(
        alias="custom_id",
    )
    name: str = pydantic.Field(
        alias="name",
    )
    packages: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="packages", default=None
    )
    parent_custom_id: typing.Optional[str] = pydantic.Field(
        alias="parent_custom_id", default=None
    )
    tier: typing.Optional[str] = pydantic.Field(alias="tier", default=None)
