import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve

n = 10000
ratio = .95
n_0 = int((1-ratio) * n)
n_1 = int(ratio * n)

y = np.array([0] * n_0 + [1] * n_1)
y_porba = np.array([1] * n)
y_pred = y_porba > .5

# print(f'accuracy score: {accuracy_score(y, y_pred)}')
# cf_mat = confusion_matrix(y, y_pred)

# print('Confusion matrix')
# print(cf_mat)

# print(f'class 0 accuracy: {cf_mat[0][0]/n_0}')
# print(f'class 1 accuracy: {cf_mat[1][1]/n_1}')


y = np.array([0] * n_0 + [1] * n_1)

# below are the probabilities obtained from a hypothetical model that doesn't always predict the mode
y_proba_2 = np.array(
    np.random.uniform(0, .7, n_0).tolist() +
    np.random.uniform(.3, 1, n_1).tolist()
)
y_pred_2 = y_proba_2 > .5


def plot_roc_curve(true_y, y_prob):
    fpr, tpr, theresholds = roc_curve(true_y, y_prob)
    plt.plot(fpr, tpr)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")


# plot_roc_curve(y, y_porba)
# print(f'model 1 AUC score: {roc_auc_score(y, y_porba)}')
# plt.show()


plot_roc_curve(y, y_proba_2)
print(f'model 2 AUC score: {roc_auc_score(y, y_porba)}')
plt.show()
