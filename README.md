# 🚗 Concours Kaggle : Russian Car Plates Price Prediction

**Prédire le prix des plaques d'immatriculation en Russie... avec la data science ?**  
C'est le défi que je relève dans ce projet Kaggle où j'analyse un marché unique mêlant tradition, symbolisme et économie.

## 📊 Objectif
Développer un modèle prédictif estimant la valeur marchande des plaques d'immatriculation russes en exploitant :
- Rareté des combinaisons alphanumériques
- Symbolisme culturel (chiffres "magiques", lettres spéciales)
- Affiliation gouvernementale
- Popularité régionale

## 🛠️ Approche Technique

### 🎯 Méthodologie
| Étape | Outils/Techniques | Innovations |
|-------|-------------------|-------------|
| **EDA** | Pandas, Matplotlib | Analyse des motifs de prix extrêmes |
| **Feature Engineering** | Mutual Info, Keras | Détection de plaques premium (`777`, `ААА`) |
| **Modélisation** | LightGBM, XGBoost | Stacking optimisé pour SMAPE |
| **Post-traitement** | NumPy, Scikit-learn | Clipping des valeurs aberrantes |

### 🏆 Modèles Implémentés
```python
# Modèle LightGBM optimisé
lgbm_params = {
    'objective': 'mape',
    'num_leaves': 127,
    'learning_rate': 0.03,
    'feature_fraction': 0.7
}

# Stacking avancé
stack = StackingRegressor(
    estimators=[('lgbm', LGBMRegressor(**lgbm_params)),
               ('xgb', XGBRegressor(objective='reg:absoluteerror'))],
    final_estimator=LGBMRegressor()
)
