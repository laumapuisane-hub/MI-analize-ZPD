import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
from statsmodels.stats.contingency_tables import mcnemar

# ielādē CSV (faila nosaukums 'test_results.csv')
df = pd.read_csv('test_results.csv', sep=';')

tools = ['copilot_pred', 'chatgpt_pred', 'plantapp_pred']

#  Ātrā pārbaude: unikālās vērtības 
print("true_label uniques:", df["true_label"].unique())
for c in tools:
    print(f"{c} uniques:", df[c].unique())

#  Map uz bināru: infected=1, healthy=0 
y_true = df['true_label'].map({'Infected': 1, 'Healthy': 0})

#  Pārbaude: vai mappingā parādās NaN 
nan_true = y_true.isna().sum()
print("\nNaN count in y_true:", nan_true)
if nan_true > 0:
    bad = df.loc[y_true.isna(), "true_label"].unique()
    print("Nesaprotamas true_label vērtības:", bad)

for c in tools:
    y_tmp = df[c].map({'Infected': 1, 'Healthy': 0})
    nan_pred = y_tmp.isna().sum()
    print(f"NaN count in {c}:", nan_pred)
    if nan_pred > 0:
        bad = df.loc[y_tmp.isna(), c].unique()
        print(f"  Nesaprotamas {c} vērtības:", bad)

# Ja ir NaN, metrikas būs nekorektas / kritīs — labāk apstāties
if nan_true > 0 or any(df[c].map({'Infected': 1, 'Healthy': 0}).isna().any() for c in tools):
    raise ValueError("\nCSV satur vērtības ārpus 'Infected'/'Healthy'. Izlabo CSV un palaid vēlreiz.")

#  Metrikas katram rīkam 
for tool in tools:
    y_pred = df[tool].map({'Infected': 1, 'Healthy': 0})

    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    cm = confusion_matrix(y_true, y_pred)  # pēc noklusējuma rindas/kolonnas: [0,1] => [healthy, infected]

    print(f"\n=== {tool} ===")
    print(f"Accuracy = {acc:.4f} -> {acc*100:.2f}%")
    print(f"Precision = {prec:.4f}")
    print(f"Recall (sensitivity) = {rec:.4f}")
    print(f"F1 = {f1:.4f}")
    print("Confusion Matrix (rows=true [Healthy, Infected], cols=predicted [Healthy, Infected]):")
    print(cm)
    print(classification_report(y_true, y_pred, target_names=['Healthy', 'Infected']))

#  McNemar tests (piemērs: copilot vs plantapp) 
# contingency table builder for two predictors on the same samples
def pair_contingency(y_true, a_pred, b_pred):
    a_corr = (y_true == a_pred)
    b_corr = (y_true == b_pred)
    both_correct = sum(a_corr & b_corr)
    a_only = sum(a_corr & ~b_corr)
    b_only = sum(~a_corr & b_corr)
    both_wrong = sum(~a_corr & ~b_corr)
    return [[both_correct, a_only], [b_only, both_wrong]]

from itertools import combinations

print("\nMcNemar tests (pairwise):")
for a_name, b_name in combinations(tools, 2):
    a = df[a_name].map({'Infected': 1, 'Healthy': 0})
    b = df[b_name].map({'Infected': 1, 'Healthy': 0})

    cont = pair_contingency(y_true, a, b)
    # try exact test first; fall back to asymptotic if it fails
    try:
        result = mcnemar(cont, exact=True)
        pval = result.pvalue
    except Exception:
        result = mcnemar(cont, exact=False)
        pval = result.pvalue

    print(f"\nMcNemar test {a_name} vs {b_name}")
    print("contingency:", cont)
    print("p-value:", pval)

