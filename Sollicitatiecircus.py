from operator import ge


print("Sollicitatieformulier: Circusdirecteur voor Circus HotelDeBotel ")
ready = input("De vragen beginnen nu, als u ervoor klaar bent tiep Ja: ") .lower()
if ready == "ja":
    vraag1 = input("Wat is uw naam? ") .lower()
    vraag2 = input ("Wat is uw geslacht? ")
    vraag3 = input("Heeft u ervaring met Dieren-dressuur? ") .lower()
    if vraag3 == "ja" :
        ervaring_dier = input("Hoeveel jaren praktijkervaring heeft u met Dieren-dressuur").lower()
        ervaring_dier = int (ervaring_dier)
        if ervaring_dier >= 4: 
            diploma = input("Heeft u een MBO 4 ondernemen diploma? ")
            if diploma == "ja" :
                rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs? ")
                if rijbewijs == "ja" :
                    hogehoed = input("Heeft u een hoge hoed? ")
                    if hogehoed == "ja" :
                        if vraag2 == "man" :
                            snor = input("Heeft u een snor?")
                            if snor == "ja":
                                lengte_snor = input("Wat is de breedte van uw snor? ")
                                lengte_snor = int (lengte_snor)
                                if lengte_snor >= 10 :
                                    lengte = input("Hoelang bent u in cm ")
                                    lengte = int (lengte)
                                    if lengte >= 150 :
                                        gewicht = input("Hoe zwaar bent u in kilo's? ")
                                        gewicht = int (gewicht)
                                        if gewicht >= 90 :
                                            certificaat = input ("Heeft u het certificaat Overleven met gevaarlijk personeel? ")
                                            if certificaat == "ja":
                                                print("U bent perfect voor deze positie en u krijgt binnenkort een mail!")
                        elif vraag2 == "vrouw" :
                            haarkleur = input("Heeft u rood haar? ")
                            if haarkleur == "ja":
                                krulhaar = input("heeft u krulhaar? ")
                                if krulhaar == "ja":
                                    lengte_krulhaar = input("Hoelang is uw krulhaar in cm? ")
                                    lengte_krulhaar = int (lengte_krulhaar)
                                    if lengte_krulhaar >= 20: 
                                        lengte = input("Hoelang bent u in cm ")
                                    lengte = int (lengte)
                                    if lengte >= 150 :
                                        gewicht = input("Hoe zwaar bent u in kilo's? ")
                                        gewicht = int (gewicht)
                                        if gewicht >= 90 :
                                            certificaat = input ("Heeft u het certificaat Overleven met gevaarlijk personeel? ")
                                            if certificaat == "ja":
                                                print("U bent perfect voor deze positie en u krijgt binnenkort een mail!")
   
   
   
    elif vraag3 == "nee" :
        jongleren = input("Heeft u ervaring met jongleren? ")
        if jongleren == "ja" :
            ervaring_jongleren = input("Hoeveel jaren ervaring heeft u met Jongleren? ")
            ervaring_jongleren = int (ervaring_jongleren)
            if ervaring_jongleren >= 5 :
                diploma = input("Heeft u een MBO 4 ondernemen diploma? ")
            if diploma == "ja" :
                rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs? ")
                if rijbewijs == "ja" :
                    hogehoed = input("Heeft u een hoge hoed? ")
                    if hogehoed == "ja" :
                        if vraag2 == "man" :
                            snor = input("Heeft u een snor?")
                            if snor == "ja":
                                lengte_snor = input("Wat is de breedte van uw snor? ")
                                lengte_snor = int (lengte_snor)
                                if lengte_snor >= 10 :
                                    lengte = input("Hoelang bent u in cm ")
                                    lengte = int (lengte)
                                    if lengte >= 150 :
                                        gewicht = input("Hoe zwaar bent u in kilo's? ")
                                        gewicht = int (gewicht)
                                        if gewicht >= 90 :
                                            certificaat = input ("Heeft u het certificaat Overleven met gevaarlijk personeel? ")
                                            if certificaat == "ja":
                                                print("U bent perfect voor deze positie en u krijgt binnenkort een mail!")

                        elif vraag2 == "vrouw" :
                            haarkleur = input("Heeft u rood haar? ")
                            if haarkleur == "ja":
                                krulhaar = input("heeft u krulhaar? ")
                                if krulhaar == "ja":
                                    lengte_krulhaar = input("Hoelang is uw krulhaar in cm? ")
                                    lengte_krulhaar = int (lengte_krulhaar)
                                    if lengte_krulhaar >= 20: 
                                        lengte = input("Hoelang bent u in cm ")
                                    lengte = int (lengte)
                                    if lengte >= 150 :
                                        gewicht = input("Hoe zwaar bent u in kilo's? ")
                                        gewicht = int (gewicht)
                                        if gewicht >= 90 :
                                            certificaat = input ("Heeft u het certificaat Overleven met gevaarlijk personeel? ")
                                            if certificaat == "ja":
                                                print("U bent perfect voor deze positie en u krijgt binnenkort een mail!")
        if jongleren == "nee":
            acrobatiek = input("Heeft u ervaring met acrobatiek? ")
            if acrobatiek == "ja":
             ervaring_acrobatiek = input("Hoeveel jaren praktijkervaring heeft u in acrobatiek?")
             ervaring_acrobatiek = int (ervaring_acrobatiek)
            if ervaring_acrobatiek >= 3 :
                diploma = input("Heeft u een MBO 4 ondernemen diploma? ")
            if diploma == "ja" :
                rijbewijs = input("Heeft u een geldig vrachtwagen rijbewijs? ")
                if rijbewijs == "ja" :
                    hogehoed = input("Heeft u een hoge hoed? ")
                    if hogehoed == "ja" :
                        if vraag2 == "man" :
                            snor = input("Heeft u een snor?")
                            if snor == "ja":
                                lengte_snor = input("Wat is de breedte van uw snor? ")
                                lengte_snor = int (lengte_snor)
                                if lengte_snor >= 10 :
                                    lengte = input("Hoelang bent u in cm ")
                                    lengte = int (lengte)
                                    if lengte >= 150 :
                                        gewicht = input("Hoe zwaar bent u in kilo's? ")
                                        gewicht = int (gewicht)
                                        if gewicht >= 90 :
                                            certificaat = input ("Heeft u het certificaat Overleven met gevaarlijk personeel? ")
                                            if certificaat == "ja":
                                                print("U bent perfect voor deze positie en u krijgt binnenkort een mail!")
                        elif vraag2 == "vrouw" :
                            haarkleur = input("Heeft u rood haar? ")
                            if haarkleur == "ja":
                                krulhaar = input("heeft u krulhaar? ")
                                if krulhaar == "ja":
                                    lengte_krulhaar = input("Hoelang is uw krulhaar in cm? ")
                                    lengte_krulhaar = int (lengte_krulhaar)
                                    if lengte_krulhaar >= 20: 
                                        lengte = input("Hoelang bent u in cm ")
                                    lengte = int (lengte)
                                    if lengte >= 150 :
                                        gewicht = input("Hoe zwaar bent u in kilo's? ")
                                        gewicht = int (gewicht)
                                        if gewicht >= 90 :
                                            certificaat = input ("Heeft u het certificaat Overleven met gevaarlijk personeel? ")
                                            if certificaat == "ja":
                                                print("U bent perfect voor deze positie en u krijgt binnenkort een mail!")