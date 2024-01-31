def un_text():
    time_of_day = input("Moment de la journée : ")
    body_part_plural = input("Une partie du corps : ")
    color = input("Une couleur: ")
    verb_past_tense = input("Verbe (à l'imparfait 3e personne du pluriel): ")
    food = input("Nourriture : ")
    noun1 = input("Nom: ")
    noun_plural_1 = input("Nom (au pluriel): ")
    adj1 = input("Adjectif: ")
    adj2 = input("Adjectif: ")

    text = f"C'était un {adj1} {time_of_day} d'été quand l'humanité découvrit que le vaccin du covid ne protégeait pas de cette maladie.\n \
The Walking Deads étaient dans la vraie vie.\n Ils étaient là pour dévorer {body_part_plural} et déambulaient dans les rues avec des {noun_plural_1} \
dans leurs mains.\n Leur peau était {color} et certains {verb_past_tense} pour trouver des {food}.\n Ils étaient {adj2}, n'ayant plus rien d'humain...\n \
Les anti-vax auraient donc raison depuis tout ce temps ?\n Ou est-ce l'oeuvre d'un être maléfique, un nouveau complot ?\n J'entends parler que cela serait un \
plan secret de \"nettoyage\" organisé par {noun1}."

    print(text)