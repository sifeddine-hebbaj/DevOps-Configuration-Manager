pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Debug User & Docker') {
            steps {
                bat 'whoami'
                bat 'docker compose --version'
            }
        }
        stage('Backend - Install & Test') {
            steps {
                dir('backend') {
                    bat 'where py'
                    bat 'py --version'
                    bat 'py -m pip --version'
                    bat 'py -m pip install -r requirements.txt'
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
        stage('Generate Docker Compose YAML') {
            steps {
                dir('backend') {
                    bat 'py generate_compose.py'
                }
            }
        }
        stage('Build Docker Images') {
            steps {
                script {
                    def dockerPath = 'C:\\Program Files\\Docker\\Docker\\resources\\bin'
                    def composeFile = 'backend/generated_yamls/docker-compose.yml'
                    withEnv(["PATH=${dockerPath};${env.PATH}"]) {
                        bat 'docker compose --version'
                        bat "if not exist ${composeFile} echo ERROR: File ${composeFile} not found! && exit 1"
                        bat "docker compose -f ${composeFile} build"
                    }
                }
            }
        }
    }
} 