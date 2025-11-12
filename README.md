# CS System 1: Marketing Data Quality Monitor

## 🎯 Problème résolu

Les plateformes B2B SaaS Marketing/Analytics (Segment, Mixpanel, Amplitude) dépendent d'un tracking précis. Quand le tracking casse (pixel mal configuré, tag supprimé), les dashboards clients deviennent incorrects.

**Impact :** Les clients découvrent le problème 3-7 jours plus tard, déjà frustrés. La confiance est érodée.

**Cette solution :** Détection proactive des anomalies en 24h, avec alerte automatique au CSM avant que le client ne s'en aperçoive.

---

## 💡 Comment ça fonctionne

**1. Monitoring continu**  
Analyse du volume d'events sur une fenêtre glissante de 7 jours.

**2. Détection intelligente**  
Identification des variations anormales avec 2 niveaux de sévérité :
- **MEDIUM** : Baisse entre 30-45% vs baseline → Investigation sous 24h
- **HIGH** : Baisse >45% vs baseline → Action immédiate (2h)

**3. Diagnostic automatisé**  
Claude API génère un email structuré pour le CSM avec :
- Root cause analysis
- Actions recommandées
- Niveau d'urgence adapté (MEDIUM / HIGH)

**4. Escalade proactive**  
Le CSM peut contacter le client avant qu'il ne découvre le problème.

---

## 🛠️ Stack technique

- **Python 3.x** - Logique de détection
- **Claude API (Haiku)** - Génération diagnostics
- **Analyse statistique** - Comparaison baseline vs temps réel

---

## 📊 Impact projeté

- **85%** des problèmes de data quality détectés avant escalation client
- **+40%** satisfaction client (problèmes résolus de manière proactive)
- **-60%** temps de résolution (contexte clair dès l'alerte)

---

## 🚀 Installation
```bash
# Cloner le repo
git clone https://github.com/username/cs-system1-data-quality-monitor.git
cd cs-system1-data-quality-monitor

# Setup environnement
python -m venv venv
.\venv\Scripts\activate          # Windows
# source venv/bin/activate       # Mac/Linux

# Installer dépendances
pip install -r requirements.txt

# Configurer clé API
echo "ANTHROPIC_API_KEY=your_key" > .env
```

---

## 💻 Utilisation
```bash
# Mode aléatoire (simulation différents scénarios)
python monitor.py

# Ou scénario spécifique
python monitor.py normal    # Pas d'anomalie
python monitor.py medium    # Anomalie modérée (-30 à -45%)
python monitor.py high      # Anomalie critique (>-45%)
```

---

## 📹 Démo

[▶️ Voir la démo (3 min)](https://www.loom.com/share/0c65f48ccebf4cb08c744e9962259489)

---

## 🎓 Contexte

Projet portfolio démontrant l'automatisation des opérations Customer Success pour scale-ups B2B SaaS (Marketing/Commerce Tech).

**Auteur :** [Ton nom]  
**LinkedIn :** [Lien]  
**Portfolio :** [Lien Notion]

---

*Note : MVP de validation. Une version production nécessiterait gestion d'erreurs avancée, logging structuré, et monitoring système.*
