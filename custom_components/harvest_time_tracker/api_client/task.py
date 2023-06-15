class Task:
  id: str
  client_id: int
  client_name: str
  project_id: int
  project_name: str
  name: str

  def __init__(self,
               id: str,
               client_id: int,
               client_name: str,
               project_id: int,
               project_name: str,
               name: str
  ):
    self.id = id
    self.client_id = client_id
    self.client_name = client_name
    self.project_id = project_id
    self.project_name = project_name
    self.name = name

  def to_json(self):
    return {
      "id": self.id,
      "client_id": self.client_id,
      "client_name": self.client_name,
      "project_id": self.project_id,
      "project_name": self.project_name,
      "name": self.name,
    }