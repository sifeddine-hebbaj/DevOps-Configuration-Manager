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
                    bat 'pip install -r requirements.txt'
                    bat 'echo No backend tests configured'
                }
            }
        }
        stage('Frontend - Install & Test') {
            steps {
                dir('frontend') {
                    bat 'npm install'
                    bat 'echo No frontend tests configured'
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                bat 'docker-compose build'
            }
        }
    }
} 