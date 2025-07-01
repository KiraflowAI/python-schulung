#
# Unit Tests
# Code ist ein lebendiges Produkt. Das heißt, einmal geschrieben, bleibt eine Codebasis nie so wie sie ist. Fehler müssen korrigiert oder neue Features hinzugefügt werden, die Anwendungsfreundlichkeit soll gesteigert werden oder die Laufzeit durch klügere Algorithmen verbessert werden. Es gibt viele Gründe, warum sich Code des selben Programms im Laufe der Zeit ändert, aber wie stellt man sicher, dass bei Änderungen (groß oder klein) alles weiterhin funktioniert?
# Eine Antwort auf diese Frage sind Unittests. Diese werden von den Programmierern parallel (oder vor dem eigentlichen Code) geschrieben und werden zukünftig immer ausgeführt, wenn es eine Änderung im Code gibt. Diese Unittests überprüfen dann nämlich, ob die einzelnen Bausteine meines Codes (die "Units"/Einheiten) immer noch funktionieren, oder ob irgendetwas durch die Änderungen gestört wurde.
# In einer Metapher gesprochen: Ein Restaurantbesitzer möchte die Küche renovieren. Er lässt von den Köchen eine lange Liste von Tests erstellen. Z.B. "Es gibt Kochlöffel"; "Die Herdplatte wird heiß, wenn man daran dreht"; "Der Eisschrank kann eine Temperatur von -17 °C halten" usw. Alle diese Tests funktionieren bisher und das müssen sie auch, wenn die neue Küche eingebaut ist. In der neuen Küche kommen noch neue Geräte hinzu und auch für diese würde man weitere Tests der Liste hinzufügen, um alles für die Zukunft zu sichern.

# Betrachten wir das folgende Beispiel, in dem die Korrektheit der quadrat Funktion getestet wird. Wir sehen hier vier Tests, die prüfen, ob
# quadrat(5) == 25,
# quadrat(0) == 0,
# quadrat(1) == 1 und
# quadrat(-5) == 25 gelten.


