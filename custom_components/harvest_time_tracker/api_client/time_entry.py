class TimeEntry:
  id: str
  client_name: str
  project_name: str
  task_name: str
  hours: float
  start: str
  end: str
  notes: str

  def __init__(self,
               id: str,
               client_name: str,
               project_name: str,
               task_name: str,
               hours: float,
               start: str,
               end: str,
               notes: str
  ):
    self.id = id
    self.client_name = client_name
    self.project_name = project_name
    self.task_name = task_name
    self.hours = hours
    self.start = start
    self.end = end
    self.notes = notes