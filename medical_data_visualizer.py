import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df.weight / (df.height/100) ** 2 > 25).astype(int)

print(df)


# 3
df['gluc'] = (df['gluc'] > 1).astype(int)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)

print(df)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['gluc', 'cholesterol', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.sort_values('variable')
    

    # 7
    df_cat = df_cat.rename(columns={"value": "total"})



    # 8
    sns_plot = sns.catplot(data=df_cat, x="variable", y="total", kind="bar", col="cardio", estimator=len, hue="total")
    fig = sns_plot.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[
      (df['ap_lo'] <= df['ap_hi']) &
      (df['height'] >= df['height'].quantile(0.025)) &
      (df['height'] <= df['height'].quantile(0.975)) &
      (df['weight'] >= df['weight'].quantile(0.025)) &
      (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    corr[mask] = np.nan

    # 14
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15
    sns.heatmap(data = corr, annot=True, fmt=".1f", linewidth=.3, vmax=0.3)

    # 16
    fig.savefig('heatmap.png')
    return fig
