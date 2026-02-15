import pandas as pd

# Load the data
df = pd.read_csv('apple-stock-prices-from-20102017.csv')

print(f"Total rows: {len(df)}")

# Calculate split point (70% train, 30% test)
split_index = int(len(df) * 0.7)

# Split the data sequentially (important for time series)
train_data = df[:split_index]
test_data = df[split_index:]

print(f"Training set: {len(train_data)} rows ({len(train_data)/len(df)*100:.1f}%)")
print(f"Test set: {len(test_data)} rows ({len(test_data)/len(df)*100:.1f}%)")

# Save to separate CSV files
train_data.to_csv('apple_train.csv', index=False)
test_data.to_csv('apple_test.csv', index=False)

print("\n✅ Data split complete!")
print("   - apple_train.csv created")
print("   - apple_test.csv created")

# Display date ranges
print(f"\nTraining period: {train_data.iloc[0]['Date']} to {train_data.iloc[-1]['Date']}")
print(f"Test period: {test_data.iloc[0]['Date']} to {test_data.iloc[-1]['Date']}")
