from fastapi import FastAPI
from context_manager import CleanText
from scraper import get_text_from_wiki
from models import UserInput
from error_handler import ExceptionErrors
import re 

app = FastAPI()


@app.get("/wiki/{user_input}")
def home(user_input: str, user_text: UserInput):
  
  text = get_text_from_wiki(user_input)

  with CleanText(text, user_input) as text:
    print("Finished")
    
  return f"Hello world {user_text}"


@app.post("/wiki/")
def user_search(user_text: UserInput):
  file = user_text.file_path
  user_text = user_text.user_input
  with open(file, 'r') as file:
    text = file.read()
  x = re.findall(user_text, text)
  return f"Hello world {len(x)}"