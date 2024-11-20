class Department:
    departments_db = []  # База данных отделений

    def __init__(self, name: str):
        self.name = name
        Department.departments_db.append(self)

    @staticmethod
    def get_all_departments():
        return Department.departments_db