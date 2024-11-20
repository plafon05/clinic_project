class Recipe:
    recipes_db = []  # База данных рецептов

    def __init__(self, patient, medication, date, doctor):
        self.patient = patient
        self.medication = medication
        self.date = date
        self.doctor = doctor
        Recipe.recipes_db.append(self)

    @staticmethod
    def get_all_recipes():
        return Recipe.recipes_db