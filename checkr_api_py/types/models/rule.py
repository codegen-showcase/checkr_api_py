import pydantic
import typing
import typing_extensions


class Rule(pydantic.BaseModel):
    """
    Description of the applied Rule, as defined for your account.

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The name of the Rule, as defined for your account.
    """
    type_: typing.Optional[
        typing_extensions.Literal[
            "count",
            "custom",
            "default",
            "fairness_and_compliance",
            "lookback_period",
            "undefined",
        ]
    ] = pydantic.Field(alias="type", default=None)
    """
    The type of the Rule.
    """
