import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# ── Estilo global ──────────────────────────────────────────────
BG = "#E8E8E8"
INK = "#292929"
ACCENT = "#1B6B45"

ns_cmap = LinearSegmentedColormap.from_list("ns_emerald", [INK, ACCENT])


def _style_ax(fig, ax, title, xlabel=None, ylabel=None,
              grid_axis="both", tick_rotation=0, tick_ha="center",
              title_size=15):
    """Aplica el estilo NS (fondo, spines, ticks, grid) a un eje."""
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)

    ax.set_title(title, fontsize=title_size, fontweight="bold", color=INK)
    if xlabel:
        ax.set_xlabel(xlabel, color=INK, fontsize=11)
    if ylabel:
        ax.set_ylabel(ylabel, color=INK, fontsize=11)

    ax.tick_params(colors=INK)
    for spine in ax.spines.values():
        spine.set_color(INK)
        spine.set_linewidth(0.8)

    if grid_axis is not None:
        ax.grid(axis=grid_axis if grid_axis != "both" else None,
                alpha=0.25, color=INK)

    if tick_rotation:
        plt.setp(ax.get_xticklabels(), rotation=tick_rotation,
                  ha=tick_ha, color=INK)
    else:
        plt.setp(ax.get_xticklabels(), color=INK)
    plt.setp(ax.get_yticklabels(), color=INK)


# ── 1. Frontera eficiente + Monte Carlo ────────────────────────
def compute_efficient_frontier(expected_returns_vector, covariance_matrix,
                                min_weight, max_weight, n_points=50,
                                upper_quantile=0.90):
    """Calcula la frontera eficiente (retorno, volatilidad)."""
    efficient_volatility, efficient_returns = [], []

    target_returns = np.linspace(
        expected_returns_vector.min(),
        expected_returns_vector.quantile(upper_quantile),
        n_points
    )

    for target in target_returns:
        try:
            ef = EfficientFrontier(
                expected_returns_vector,
                covariance_matrix,
                weight_bounds=(min_weight, max_weight)
            )
            ef.efficient_return(target)
            ret, vol, _ = ef.portfolio_performance()
            efficient_returns.append(ret)
            efficient_volatility.append(vol)
        except Exception:
            continue

    return efficient_volatility, efficient_returns


def plot_efficient_frontier(simulation_results,
                             max_sharpe_performance,
                             min_volatility_performance,
                             max_sharpe_performance_constrained,
                             efficient_volatility,
                             efficient_returns,
                             figsize=(12, 8)):
    fig, ax = plt.subplots(figsize=figsize)

    scatter = ax.scatter(
        simulation_results["volatility"],
        simulation_results["expected_return"],
        c=simulation_results["sharpe_ratio"],
        cmap=ns_cmap,
        s=6,
        alpha=0.55
    )

    ax.scatter(*max_sharpe_performance[::-1][:2] if False else
               (max_sharpe_performance[1], max_sharpe_performance[0]),
               color=ACCENT, marker="*", s=350,
               edgecolors=INK, linewidths=0.8, label="Maximum Sharpe")

    ax.scatter(min_volatility_performance[1], min_volatility_performance[0],
               color=INK, marker="*", s=350,
               edgecolors=ACCENT, linewidths=0.8, label="Minimum Volatility")

    ax.scatter(max_sharpe_performance_constrained[1],
               max_sharpe_performance_constrained[0],
               color=INK, marker="X", s=220,
               label="Constrained Maximum Sharpe")

    ax.plot(efficient_volatility, efficient_returns,
            color=ACCENT, linewidth=3, label="Efficient Frontier")

    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label("Sharpe Ratio", color=INK, fontweight="bold")
    cbar.ax.yaxis.set_tick_params(color=INK)
    plt.setp(plt.getp(cbar.ax.axes, "yticklabels"), color=INK)
    cbar.outline.set_edgecolor(INK)

    _style_ax(fig, ax, "Monte Carlo Portfolio Simulation",
              "Annualized Volatility", "Expected Annual Return",
              grid_axis=None)
    ax.grid(alpha=0.25, color=INK)  # grid "both" en el original

    ax.legend(facecolor=BG, edgecolor=INK, labelcolor=INK)

    plt.tight_layout()
    plt.show()


# ── 2. Pesos del portafolio (barh) ─────────────────────────────
def plot_weights(weights_df, ticker_col="ticker", weight_col="weight",
                  title="Optimal Portfolio Allocation", figsize=(10, 6)):
    plot_data = weights_df.sort_values(weight_col, ascending=True)

    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(plot_data[ticker_col], plot_data[weight_col], color=ACCENT)

    _style_ax(fig, ax, title, "Portfolio Weight", "Asset",
              grid_axis="x")

    plt.tight_layout()
    plt.show()


# ── 3. Barras genéricas por categoría (asset class / sector) ───
def plot_allocation_bar(df, category_col, weight_col, title,
                         ylabel="Weight", rotation=20, ha="center",
                         figsize=(8, 5)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.bar(df[category_col], df[weight_col], color=ACCENT)

    _style_ax(fig, ax, title, ylabel=ylabel,
              grid_axis="y", tick_rotation=rotation, tick_ha=ha)

    plt.tight_layout()
    plt.show()


# ── 4. Análisis de sensibilidad (subplots) ──────────────────────
def plot_sensitivity(sensitivity_summary,
                      metrics=("Expected Return", "Volatility", "Sharpe Ratio"),
                      figsize=(14, 4)):
    fig, axes = plt.subplots(1, len(metrics), figsize=figsize)
    fig.patch.set_facecolor(BG)

    for ax, metric in zip(axes, metrics):
        ax.set_facecolor(BG)
        ax.bar(sensitivity_summary["Scenario"],
               sensitivity_summary[metric], color=ACCENT)

        _style_ax(fig, ax, metric, grid_axis="y",
                  tick_rotation=30, tick_ha="right", title_size=12)

    plt.tight_layout()
    plt.show()