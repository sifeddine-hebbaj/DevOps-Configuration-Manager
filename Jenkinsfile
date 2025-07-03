pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Backend - Install & Test') {
            steps {
                dir('backend') {
                    sh 'pip install -r requirements.txt'
                    // Remplace par la commande de test réelle si besoin
                    sh 'echo "No backend tests configured"'
                }
            }
        }
        stage('Frontend - Install & Test') {
            steps {
                dir('frontend') {
                    sh 'npm install'
                    // Remplace par la commande de test réelle si besoin
                    sh 'echo "No frontend tests configured"'
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }
    }
} 