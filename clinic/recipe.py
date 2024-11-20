class Recipe:
    def __init__(self, recipe_id: int, patient: Patient, medications: str):
        self.recipe_id = recipe_id  # ID рецепта
        self.patient = patient  # Пациент, для которого выписан рецепт
        self.medications = medications  # Перечень медикаментов

    def __str__(self) -> str:
        return f"Recipe({self.recipe_id}, {self.patient.get_name()}, {self.medications})"