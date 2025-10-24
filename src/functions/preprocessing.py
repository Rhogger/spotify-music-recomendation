from scipy.stats import boxcox


def apply_boxcox_transform(X):
    """
    Aplica Box-Cox em instrumentalness e speechiness

    Args:
        X: DataFrame com as features

    Returns:
        X_transformed: DataFrame com Box-Cox aplicado
    """
    X_transformed = X.copy()
    if "instrumentalness" in X_transformed.columns:
        X_transformed["instrumentalness"], _ = boxcox(
            X_transformed["instrumentalness"] + 0.0001
        )
    if "speechiness" in X_transformed.columns:
        X_transformed["speechiness"], _ = boxcox(X_transformed["speechiness"] + 0.0001)
    return X_transformed
