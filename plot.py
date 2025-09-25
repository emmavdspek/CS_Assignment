import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load the data
colnames = ["year", "#students", "beer"]
data = pd.read_csv(
    "istherecorrelation.csv",
    delimiter=";",
    names=colnames,
    skiprows=1,
)

# reformat the data to be compatible for plotting
data["beer"] = data["beer"].astype(float)
for i in range(len(data["#students"])):
    data.loc[i, "#students"] = data.loc[i, "#students"].replace(",", ".")
    data.loc[i, "beer"] = data.loc[i, "beer"] * 10 ** (-4)
data["#students"] = data["#students"].astype(float)


# plot the data
fig, ax1 = plt.subplots(1, figsize=(8, 4), dpi=300)
ax2 = ax1.twinx()
axes = [ax1, ax2]
colors = ["darkred", "coral"]
ylabels = [r"$N_{students}~[\cdot 10^3]$", r"beer consumed [$\cdot 10^9$ L]"]
width = 0.25  # width of the bins
range_ratio = 0
for i in range(2):
    ax = axes[i]
    plotdata = np.array(data[colnames[i + 1]]).astype(float)
    ax.bar(
        x=data["year"].values + width * i,
        height=plotdata,
        width=width * 0.8,
        color=colors[i],
    )
    if np.max(plotdata) / np.min(plotdata) > range_ratio:
        range_ratio = np.max(plotdata) / np.min(plotdata)
    # ax.set_ylim(np.min(plotdata) * 0.9, np.max(plotdata) * 1.05)
    ax.tick_params(axis="y", labelcolor=colors[i])
    ax.set_ylabel(ylabels[i], color=colors[i])
ax1.set_ylim(
    np.min(data["#students"]) * 0.95, np.min(data["#students"]) * range_ratio * 1.05
)
ax2.set_ylim(np.min(data["beer"]) * 0.95, np.min(data["beer"]) * range_ratio * 1.05)
ax1.set_xlim(np.min(data["year"]) - 0.5, np.max(data["year"]) + 0.5 + width)
ax1.set_xticks(data["year"] + width / 2, data["year"])
plt.tight_layout()
plt.savefig("plot.png")
plt.show()
