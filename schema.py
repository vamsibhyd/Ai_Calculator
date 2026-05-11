from pydantic import BaseModel, Field
from typing import Dict, Any

class ImageData(BaseModel):
    """
    Schema for image data and variables.
    
    Attributes:
        image (str): Base64 encoded image string
        dict_of_vars (Dict[str, Any]): Dictionary of variables and their values
    """
    image: str = Field(..., description="Base64 encoded image string")
    dict_of_vars: Dict[str, Any] = Field(default_factory=dict, description="Dictionary of variables and their values")
    
    class Config:
        json_schema_extra = {
            "example": {
                "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
                "dict_of_vars": {"x": 5, "y": 10}
            }
        }
