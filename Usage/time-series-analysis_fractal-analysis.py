import numpy as np

def compute_RS(ts, tau):
    """Compute rescaled range R/S for time series ts and time lag tau."""
    # Split the time series into subsets of size tau
    subsets = np.array_split(ts, len(ts) // tau)
    
    RS_values = []
    for subset in subsets:
        mean_val = np.mean(subset)
        
        # Compute the cumulative deviation from the mean
        cum_dev = np.cumsum(subset - mean_val)
        
        # Compute the range R
        R = max(cum_dev) - min(cum_dev)
        
        # Compute the standard deviation S
        S = np.std(subset)
        
        RS = R / S
        RS_values.append(RS)
    
    return np.mean(RS_values)

def hurst_exponent(ts, max_lag=20):
    """Compute the Hurst exponent for time series ts."""
    lags = range(2, max_lag)
    RS_vals = [compute_RS(ts, lag) for lag in lags]
    
    # Use the slope of the log-log plot as an estimate for the Hurst exponent
    return np.polyfit(np.log(lags), np.log(RS_vals), 1)[0]

# Sample time series data
ts = np.cumsum(np.random.randn(1000))

# Compute the Hurst Exponent
H = hurst_exponent(ts)
print(f"Hurst Exponent: {H}")

