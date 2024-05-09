class Feature:
    def __init__(self, title, description, level, subclass=None, optional=False):
        self.title = title
        self.description = description
        self.level = level
        self.subclass = subclass
        self.optional = optional