class Task:
  id: str
  project_id: int
  project_name: str
  name: str

  def __init__(self,
               id: str,
               project_id: int,
               project_name: str,
               name: str
  ):
    self.id = id
    self.project_id = project_id
    self.project_name = project_name
    self.name = name

  def to_json(self):
    return {
      "id": self.id,
      "project_id": self.project_id,
      "project_name": self.project_name,
      "name": self.name,
    }