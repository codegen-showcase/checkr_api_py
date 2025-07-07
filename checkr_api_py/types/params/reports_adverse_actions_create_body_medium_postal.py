import pydantic
import typing
import typing_extensions


class ReportsAdverseActionsCreateBodyMediumPostal(typing_extensions.TypedDict):
    """
    The postal medium is used to send an adverse action via physical mail to the candidate.

    """

    priority: typing_extensions.NotRequired[float]
    """
    The priority setting dictates whether the adverse action should be sent through this medium. A priority of 1 means the adverse action will be sent, while a priority of 0 means it will not be sent through this medium.
    """

    required: typing_extensions.NotRequired[bool]
    """
    The "required" setting specifies whether an adverse action must be sent. If set to true, it means the adverse action must be sent through this medium. If set to false, sending the adverse action through this medium is optional.
    """


class _SerializerReportsAdverseActionsCreateBodyMediumPostal(pydantic.BaseModel):
    """
    Serializer for ReportsAdverseActionsCreateBodyMediumPostal handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    priority: typing.Optional[float] = pydantic.Field(alias="priority", default=None)
    required: typing.Optional[bool] = pydantic.Field(alias="required", default=None)
