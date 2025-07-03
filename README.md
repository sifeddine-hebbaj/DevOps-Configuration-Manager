# DevOps Configuration Manager

Un projet complet de gestion de configuration DevOps avec pipeline CI/CD automatisé.

## 📋 Vue d'ensemble

Ce projet démontre une approche moderne de DevOps avec :
- **Backend Python** pour la génération de configurations Docker/Kubernetes
- **Frontend React** pour l'interface utilisateur
- **Pipeline Jenkins** pour l'automatisation CI/CD
- **Docker** pour la conteneurisation
- **Kubernetes** pour l'orchestration

## 🏗️ Architecture

```
DevOps-Configuration-Manager/
├── backend/                 # API Python + générateurs de config
│   ├── app.py              # Application Flask
│   ├── generate_compose.py # Générateur Docker Compose
│   ├── requirements.txt    # Dépendances Python
│   └── Dockerfile         # Image Docker backend
├── frontend/               # Interface React
│   ├── src/               # Code source React
│   ├── package.json       # Dépendances Node.js
│   └── Dockerfile         # Image Docker frontend
└── Jenkinsfile            # Pipeline CI/CD Jenkins
```

## 🚀 Étapes du Pipeline Jenkins

### 1. **Checkout** 
- Récupération du code source depuis Git
- Branche : `main`

### 2. **Debug User & Docker**
- Vérification de l'utilisateur Jenkins
- Contrôle de la version Docker Compose
- Diagnostic de l'environnement

### 3. **Backend - Install & Test**
- Installation des dépendances Python (`requirements.txt`)
- Vérification de l'environnement Python
- Tests backend (actuellement désactivés)

### 4. **Frontend - Install & Test**
- Installation des dépendances Node.js (`npm install`)
- Tests frontend (actuellement désactivés)

### 5. **Generate Docker Compose YAML**
- Exécution du script `generate_compose.py`
- Génération automatique du fichier `docker-compose.yml`
- Sortie : `backend/generated_yamls/docker-compose.yml`

### 6. **Build Docker Images**
- Construction des images Docker
- Utilisation du fichier généré `docker-compose.yml`
- Images créées : backend et frontend

### 7. **Run Docker Containers**
- Démarrage des conteneurs en mode détaché
- Services accessibles via les ports configurés

### 8. **Fin du pipeline**
- Confirmation de l'exécution réussie
- Message de fin : "Pipeline terminé avec succès !"

## 🔧 Configuration DevOps

### Prérequis
- **Jenkins** avec plugins Pipeline
- **Docker Desktop** installé et configuré
- **Python 3.x** et **Node.js** sur l'agent Jenkins
- **Git** pour le versioning

### Variables d'environnement Jenkins
```bash
PATH=C:\Program Files\Docker\Docker\resources\bin;${env.PATH}
```

### Structure des fichiers générés
```
backend/generated_yamls/
├── docker-compose.yml     # Configuration Docker Compose
└── kubernetes.yml         # Configuration Kubernetes (futur)
```

## 📁 Détail des composants

### Backend (Python/Flask)
- **Générateur de configurations** : Transforme les spécifications en fichiers Docker/Kubernetes
- **API REST** : Interface pour la gestion des configurations
- **Validation XML** : Vérification des schémas de configuration

## 🔧 Système XML/XSLT/XSD

### Architecture de transformation
Le projet utilise un système de transformation XML pour générer automatiquement les configurations Docker et Kubernetes :

```
XML Config → XSLT Transformation → Docker Compose / Kubernetes YAML
```

### Fichiers de configuration

#### `config.xml` - Configuration principale
```xml
<config>
  <environments>
    <environment name="dev">
      <container>
        <name>web-app</name>
        <image>nginx:latest</image>
        <ports>8080</ports>
      </container>
    </environment>
  </environments>
</config>
```

#### `config.xsd` - Schéma de validation
- **Validation structurelle** : Définit la structure autorisée des fichiers XML
- **Types de données** : Contrôle les types de valeurs (string, integer, etc.)
- **Contraintes** : Assure la cohérence des configurations

#### `test.xml` - Fichier de test
- **Exemple de configuration** : Démonstration de l'utilisation
- **Validation** : Test du schéma XSD
- **Conteneurs** : web-app (nginx) et sql-db (mysql)

### Transformations XSLT

#### `xml2dockercompose.xslt` - Génération Docker Compose
```xml
<xsl:template match="container">
  <xsl:value-of select="name"/>:
    image: <xsl:value-of select="image"/>
    ports:
      - <xsl:value-of select="ports"/>
</xsl:template>
```

**Sortie générée :**
```yaml
services:
  web-app:
    image: nginx:latest
    ports:
      - 8080
  sql-db:
    image: mysql:8.0
    ports:
      - 3306
```

#### `xml2kubernetes.xslt` - Génération Kubernetes
```xml
<xsl:template match="container">
  - name: <xsl:value-of select="name"/>
    image: <xsl:value-of select="image"/>
    ports:
      - containerPort: <xsl:value-of select="ports"/>
</xsl:template>
```

**Sortie générée :**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: web-app
        image: nginx:latest
        ports:
          - containerPort: 8080
```

### Workflow de transformation

1. **Édition** : Modification du fichier `config.xml`
2. **Validation** : Vérification avec `config.xsd`
3. **Transformation** : Application des templates XSLT
4. **Génération** : Création des fichiers YAML
5. **Déploiement** : Utilisation par Docker/Kubernetes

### Avantages du système XML/XSLT

- **Séparation des préoccupations** : Configuration ≠ Génération
- **Réutilisabilité** : Un XML → Plusieurs formats (Docker, K8s)
- **Validation** : Schéma XSD pour la cohérence
- **Maintenabilité** : Modifications centralisées
- **Extensibilité** : Ajout facile de nouveaux formats

### Frontend (React)
- **Interface utilisateur moderne** : Dashboard pour la gestion des configurations
- **Responsive design** : Compatible desktop et mobile
- **Intégration API** : Communication avec le backend

### Pipeline Jenkins
- **Automatisation complète** : De la récupération du code au déploiement
- **Gestion des erreurs** : Vérifications à chaque étape
- **Logs détaillés** : Traçabilité complète du processus

## 🚦 Workflow DevOps

1. **Développement** → Code dans Git
2. **Intégration** → Pipeline Jenkins automatique
3. **Tests** → Validation des composants
4. **Build** → Construction des images Docker
5. **Déploiement** → Lancement des conteneurs
6. **Monitoring** → Surveillance des services

## 🔍 Dépannage

### Problèmes courants
- **"Waiting for next available executor"** : Aucun agent Jenkins disponible
- **"Stage Name est vide"** : Pipeline non exécuté, relancer depuis le début
- **Erreur Docker** : Vérifier l'installation et les permissions Docker

### Commandes utiles
```bash
# Vérifier l'état Jenkins
docker ps | grep jenkins

# Logs du pipeline
tail -f /var/log/jenkins/jenkins.log

# Vérifier les conteneurs
docker compose -f backend/generated_yamls/docker-compose.yml ps
```

## 📈 Évolutions futures

- [ ] Tests automatisés (unitaires et intégration)
- [ ] Déploiement Kubernetes
- [ ] Monitoring et alerting
- [ ] Sécurité et secrets management
- [ ] Multi-environnements (dev, staging, prod)

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

---

**Auteur** : SIF-EDDINE HEBBAJ  
**Version** : 1.0.0  
**Dernière mise à jour** : 2024 
