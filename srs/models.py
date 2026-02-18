
from catboost import CatBoostClassifier


def get_base_CatBoostClassifier():
    return CatBoostClassifier(
        iterations=10,
        depth=4,
        learning_rate=0.25,
        loss_function="MultiLogloss",
        nan_mode="Min",
        random_seed=1234,
        verbose=1,
    )