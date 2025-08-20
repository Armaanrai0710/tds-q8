import pandas as pd
import matplotlib.pyplot as plt

# Verification email for PR: 24ds2000041@ds.study.iitm.ac.in

INDUSTRY_TARGET = 85.0

def main():
    df = pd.read_csv("data.csv")
    df["retention_rate"] = df["retention_rate"].astype(float)

    avg = df["retention_rate"].mean()
    latest = df.iloc[-1]["retention_rate"]
    gap_to_target_latest = INDUSTRY_TARGET - latest
    gap_to_target_avg = INDUSTRY_TARGET - avg

    print("Quarterly retention rates:")
    print(df.to_string(index=False))
    print("\nAverage retention:", round(avg, 2))
    print("Industry target:", INDUSTRY_TARGET)
    print("Gap to target (latest Q):", round(gap_to_target_latest, 2))
    print("Gap to target (average):", round(gap_to_target_avg, 2))

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(df["quarter"], df["retention_rate"], marker="o", linewidth=2)
    plt.axhline(INDUSTRY_TARGET, linestyle="--")
    plt.title("Customer Retention Rate - 2024 Quarterly")
    plt.xlabel("Quarter")
    plt.ylabel("Retention Rate")
    # Annotate last point and target
    last_q = df["quarter"].iloc[-1]
    plt.text(last_q, latest, f" {latest:.2f}", va="bottom")
    plt.text(df["quarter"].iloc[0], INDUSTRY_TARGET, f" Target {INDUSTRY_TARGET:.0f}", va="bottom")

    plt.tight_layout()
    plt.savefig("chart.png", dpi=150)

if __name__ == "__main__":
    main()
