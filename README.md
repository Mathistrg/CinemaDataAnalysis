### Exercice 3 : Analyse de la relation entre infrastructures et fréquentation

**Focus sur 2022 :**  
Les données de l'année 2022 ont été utilisées pour analyser l'influence des infrastructures sur la fréquentation des cinémas.

---

#### Résultats de la corrélation :

- **Nombre d'écrans vs Entrées annuelles :**  
  - Corrélation : **0.2061**  
  - Interprétation : Relation positive significative.

- **Nombre de fauteuils vs Entrées annuelles :**  
  - Corrélation : **0.0009**  
  - Interprétation : Relation très faible par rapport au nombre d'écrans.

---

#### Visualisation :

Deux nuages de points accompagnés de régressions linéaires ont été créés pour représenter les relations suivantes :  

1. **Nombre d'écrans et entrées annuelles :**
   - Montre une tendance positive claire.

2. **Nombre de fauteuils et entrées annuelles :**
   - Une tendance beaucoup moins marquée.   

---

#### Conclusion :

- **Impact principal :** Le nombre d'écrans a un impact plus significatif sur les entrées annuelles comparé au nombre de fauteuils.
- **Corrélation élevée :** L'effet des écrans est confirmé par une corrélation plus élevée (**0.2061**) par rapport aux fauteuils (**0.0009**).

---


# Analyse des modèles prédictifs et recommandations stratégiques

## Exercice 4 : Analyse des performances du modèle

### Question : Selon les performances du modèle, le nombre d'écrans ou de fauteuils est-il un bon prédicteur des entrées ?

Le modèle montre que **le nombre d'écrans est un meilleur prédicteur des entrées annuelles que le nombre de fauteuils**. Voici les points principaux de l'analyse :

- **Coefficient pour les écrans** : `41 482.68`.  
  Cela signifie qu'ajouter un écran supplémentaire augmenterait les entrées annuelles de **41 483** en moyenne.

- **Coefficient pour les fauteuils** : `30.83`.  
  Cela signifie qu'ajouter un fauteuil supplémentaire augmenterait les entrées annuelles de **31** en moyenne.

Cependant, le score du modèle (**R² ≈ 0.54**) montre qu'il explique seulement **54%** de la variance des données.  
Cela indique que d'autres facteurs non inclus dans le modèle influencent également les entrées annuelles.

---

## Exercice 5 : Recommandations stratégiques

### Calculs effectués (présents dans le code) :

#### Scénarios étudiés :

1. **Situation actuelle :**  
   - 2 écrans, 120 fauteuils  
   - **Entrées estimées** : `35 541`

2. **Ajout d'un écran (3 écrans, 120 fauteuils) :**  
   - **Entrées estimées** : `77 024`  
   - **Gain potentiel** : `+41 483`

3. **Ajout de 50 fauteuils (2 écrans, 170 fauteuils) :**  
   - **Entrées estimées** : `37 083`  
   - **Gain potentiel** : `+1 542`

#### Comparaison des coûts :
- **Coût moyen d'un écran de cinéma** : `10 000€`  
- **Coût moyen d'un fauteuil de cinéma** : `200€`  

Acheter **50 fauteuils** coûterait environ `10 000€`, soit le même prix qu'un nouvel écran.  

---

### Recommandation stratégique :

Il est **plus rentable** d'investir dans **l'ajout d'un écran** plutôt que d'ajouter des fauteuils.  
Un écran supplémentaire a un impact beaucoup plus significatif sur les entrées annuelles qu'un nombre équivalent de fauteuils.  

**Résumé des recommandations :**
- Prioriser l'augmentation du **nombre d'écrans** pour maximiser les entrées.
- Considérer l'ajout de fauteuils uniquement lorsque la capacité des salles devient un frein à la fréquentation.

---

## Résumé des calculs effectués :

Pour une commune de **20 000 habitants**, voici les estimations des entrées annuelles :  

| Scénario                        | Nombre d'écrans | Nombre de fauteuils | Entrées estimées | Gain par rapport à l'actuel |
|---------------------------------|-----------------|----------------------|------------------|----------------------------|
| Situation actuelle              | 2               | 120                  | 35 541           | -                          |
| Ajout d'un écran supplémentaire | 3               | 120                  | 77 024           | +41 483                    |
| Ajout de 50 fauteuils           | 2               | 170                  | 37 083           | +1 542                     |

---
