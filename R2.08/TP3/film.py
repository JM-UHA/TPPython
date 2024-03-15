import json


class Film:
    def __init__(
        self, titre: str, date: str, note: float, avis: list[str]
    ) -> None:
        self._titre = titre
        self._date_de_sortie = date
        self._note = note
        self._avis = avis

    @property
    def titre(self) -> str:
        return self._titre

    @property
    def date_de_sortie(self) -> str:
        return self._date_de_sortie

    @property
    def note(self) -> float:
        return self._note

    @property
    def avis(self) -> list[str]:
        return self._avis

    def __str__(self) -> str:
        return f"Le film {self.titre} est sorti le {self.date_de_sortie}, il a la note {self.note} et voici les avis du public l'ayant vu :\n{self.__liste_avis()}"

    def __repr__(self) -> str:
        return f"<Film titre={self.titre} note={self.note}>"

    def __liste_avis(self) -> str:
        liste_avis = ""
        for avis in self.avis:
            liste_avis += f"\t- {avis}\n"
        return liste_avis

    def to_json(self):
        return json.dumps(self.__dict__)
