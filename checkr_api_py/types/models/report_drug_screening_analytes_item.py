import pydantic
import typing
import typing_extensions


class ReportDrugScreeningAnalytesItem(pydantic.BaseModel):
    """
    ReportDrugScreeningAnalytesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disposition: typing.Optional[typing_extensions.Literal["negative", "positive"]] = (
        pydantic.Field(alias="disposition", default=None)
    )
    """
    Medical evaluation for specific drug
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Name of drug that was tested
    """
    specimen_type: typing.Optional[
        typing_extensions.Literal["breath", "saliva", "urine"]
    ] = pydantic.Field(alias="specimen_type", default=None)
    """
    Type of specimen that was tested
    """
