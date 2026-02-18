import polars as pl

__all__ = [
    'get_cat_feature_names',
    'cast_cat_features',
    'save_submit'
]

def get_cat_feature_names(df):
    return [col for col in df.columns if col.startswith('cat_feature')]


def cast_cat_features(df, cat_feature_names):
    if not cat_feature_names:
        return df
    return df.with_columns(pl.col(cat_feature_names).cast(pl.Int32))


def save_submit(df, path='data/sample_submit.parquet'):
    df.write_parquet(path)
