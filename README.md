# Portfolio Optimization and Risk Analysis

## Project Overview

This project presents the complete development of an investment portfolio optimization and risk analysis workflow for a fictional client seeking long-term capital appreciation. The analysis combines Modern Portfolio Theory (Markowitz), historical performance evaluation, portfolio risk analysis, and Monte Carlo simulation to support investment decision-making through quantitative methods.

Rather than focusing exclusively on optimization algorithms, the project follows a business-oriented analytical process, emphasizing the interpretation of results, model limitations, and the translation of quantitative findings into actionable investment recommendations.

---

## Business Problem

An investor with an initial capital of **USD 10,000** seeks a data-driven recommendation for constructing a diversified investment portfolio.

The client has the following characteristics:

- Investment horizon: **10 years**
- Initial capital: **USD 10,000**
- High risk tolerance
- Long-term capital growth objective
- Accepts high market volatility
- Reinvests all returns (compound growth)

The challenge is not simply selecting assets with the highest historical returns, but identifying a portfolio that provides an appropriate balance between expected return and risk while remaining aligned with the client's investment profile.

---

## Business Objectives

The primary business objective is to design an investment strategy capable of maximizing long-term capital growth while maintaining a level of risk consistent with an aggressive investor.

More specifically, the project aims to answer the following business questions:

- Which assets should be included in the portfolio?
- How diversified is the proposed portfolio?
- What is the expected return and associated risk?
- How does the portfolio compare against the S&P 500?
- What are the potential losses during adverse market conditions?
- How could the investment evolve over the next ten years?

---

## Analytical Objectives

From an analytical perspective, the project focuses on:

- Building an optimized investment portfolio using Modern Portfolio Theory.
- Evaluating historical portfolio performance.
- Measuring portfolio risk through multiple financial metrics.
- Comparing portfolio performance against a market benchmark (S&P 500).
- Quantifying downside risk using Value at Risk (VaR) and Expected Shortfall (CVaR).
- Simulating future investment scenarios using Monte Carlo methods.
- Translating technical results into business recommendations.

---

## Methodology

The project follows a business-oriented adaptation of the CRISP-DM methodology.

### 1. Business Understanding

- Definition of investor profile
- Investment objectives
- Investment constraints
- Risk tolerance

### 2. Data Understanding

- Selection of investment universe
- Historical price collection
- Data quality verification

### 3. Feature Construction

- Historical returns
- Covariance matrix
- Correlation matrix

### 4. Portfolio Optimization

- Mean-Variance Optimization (Markowitz)
- Maximum Sharpe Portfolio
- Minimum Volatility Portfolio
- Constrained Portfolio Optimization
- Efficient Frontier
- Sensitivity Analysis

### 5. Portfolio Evaluation

- Historical portfolio reconstruction
- CAGR
- Annualized Volatility
- Sharpe Ratio
- Sortino Ratio
- Historical Drawdown
- Benchmark Comparison

### 6. Tail Risk Analysis

- Historical Value at Risk (VaR)
- Expected Shortfall (CVaR)

### 7. Future Scenario Analysis

- Monte Carlo Simulation
- Confidence Intervals
- Probability of Capital Loss

### 8. Business Recommendations

- Portfolio recommendation
- Risk assessment
- Investment considerations
- Model limitations

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- PyPortfolioOpt
- SciPy

---

## Project Structure

```text
portfolio-optimization/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── notebooks/

│   ├── 01_portfolio_optimization.ipynb

│   └── 02_portfolio_risk_analysis.ipynb

│

├── reports/

│   ├── CSV exports

│   ├── Excel report

│   └── Figures

│

├── src/

│

└── README.md
```

---

## Key Results

The optimized portfolio achieved:

- Historical CAGR of approximately **15%**
- Expected long-term capital appreciation consistent with an aggressive investment strategy
- Higher historical return than the S&P 500
- Greater volatility than the benchmark, reflecting the client's risk profile
- Low probability of capital loss over a 10-year investment horizon according to Monte Carlo simulation
- Diversified allocation across multiple industries and asset classes

The project also demonstrates that higher expected returns come at the cost of increased downside risk, highlighting the importance of evaluating both return and risk simultaneously rather than focusing on performance alone.

---

## Main Insights

Several important analytical insights emerged during the project:

- Modern Portfolio Theory is highly sensitive to expected return estimates (Error Maximization).
- Portfolio optimization results should never be accepted without validating model inputs.
- Historical performance does not guarantee future returns.
- Risk metrics such as VaR, CVaR and Maximum Drawdown provide valuable information beyond volatility.
- Monte Carlo simulation should be interpreted as a scenario analysis tool rather than a prediction of future performance.

---

## Limitations

This analysis has several limitations that should be considered:

- Expected returns are estimated from historical data.
- Transaction costs and taxes were not included.
- Portfolio rebalancing was assumed to be static.
- Monte Carlo simulations rely on Geometric Brownian Motion assumptions.
- Financial markets rarely satisfy all statistical assumptions used by the models.

---

## Future Improvements

Potential extensions of this project include:

- Black-Litterman Portfolio Optimization
- Bayesian Shrinkage Models
- Robust Portfolio Optimization
- GARCH-based volatility forecasting
- Bootstrap Monte Carlo Simulation
- Dynamic Portfolio Rebalancing
- Inclusion of transaction costs and taxes
- Stress testing under macroeconomic scenarios

---

## Repository

This project was developed as part of a business analytics portfolio focused on applying quantitative methods to real-world decision-making.

The emphasis of the project is not only on building mathematical models, but on understanding business problems, evaluating model assumptions, interpreting results critically, and communicating actionable recommendations to decision-makers.