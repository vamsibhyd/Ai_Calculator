from fastapi import APIRouter, HTTPException
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    try:
        # Validate image data
        if not data.image or not data.image.startswith('data:image/'):
            raise HTTPException(status_code=400, detail="Invalid image format")

        # Decode base64 image
        try:
            image_data = base64.b64decode(data.image.split(",")[1])
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to decode image: {str(e)}")

        # Process image
        try:
            image_bytes = BytesIO(image_data)
            image = Image.open(image_bytes)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Failed to process image: {str(e)}")

        # Analyze image and get responses
        try:
            responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
            if not responses:
                return {
                    "message": "No results found",
                    "data": [],
                    "status": "success"
                }
            
            return {
                "message": "Image processed successfully",
                "data": responses,
                "status": "success"
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to analyze image: {str(e)}")

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
