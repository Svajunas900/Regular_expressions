import re


def remove_non_ascii(text: str) -> str:
    return re.sub(r'[^\x00-\x7F]', '', text)


class CleanText:
  def __init__(self, text: str, new_text_file: str):
    self.text = text
    self.new_text_file = new_text_file
    self.new_text = None

  def __enter__(self):
    self.new_text = remove_non_ascii(self.text)

  def __exit__(self, exc_type, exc_value, exc_traceback):
    text_file = open(f"{self.new_text_file}_file.txt", "w+")
    text_file.write(self.new_text)
    text_file.close()

