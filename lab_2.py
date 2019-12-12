from sklearn.datasets import load_wine
import matplotlib.pyplot as plt

wines = load_wine()

X = wines.data
y = wines.target

scatter_feature_name_1='color_intensity'
scatter_feature_name_2='alcohol'
fig = plt.scatter(wines[scatter_feature_name_1], wines[scatter_feature_name_2])

plt.xlabel(scatter_feature_name_1)
plt.ylabel(scatter_feature_name_2)
plt.show()