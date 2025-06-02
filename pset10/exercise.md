# Toverdrankjes (9pt)
In een het toverbos moeten verschillende toverdrankjes tegelijkertijd actief zijn om een betovering succesvol te laten werken. In je rugzak heb je n unieke toverdrankjes, die elk een werkingsduur van t1…t{n seconden hebben. Het duurt `s` seconden om een toverdrankje te drinken. Is het mogelijk om alle drankjes tegelijkertijd actief te hebben?

Als de werking van een toverdrankje eindigt op hetzelfde moment dat je een ander toverdrankje drinkt, worden de toverdrankjes niet als tegelijkertijd actief beschouwd.

## Input
De invoer bestaat uit:
- Eén regel met twee hele positieve getallen, `n`, `s`, het aantal drankjes in je rugzak en het aantal seconden dat het duurt om een drankje te drinken.
- Eén regel met `n` gehele getallen `i`, die de werkingsduur van een drankje in seconden aangeven.

## Output
Geef ‘Ja’ als alle toverdrankjes tegelijkertijd actief kunnen zijn, anders geef ‘Nee’.

|Input|Output|
|-----|------|
|5 1<br>1 2 3 4 5|Ja|
|3 2<br>4 3 2|Nee|