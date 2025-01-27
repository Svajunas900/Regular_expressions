from pydantic import BaseModel


class UserInput(BaseModel):
  user_input: str
  file_path: str
  lookup_text: str