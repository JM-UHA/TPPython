import json
import pathlib


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


class Bibliothèque:
    def __init__(self, liste_des_films: list[Film]) -> None:
        self._films: list[Film] = liste_des_films

    def __str__(self) -> str:
        return f"Bibliothèque(films={len(self.films)})"

    @property
    def films(self) -> list[Film]:
        return self._films

    def afficher_films(self):
        print(
            "\n\n".join(
                [
                    f"Film {i+1} : {film.titre}\nDate : {film.date_de_sortie}\nNote : {film.note}"
                    f"\nAvis : {', '.join(film.avis)}"
                    for i, film in enumerate(self.films)
                ]
            )
        )

    def mostrate(self):
        return max(self.films, key=lambda film: film.note)

    def top3(self):
        return sorted(self.films, key=lambda film: film.note, reverse=True)[:3]

    def lastmovie(self):
        return max(self.films, key=lambda film: film.date_de_sortie)

    def avrgnote(self):
        return sum([film.note for film in self.films]) / len(self.films)

    def to_json_file(self):
        data = {"films": [film.to_json() for film in self.films]}
        with open("films.json", "w") as file:
            json.dump(data, file)

    @classmethod
    def from_json(cls, file: str | pathlib.Path):
        if isinstance(file, pathlib.Path):
            file = file.resolve()
        with open(file, "r") as movies:
            data = json.load(movies)
            return cls([Film(**film) for film in data["films"]])

bibli = Bibliothèque.from_json(pathlib.Path(__file__, "..", "movies.json"))
print(bibli.afficher_films())
print(bibli.mostrate())
print(bibli.top3())
print(bibli.lastmovie())
print(bibli.avrgnote())
