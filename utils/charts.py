import plotly.express as px
import plotly.graph_objects as go


def device_distribution(df):
    fig = px.histogram(
        df,
        x="Device_Type",
        color="Device_Type",
        title="Device Type Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def maintenance_cost_chart(df):

    cost_df = (
        df.groupby("Device_Type")["Maintenance_Cost"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        cost_df,
        x="Device_Type",
        y="Maintenance_Cost",
        color="Maintenance_Cost",
        title="Average Maintenance Cost by Device"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def downtime_chart(df):

    fig = px.scatter(
        df,
        x="Downtime",
        y="Maintenance_Cost",
        color="Device_Type",
        size="Failure_Event_Count",
        hover_data=["Country"],
        title="Downtime vs Maintenance Cost"
    )

    fig.update_layout(
        template="plotly_white",
        height=550
    )

    return fig


def failure_chart(df):

    fig = px.histogram(
        df,
        x="Failure_Event_Count",
        color="Maintenance_Class",
        title="Failure Event Analysis"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def age_vs_failure(df):

    fig = px.scatter(
        df,
        x="Age",
        y="Failure_Event_Count",
        color="Device_Type",
        size="Maintenance_Cost",
        title="Device Age vs Failure Count"
    )

    fig.update_layout(
        template="plotly_white",
        height=550
    )

    return fig


def maintenance_frequency_chart(df):

    fig = px.box(
        df,
        x="Device_Type",
        y="Maintenance_Frequency",
        color="Device_Type",
        title="Maintenance Frequency Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def country_analysis(df):

    country_df = (
        df.groupby("Country")["Failure_Event_Count"]
        .sum()
        .reset_index()
        .sort_values(
            by="Failure_Event_Count",
            ascending=False
        )
    )

    fig = px.bar(
        country_df,
        x="Country",
        y="Failure_Event_Count",
        color="Failure_Event_Count",
        title="Failures by Country"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig


def sunburst_chart(df):

    fig = px.sunburst(
        df,
        path=[
            "Country",
            "Device_Type",
            "Maintenance_Class"
        ],
        title="Medical Device Hierarchy Analysis"
    )

    fig.update_layout(
        height=700
    )

    return fig


def correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include=["int64", "float64"]
    )

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation Heatmap"
    )

    fig.update_layout(
        height=650
    )

    return fig


def risk_devices_table(df):

    risk_df = df.sort_values(
        by="Failure_Event_Count",
        ascending=False
    )

    return risk_df.head(20)
