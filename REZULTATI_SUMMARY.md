# Novērtējuma rezultāti

## Dati
- **Kopējais attēlu skaits**: 220 
- **Klases**: Infected (inficēts), Healthy (veselīgs)

## Rīku salīdzinājums

### 1. Copilot (Labākais rezultāts)
- **Precizitāte(%)**: 79.55%
- **Precizitāte**: 0.7686
- **Jutība**: 0.8455
- **F1 rādītājs**: 0.8052

**Kļūdu matrica:**
```
              Predicted
         Healthy  Infected
True  Healthy      82         28
      Infected     17         93
```

### 2. PlantApp
- **Precizitāte(%)**: 76.36%
- **Precizitāte**: 0.8295
- **Jutība**: 0.6636
- **F1 rādītājs**: 0.7374

**Kļūdu matrica:**
```
              Predicted
         Healthy  Infected
True  Healthy      95         15
      Infected     37         73
```

### 3. ChatGPT (Sliktākais rezultāts)
- **Precizitāte**: 68.64%
- **Precizitāte(%)**: 0.6723
- **Jutība**: 0.7273
- **F1 rādītājs**: 0.6987

**Kļūdu matrica:**
```
              Predicted
         Healthy  Infected
True  Healthy      71         39
      Infected     30         80
```

## Neparametriskais statistiskais tests: McNemar tests

- **Testa rezultāti:**
      - `copilot_pred` vs `chatgpt_pred`: contingency = [[126, 49], [25, 20]], p = 0.00708
      - `copilot_pred` vs `plantapp_pred`: contingency = [[136, 39], [32, 13]], p = 0.47669
      - `chatgpt_pred` vs `plantapp_pred`: contingency = [[126, 25], [42, 27]], p = 0.04980

- **Interpretācija:**
      - `copilot` vs `chatgpt`: p = 0.00708 < 0.05 0.05— atšķirība ir **statistiski nozīmīga**; Copilot darbojas labāk.
      - `copilot` vs `plantapp`: p = 0.47669 > 0.05 — **nav statistiski nozīmīgas atšķirības**.
      - `chatgpt` vs `plantapp`: p = 0.04980 ~ 0.05 — ļoti tuvu robežai; pēc klasiskas 0.05 robežas tas ir **statistiski nozīmīgs**, taču efektam ir jābūt interpretētam piesardzīgi.

- **Salīdzināšanas korekcija (Bonferroni):**
      -3 pāru salīdzinājumus, pēc Bonferroni koriģētais alfa = 0.05 / 3 ≈ 0.0167.
      - Pielietojot Bonferroni kritēriju: tikai `copilot` vs `chatgpt` (p = 0.00708) paliek **statistiski nozīmīgs** (0.00708 < 0.0167). `chatgpt` vs `plantapp` (p = 0.04980) vairs nav nozīmīgs pēc korekcijas.
