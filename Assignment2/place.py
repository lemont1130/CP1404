class Place:
    def __init__(self,name,country,priority,status):
        self.name=name
        self.country=country
        self.priority=priority
        self.status=status
    def mark_place_visited(self,status):
        self.status=status

