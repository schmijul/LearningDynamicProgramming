# Dynamic Programming



## Ursprung

### Divide & Conquer - Prinzip

- Divide : teile ein Problem in unabhängige Teilprobleme

- Conquer : löse die Teilprobleme

- Kombiniere: zusammensetzen der Teillösungen > lösung des Gesamtproblems


### Unterschied

- Divide & Conquer würden identische Teilprobleme mehrfach Lösen > Problematik mit hoher Anzahl an ident. Teilproblemen ( hier is DP besser)


## Anwendungsfälle

- Optimierungsprobleme ( Matrix Muliplikation)
- Probleme mit vielen abhängigen Teilproblemen


## Grundidee

Lösung von Teilproblemen peicher 

- Identische Teilprobleme müsen nicht doppelt gelöst werden.
- Laufzeitoptimierung

## Vorgehen

1. Was ist die Struktur einer Optimatlen Lösung?
2. Austellen einer Rekursionsgleichung
3. Berechnung des Weges einer opt. Lösung
4. Konstruktion einer opt. Lösung


# Greedy

## Anwednungsfälle

- Optimierungsprobleme
- Kürzere Laufzeit als DP
- Teilprobleme lokal lösen -> globale opt. Lösung
- erst Entscheiden, dann lösen
- Annähern einer Lösung für NP-harte Probleme


# Wann ist die Lösung opt.?

- Greedy
    - Teilproblem-Eigenschaft erfüllt
    - Greedy-Eigenschaft erfüllt
    - Lösung wird hier approximiert

- DP
    - Teilproblem-Eigenschaft erfüllt

DP dauert mesit länger als DP
