# Novērtējuma rezultāti

## Dati
- **Kopējais attēlu skaits**: 220 
- **Klases**: Infected (inficēts), Healthy (veselīgs)

## Rīku salīdzinājums

### 1. Copilot (Labākais rezultāts)
- **Precizitāte(%) (Accuracy)**: 79.55%
- **Precizitāte (Precision)**: 0.7686
- **Recall (Jutīgums)**: 0.8455
- **F1 rādītājs**: 0.8052

**Confusion Matrix:**
```
              Predicted
         Healthy  Infected
True  Healthy      82         28
      Infected     17         93
```

**Detalizēts pārskats:**
```
              precision    recall  f1-score   support
     Healthy       0.83      0.75      0.78       110
    Infected       0.77      0.85      0.81       110
    
    accuracy                           0.80       220
   macro avg       0.80      0.80      0.79       220
weighted avg       0.80      0.80      0.79       220
```

---

### 2. PlantApp
- **Precizitāte (Accuracy)**: 76.36%
- **Precisitāte (Precision)**: 0.8295
- **Recall (Jutīgums)**: 0.6636
- **F1 rādītājs**: 0.7374

**Confusion Matrix:**
```
              Predicted
         Healthy  Infected
True  Healthy      95         15
      Infected     37         73
```

**Detalizēts pārskats:**
```
              precision    recall  f1-score   support
     Healthy       0.72      0.86      0.79       110
    Infected       0.83      0.66      0.74       110
    
    accuracy                           0.76       220
   macro avg       0.77      0.76      0.76       220
weighted avg       0.77      0.76      0.76       220
```

---

### 3. ChatGPT (Sliktākais rezultāts)
- **Precizitāte (Accuracy)**: 68.64%
- **Precisitāte (Precision)**: 0.6723
- **Recall (Jutīgums)**: 0.7273
- **F1 rādītājs**: 0.6987

**Confusion Matrix:**
```
              Predicted
         Healthy  Infected
True  Healthy      71         39
      Infected     30         80
```

**Detalizēts pārskats:**
```
              precision    recall  f1-score   support
     Healthy       0.70      0.65      0.67       110
    Infected       0.67      0.73      0.70       110
    
    accuracy                           0.69       220
   macro avg       0.69      0.69      0.69       220
weighted avg       0.69      0.69      0.69       220
```

---

## Statistiskais tests: McNemar

**Copilot vs PlantApp salīdzinājums:**
- **Contingency table**: [[136, 39], [32, 13]]
- **p-value**: 0.477

**Interpretācija**: p-value > 0.05, tāpēc **nav statistiski nozīmīgas atšķirības** starp Copilot un PlantApp veiktspēju.

---

### McNemar — pilni pāru rezultāti un interpretācija

- **Testa rezultāti (pairwise):**
      - `copilot_pred` vs `chatgpt_pred`: contingency = [[126, 49], [25, 20]], p = 0.00708
      - `copilot_pred` vs `plantapp_pred`: contingency = [[136, 39], [32, 13]], p = 0.47669
      - `chatgpt_pred` vs `plantapp_pred`: contingency = [[126, 25], [42, 27]], p = 0.04980

- **Interpretācija:**
      - `copilot` vs `chatgpt`: p = 0.00708 < 0.05 0.05— atšķirība ir **statistiski nozīmīga**; Copilot darbojas labāk.
      - `copilot` vs `plantapp`: p = 0.47669 > 0.05 — **nav statistiski nozīmīgas atšķirības**.
      - `chatgpt` vs `plantapp`: p = 0.04980 ~ 0.05 — ļoti tuvu robežai; pēc klasiskas 0.05 robežas tas ir **statistiski nozīmīgs**, taču efektam ir jābūt interpretētam piesardzīgi.

- **Daudzsalīdzinošuma korekcija (Bonferroni):**
      - Veicam 3 pāru salīdzinājumus, tāpēc Bonferroni koriģētais alfa = 0.05 / 3 ≈ 0.0167.
      - Pielietojot Bonferroni kritēriju: tikai `copilot` vs `chatgpt` (p = 0.00708) paliek **statistiski nozīmīgs** (0.00708 < 0.0167). `chatgpt` vs `plantapp` (p = 0.04980) vairs nav nozīmīgs pēc korekcijas.

- **Praktiska piezīme:** statistiski nozīmīga p-vērtība nenozīmē lielu praktisku labumu — skaties arī atšķirību metrikās (accuracy, recall, precision) un contingency elementus (a_only / b_only), lai saprastu, kāda ir reālā ietekme.

## Secinājumi

1. **Copilot** ir labākais rīks ar **79.55% precizitāti** un labu jutīgumu (84.55%)
2. **PlantApp** ir otrs ar **76.36% precizitāti**, bet ar augstu precizitāti (82.95%)
3. **ChatGPT** ir vājākais ar **68.64% precizitāti**
4. Copilot un PlantApp starp sevi **statistiski neatšķiras** (McNemar tests, p=0.477)
