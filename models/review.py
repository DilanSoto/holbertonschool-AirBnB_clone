from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review with a place ID, user ID, and text"""
    place_id = ""
    user_id = ""
    text = ""
