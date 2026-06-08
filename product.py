from pydantic import BaseModel, Field , AnyUrl, field_validator , model_validator , computed_field
from typing import Annotated , Literal, Optional,List
from uuid import UUID
from datetime import datetime
class Product(BaseModel):
    id: int
    uuid: Annotated[
        UUID,
        Field(
            description="Unique identifier for the product" ,
            examples=["a1f3c9b2-9d12-4f2c-8c21-91a1c2d9f101"],
        )
    ]
    name: Annotated[
        str,
        Field(
            description="Name of the product",
            examples=["apple iphone 13"],
            min_length=1,
            max_length=50,
        )
    ]
    price :Annotated[
        float,
        Field(
            description="Price of the product",
            examples=[999],
            ge=0,
            le=100000,
        )
    ]
    currency: Literal["INR", "USD"] = "INR"
    brand :Annotated[
        str,
        Field(
            description="Brand of the product",
            examples=["apple"],
            min_length=1,
            max_length=50,
        )
    ]
    category:Annotated[
        str,
        Field(
            description="Category of the product",
            examples=["mobile"],
            min_length=1,
            max_length=20,
        )
    ]
    tags:Annotated[
        Optional[List[str]],
        Field(
            default=None,
            description="upto 10 tags",
            max_length=10,
        )
    ]
    image_urls:Annotated[
        List[AnyUrl],
        Field(
            max_length=10,
            description="at least one image url",
        )
    ]
    #dimension_cm
    #seller
    created_at : datetime
    ## to make more strictness of the format in uuid
    @field_validator("uuid", mode="after")
    @classmethod
    def validate_uuid_format(cls, value=str):
        if "-" not in value :
            raise ValueError("UUID format is wrong")
        last=value.strip("-")[-1]
        if not (len(last) ==3 and last.isdigit()):
            raise ValueError("UUID must end with 3 digits sequence -234")
        return value