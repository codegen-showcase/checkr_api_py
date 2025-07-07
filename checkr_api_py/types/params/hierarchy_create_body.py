import pydantic
import typing
import typing_extensions

from .hierarchy_node import HierarchyNode, _SerializerHierarchyNode


class HierarchyCreateBody(typing_extensions.TypedDict):
    """
    HierarchyCreateBody
    """

    nodes: typing_extensions.Required[typing.List[HierarchyNode]]


class _SerializerHierarchyCreateBody(pydantic.BaseModel):
    """
    Serializer for HierarchyCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    nodes: typing.List[_SerializerHierarchyNode] = pydantic.Field(
        alias="nodes",
    )
