def fit_linear_regression(x_values, y_values):
    sample_count = len(x_values)
    x_mean = sum(x_values) / sample_count
    y_mean = sum(y_values) / sample_count

    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    denominator = sum((x - x_mean) ** 2 for x in x_values)

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    return intercept, slope


def predict(x_value, parameters):
    intercept, slope = parameters
    return intercept + slope * x_value


if __name__ == "__main__":
    gdp_per_capita = [757.0, 11471.0, 12387.0, 19432.0, 27325.0, 34344.0, 42557.0, 52114.0]
    life_satisfaction = [4.2, 5.8, 5.6, 6.4, 6.9, 7.1, 7.3, 7.6]

    theta = fit_linear_regression(gdp_per_capita, life_satisfaction)
    cyprus_gdp_per_capita = 22587.0
    predicted_life_satisfaction = predict(cyprus_gdp_per_capita, theta)

    print(f"Model parameters: intercept={theta[0]:.4f}, slope={theta[1]:.8f}")
    print(
        "Predicted life satisfaction for GDP per capita "
        f"{cyprus_gdp_per_capita:.0f}: {predicted_life_satisfaction:.2f}"
    )
