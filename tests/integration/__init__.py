import os

class TestContext:
  def __init__(self, api_key: str, account_id: str, user_id: str):
    self.api_key = api_key
    self.account_id = account_id
    self.user_id = user_id

def get_test_context() -> TestContext:
  api_key = os.environ["API_KEY"]
  if (api_key is None):
      raise Exception("API_KEY must be set")
  
  account_id = os.environ["ACCOUNT_ID"]
  if (account_id is None):
      raise Exception("ACCOUNT_ID must be set")
  
  user_id = os.environ["USER_ID"]
  if (user_id is None):
      raise Exception("USER_ID must be set")

  return TestContext(api_key, account_id, user_id)