import os

class TestContext:
  api_key: str
  account_id: str

  def __init__(self, api_key: str, account_id: str):
    self.api_key = api_key
    self.account_id = account_id

def get_test_context() -> TestContext:
  api_key = os.environ["API_KEY"]
  if (api_key is None):
      raise Exception("API_KEY must be set")
  
  account_id = os.environ["ACCOUNT_ID"]
  if (account_id is None):
      raise Exception("ACCOUNT_ID must be set")

  return TestContext(api_key, account_id)