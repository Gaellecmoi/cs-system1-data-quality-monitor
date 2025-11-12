"""
Système 1 : Marketing Data Quality Monitor
Détection proactive d'anomalies de tracking
"""

import anthropic
import os
from dotenv import load_dotenv

# Configuration
load_dotenv()
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def simulate_client_events():
    """Simule 7 jours d'events avec anomalie jour 7"""
    return [
        {"date": "2024-11-04", "event": "page_view", "count": 1200, "client": "Acme E-commerce"},
        {"date": "2024-11-05", "event": "page_view", "count": 1150, "client": "Acme E-commerce"},
        {"date": "2024-11-06", "event": "page_view", "count": 1180, "client": "Acme E-commerce"},
        {"date": "2024-11-07", "event": "page_view", "count": 1220, "client": "Acme E-commerce"},
        {"date": "2024-11-08", "event": "page_view", "count": 1190, "client": "Acme E-commerce"},
        {"date": "2024-11-09", "event": "page_view", "count": 1210, "client": "Acme E-commerce"},
        {"date": "2024-11-10", "event": "page_view", "count": 600, "client": "Acme E-commerce"},  # ANOMALIE
    ]

def detect_anomaly(events, threshold=-30):
    """Détecte baisse >30% vs baseline"""
    if len(events) < 2:
        return None
    
    baseline_avg = sum([e["count"] for e in events[:-1]]) / len(events[:-1])
    last_count = events[-1]["count"]
    variation_pct = ((last_count - baseline_avg) / baseline_avg) * 100
    
    if variation_pct < threshold:
        return {
            "client": events[-1]["client"],
            "event": events[-1]["event"],
            "date": events[-1]["date"],
            "baseline_avg": round(baseline_avg, 0),
            "last_count": last_count,
            "variation_pct": round(variation_pct, 1),
            "severity": "HIGH" if variation_pct < -50 else "MEDIUM"
        }
    return None

def generate_diagnosis(anomaly):
    """Claude génère diagnostic + troubleshooting"""
    prompt = f"""You are a CS automation system for a B2B SaaS analytics platform.

ANOMALY DETECTED:
- Client: {anomaly['client']}
- Event: {anomaly['event']}
- Date: {anomaly['date']}
- Baseline: {anomaly['baseline_avg']:.0f} events/day
- Yesterday: {anomaly['last_count']} events
- Change: {anomaly['variation_pct']}%

Generate a diagnostic email for the CSM:

Subject: [Urgent] Data Quality Alert - {anomaly['client']}

**Summary:** (2 sentences)

**Most Likely Causes:**
1. [Cause 1]
2. [Cause 2]
3. [Cause 3]

**Recommended Actions:**
1. [Action]
2. [Action]
3. [Action]

Keep it concise and actionable."""

    message = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def main():
    print("=" * 70)
    print("  SYSTÈME 1 : MARKETING DATA QUALITY MONITOR")
    print("=" * 70)
    print()
    
    print("📊 [1/4] Loading client data...")
    events = simulate_client_events()
    print(f"    ✓ Loaded {len(events)} days of data")
    print()
    
    print("🔍 [2/4] Analyzing for anomalies...")
    anomaly = detect_anomaly(events)
    
    if not anomaly:
        print("    ✓ No anomalies detected")
        return
    
    print(f"    ⚠️  ANOMALY DETECTED!")
    print(f"       Date: {anomaly['date']}")
    print(f"       Baseline: {anomaly['baseline_avg']:.0f} events/day")
    print(f"       Yesterday: {anomaly['last_count']} events")
    print(f"       Change: {anomaly['variation_pct']}%")
    print()
    
    print("🤖 [3/4] Generating diagnostic...")
    diagnosis = generate_diagnosis(anomaly)
    print("    ✓ Done")
    print()
    
    print("=" * 70)
    print("📧 [4/4] ALERT EMAIL FOR CSM")
    print("=" * 70)
    print()
    print(diagnosis)
    print()
    print("=" * 70)

if __name__ == "__main__":
    main()