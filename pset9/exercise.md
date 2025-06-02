# Bijna Perfecte Gokjes (7pt)
Voor zijn 22e verjaardag heeft je vriend je uitgenodigd voor een feest met als thema het getal twee. Wanneer je op het feest aankomt, merk je dat iedereen een spelletje speelt. Je vriend is een echte datafreak en houdt erg van cijfers. Daarom gaat het spel ook over getallen. Iemand verzint een target nummer en de rest schrijft een eigen getal op. Alle papiertjes worden verzameld en de winnaar(s) worden bepaald. Het op één na dichtstbijzijnde getal wint! Omdat er meerdere mensen meedoen, kan het zijn dat er ook meerdere winnaars zijn.

Het spel wordt erg populair, maar het duurt te lang om de winnaar te bepalen. Kun je helpen het proces te automatiseren?

## Input
De invoer bestaat uit:
- Eén regel met twee gehele getallen: `n`, `k`, het aantal mensen dat het spel speelt en het target nummer.
- Eén regel met `n` getallen `g` die de gokken vertegenwoordigen.

## Output
Geef het op één na dichtstbijzijnde getal bij het target nummer van de reeks getallen. Als twee getallen even dicht bij het target nummer liggen, beschouw dan het kleinere getal als het meest dichtbij.

|Input|Output|
|-----|------|
|3 10<br>7 15 12|7|
|5 20<br>17 17 15 23 50|23|
|7 16360<br>50843 82492 6468 98519 14206 49461 50061|6468|