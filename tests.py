import requests
from unittest.mock import patch
import unittest


def get_data_from_url(url: str, payload: dict):
  response = requests.post(url=url, json=payload)
  if response.status_code == 200:
    return response.json()
  else:
    return None
  
class TestApiRequests(unittest.TestCase):
  @patch("requests.post")
  def test_request_success(self, mock_post):
    mock_response = mock_post.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
    "user_text": "git",
    "Occurences": 103,
    "Lookup_text": "repository",
    "Result": 26
    }
    url = 'http://127.0.0.1:8000/wiki'
    payload = {
    "user_input": "git",
    "file_path": "git_file.txt",
    "lookup_text": "repository"
    }
    result = get_data_from_url(url=url, payload=payload)
    self.assertEqual(result['user_text'], "git")
    self.assertEqual(result['Occurences'], 103)
    self.assertEqual(result["Result"], 26)
    self.assertEqual(result["Lookup_text"], "repository")
    mock_post.assert_called_once_with(url=url, json=payload)

  @patch("requests.post")
  def test_request_failure(self, mock_post):
    mock_response = mock_post.return_value
    mock_response.status_code = 404
    mock_response.json.return_value = {}
    url = 'http://127.0.0.1:8000/wiki'
    payload = {
    "user_input": "git",
    "file_path": "git_file.txt",
    "lookup_text": "repository"
    }
    result = get_data_from_url(url=url, payload=payload)
    self.assertIsNone(result)
    mock_post.assert_called_once_with(url=url, json=payload)
  
  @patch("requests.post")
  def test_request_failure_no_occurances(self, mock_post):
    mock_response = mock_post.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = "No occurences"
    url = 'http://127.0.0.1:8000/wiki'
    payload = {
    "user_input": "gitasdasd",
    "file_path": "git_file.txt",
    "lookup_text": "repository"
    }
    result = get_data_from_url(url=url, payload=payload)
    self.assertEqual(result, "No occurences")
    mock_post.assert_called_once_with(url=url, json=payload)

  @patch("requests.post")
  def test_request_failure_no_such_a_file(self, mock_post):
    mock_response = mock_post.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = "No such a file"
    url = 'http://127.0.0.1:8000/wiki'
    payload = {
    "user_input": "gitasdasd",
    "file_path": "git_file.txt",
    "lookup_text": "repository"
    }
    result = get_data_from_url(url=url, payload=payload)
    print(result)
    self.assertEqual(result, "No such a file")
    mock_post.assert_called_once_with(url=url, json=payload)


if __name__ == '__main__':
    unittest.main()