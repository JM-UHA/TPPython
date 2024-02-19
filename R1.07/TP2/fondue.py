BASE = 4
fromage = 800.0  # en g
eau = 2
ail = 2
pain = 400

nombre_convives = int(input("Combien de convives pour préparer la fondue ? : "))

calc_fromage = fromage * nombre_convives / BASE
calc_eau = eau * nombre_convives / BASE
calc_ail = ail * nombre_convives / BASE
calc_pain = pain * nombre_convives / BASE

print(
    f"Pour faire une fondue fribourgeoise pour {nombre_convives}, il vous faut :\n"
    f"- {calc_fromage}g de fromage\n"
    f"- {calc_eau}dL d'eau\n"
    f"- {calc_ail} gousse(s) d'ail\n"
    f"- {calc_pain}gr de pain\n"
)
