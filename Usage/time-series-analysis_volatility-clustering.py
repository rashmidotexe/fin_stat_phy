from statsmodels.graphics.tsaplots import plot_acf

# Assuming 'price' column in order_flow_data
price_data = order_flow_data['price']
returns = price_data.pct_change().dropna()

plot_acf(returns**2)
plt.show()
