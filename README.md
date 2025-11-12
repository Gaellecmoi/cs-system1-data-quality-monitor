# CS System 1: Marketing Data Quality Monitor

## Objectif

Détection proactive d'anomalies de qualité de données pour plateformes B2B SaaS Marketing/Analytics.

## Problème résolu

Les clients de plateformes analytics (type Segment, Mixpanel) ont des problèmes de tracking (pixel cassé, tag supprimé). Leurs dashboards deviennent faux mais ils ne le voient que 3-7 jours plus tard.

**Ce système détecte les anomalies en 24h et alerte le CSM proactivement.**

## Fonctionnement

1. Analyse volume events sur 7 jours
2. Détecte baisse >30% vs baseline
3. Claude API génère diagnostic + troubleshooting
4. Email automatique pour CSM

## Stack

- Python 3.x
- Claude API (Haiku)
- Détection statistique simple

## Installation
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
echo "ANTHROPIC_API_KEY=your_key" > .env
```

## Utilisation
```bash
python monitor.py
```

## Impact projeté

- 85% problèmes détectés avant escalation client
- Satisfaction +40%
- Temps résolution -60%