# Springen maar! (20pt)
Op een oneindig schaakbord, waarbij elk vierkant een zijde heeft van `Z` meter, zijn de vierkanten zwart of wit. Het meest linksonder gelegen vierkant van het schaakbord is zwart. Niels bevindt zich op positie (`x`, `y`) op het bord, uitgedrukt in meters, en maakt verplaatsingen van dx meter naar rechts en `dy` meter omhoog. Na elke verplaatsing staat hij op positie `(x + dx, y + dy)`.

Het probleem is dat Niels alleen kan staan op witte vierkanten van het schaakbord. Als Niels na **10.000** verplaatsingen nog steeds alleen op zwarte vierkanten is geland, kan hij niet ontsnappen. Als hij terechtkomt op een grens tussen twee vierkanten, telt dit niet als het landen op een wit vierkant. Bereken hoeveel verplaatsingen Niels nodig heeft om de zwarte vierkanten te kunnen ontvluchten, of dat hij er voor altijd aan vast zit.

## Input
De invoer bestaat uit:
- Eén regel met vijf hele positieve getallen, `Z`, `x`, `y`, `dx`, `dy`.

## Output
Geef het aantal verplaatsingen weer, en de eindcoordinaten op het bord, of dat Niels niet van de zwarte vierkanten afkomt.

|Input|Output|
|-----|------|
|10 2 3 3 2|Na 3 verplaatsingen bereikt Niels (11, 9).|
|18 72 6 18 6|Niels kan de zwarte vierkanten niet ontsnappen.|