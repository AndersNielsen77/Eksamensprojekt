from math import *
import time
print "Du kan bruge dette billede på dette link som hjælp til at forstå hvilken dele af ballonen vi udregner:"
print "https://gyazo.com/43f017e828a64e1187728a07677e57ed"
print "Det er anbefalet at bruge programmet i fuldskærm"
time.sleep(1)
h1 = input("Skriv totale højde af ballon:")
diameter = input("Skriv kugleafnittets diameter:")
keglediameter = input("Skriv keglestubbens lille diameter:")
baner = input ("Skriv hvor mange baner du vil have:")

#Formel samling:
radiuskegle = (keglediameter / 2)
radius = (diameter/2)
a1 = 2 * radiuskegle * pi
b1 = sqrt(((h1 - radius)**2 + radiuskegle**2))
c1 = sqrt((b1**2 - radius**2))
d1 = (b1**2 + (h1 - radius)**2 - radiuskegle**2) / (2 * b1 * (h1 - radius))
e1 = acos(d1)
f1 = (radius**2 + b1**2 - c1**2) / (2 * radius * b1)
g1 = acos(f1)
h1 = 180 - (degrees(e1) + degrees(g1))
i1 = (2 * pi * radius)/360 * h1


print "Programmet vil nu give jer de understøttende udregninger:"
time.sleep(2)
print ""
print "Vi bruger formlen 2 * r * Pi for at finde radius af keglens cirkel, dit resultat bliver:"
print round(a1,3)
print ""
print "Med denne radius kan vi finde ud af hvor lang bunden af vores baner skal være, ved at dividere omkredsen med det antal baner vi har:"
print round((a1 / baner),3)
print ""
time.sleep(0.5)
print "Vi finder længden f (ses på billedet) ved at"
print "bruge pytagoras, vi kender højden fra bunden af keglen til centeret af cirkel buen (h1 på billedet)"
print "ved at minus cirkelbuens radius med den totale højde af vores ballon (H1 på billedet), denne værdi kan vi"
print "pludse keglens lille diameter (d1 på billede) sammen med i pytagoras og derefter finde kvadratroden af det. Så har vi f længden:"
print round(b1,3)
print ""
time.sleep(0.5)
print "Vi finder b1 som ses på billedet ved at bruge omvendt pytagoras fordi vinklen S1 er vinkelret. Vi minuser"
print "f med R1, det finder vi så kvadratroden af:"
print round(c1,3)
print ""
time.sleep(0.5)
print "Da vi nu har fundet alle disse sider kan vi finde"
print "vinklen C for trekanten ABC og vinklen C for trekanten S1CB (ses på billede)."
print "Det gør vi ved at bruge cosinus relationen Cos(C) = (a^2 + b^2 - c^2)/(2 * a * b)."
print "Resultatet for vinkel C i trekant ABC bliver: (OBS det bliver vist i radianer!!!)"
print round(d1,3)
print ""
time.sleep(0.5)
print "Resultatet for vinkel C i trekant S1CB bliver: (OBS det bliver vist i radianer!!!)"
print round(f1,3)
print ""
time.sleep(0.5)
print "Da vi har fundet disse to vinkler kan vi nu finde den store vinkel C i trekant CS1T1,"
print "det gør vi bare ved at sammenlægge de to vinkler vi lige fandt og herefter minus 180 med det:"
print "(programmet her konvertere automatisk fra radianer til grader)"
print round(h1,3)
print ""
time.sleep(0.5)
print "Til sidst kan vi finde cirkelbuen S1T1 med formlen (2 * Pi * r) / 360 * v:"
print round(i1,3)
print ""
time.sleep(0.5)

V = 0
loop = 0
print "Her finder vi bane bredde og bane længde ved forskellige vinkler. For at finde bane bredde bruger vi formlen (2 * Pi * (kugle radius * sin(V)) / baner."
print "For at finde bane længde bruger vi formlen 2 * Pi * kugle radius * V / 360."
print "Husk at vi forhøjer V værdien hele tiden(med 5 i dette program) for at finde forskellige bane længder og bredder ved forskellige vinkler."
for loop in range(0, baner + 11):
        V = V + 5
        rny = radius * sin(radians(V))
        j1 = (2 * pi * rny) / baner
        k1 = 2 * pi * radius * V / 360
        loop + 1
        print ""
        print "V:" + str(V) + "    Bb:" + str(round(j1,3)) + "    Bl:" + str(round(k1,3))
        






	
