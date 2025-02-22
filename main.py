from fastapi import FastAPI
from context_manager import CleanText
from scraper import get_text_from_wiki
from models import UserInput
from error_handler import ExceptionErrors
import re 
import json

app = FastAPI()


@app.get("/wiki/{user_input}")
def home(user_input: str):
  text = get_text_from_wiki(user_input)
  with CleanText(text, user_input) as text:
    pass
    
  return f"Hello world"


@app.post("/wiki/")
def user_search(user_text: UserInput):
  lookup_text = user_text.lookup_text
  file = user_text.file_path
  user_text = user_text.user_input
  try:
    with open(file, 'r') as file:
      text = file.read()
  except FileNotFoundError:
    return ExceptionErrors.no_such_file()
  pattern = re.compile(f"[^.]+{lookup_text}[^.]+")
  match = pattern.findall(text)
  user_text_occurences = re.findall(user_text, text)
  length_of_occurences = len(user_text_occurences)
  if length_of_occurences == 0:
    return ExceptionErrors.no_occurences()
  return {"user_text": user_text,
                     "Occurences": length_of_occurences,
                     "Lookup_text": lookup_text,
                     "Result": len(match)}

