class Place:
    def __init__(self,name,country,priority,n):
        self.n=n
        self.name=name
        self.country=country
        self.priority=priority
    def mark_place_visited(self,n):
        self.n=n

