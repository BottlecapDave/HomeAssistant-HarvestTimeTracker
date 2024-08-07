from datetime import datetime

class TimeEntry:
  def __init__(self,
               id: str,
               client_id: int,
               client_name: str,
               project_id: int,
               project_name: str,
               task_id: int,
               task_name: str,
               hours: float,
               start: datetime,
               end: datetime,
               notes: str,
               user_id: str
  ):
    self.id = id
    self.client_id = client_id
    self.client_name = client_name
    self.project_id = project_id
    self.project_name = project_name
    self.task_id = task_id
    self.task_name = task_name
    self.hours = hours
    self.start = start
    self.end = end
    self.notes = notes
    self.user_id = user_id

  def to_json(self):
    return {
      "id": self.id,
      "client_id": self.client_id,
      "client_name": self.client_name,
      "project_id": self.project_id,
      "project_name": self.project_name,
      "task_id": self.task_id,
      "task_name": self.task_name,
      "hours": self.hours,
      "start": self.start,
      "end": self.end,
      "notes": self.notes,
    }