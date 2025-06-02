# Eindeloos scrollen (15pt)

Ahmed heeft eindelijk TikTok gedownload om up-to-date te blijven met de grappen van de studenten. Hij begint met een volledige aandachtsspanne, maar elke keer dat hij een video bekijkt, verliest hij een beetje van die aandacht. Hoeveel aandacht hij verliest hangt af van hoe interessant hij de video vindt. Als Ahmed zijn aandacht onder de `m` zakt (`a` < `m`) kan hij een pauze nemen om zichzelf weer even op te frissen, helaas is iedere pauze minder effectief dan de vorige. Ahmed moet gebruikmaken van de pauzes totdat de effectiviteit van zijn pauzes **0** is.

Schrijf een programma dat bepaalt hoeveel video's Ahmed kan bekijken totdat zijn aandachtsspanne onder het minimum percentage komt (`a` < `m`).

## Input
De invoer bestaat uit vijf regels:

- Eén regel met een positief geheel getal `a`, de initiële aandachtsspanne als percentage (0 ≤ `a` < 100).
- Eén regel met een positief geheel getal `m`, het minimumpercentage aandacht waarbij interesse blijft.
- Eén regel met een positief geheel getal `b`, de effectiviteit van aandachtsspanne waarmee Ahmed zijn aandacht herstelt na een pauze. (`a`+`b`).
- Eén regel met een positief geheel getal `d`, het verlies van effectiviteit van elke volgende pauze.
- Eén regel met lijst `i`, bestaande uit 5 reële getallen tussen 0 en 1 die de interessepercentages van elke video aangeven (als Ahmed meer dan 5 video's kan bekijken, begint hij opnieuw bij het begin van de lijst).

## Output
Het aantal video's dat Ahmed kan bekijken zonder dat hij verveeld raakt.

|Input|Output|
|-----|------|
|80<br>25<br>20<br>10<br>0.1 0.3 0.4 0.1 0.2|9|
|100<br>50<br>0<br>0<br>0.5 0.5 0.5 0.5 0.5|2|
|60<br>15<br>30<br>5<br>0.1 0.15 0.1 0.5 0.2|25|
|80<br>70<br>30<br>10<br>0.2 0.2 0.4 0.2 0.2|3|