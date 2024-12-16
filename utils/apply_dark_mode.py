def apply_dark_mode(fig):
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white"),
        xaxis=dict(gridcolor="gray"),
        yaxis=dict(gridcolor="gray"),
    )
    return fig
# unused, here for future use