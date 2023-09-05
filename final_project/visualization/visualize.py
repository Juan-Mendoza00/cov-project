import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def time_series_vis(dataFrame: pd.DataFrame):
    sns.lineplot(
        data=dataFrame,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series")


# Return top n countries in sorted values. Specify number (n) of countries
def top_n(n,data):
    top_countries_df = (
        data
        .select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(n)
        # .transform_column(
        #     column_name="country_region",
        #     function=lambda x: "red" if x in countries else "lightblue",
        #     dest_column_name="color"
        #     )
        )
    return top_countries_df

def highlight(list,df):
    hl = (
    df
     .transform_column(
            column_name="country_region",
            function=lambda x: "red" if x in list else "lightblue",
            dest_column_name="color"
            )
    )
    return hl

