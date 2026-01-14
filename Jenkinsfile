pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "fase1"
    }

    stages {
        stage('Checkout') {
            steps {
                // Opción más simple para evitar el error de 'scm' [cite: 1]
                checkout scm 
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube-Server') {
                        // Usamos comillas dobles claras para la ruta del scanner
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
         
        stage('Build Image') {
            steps {
                // Usamos comillas simples para el comando estático y evitamos caracteres extra [cite: 2]
                sh "docker build -t ${env.IMAGE_NAME}:latest ."
            }
        }

        stage('Run Container') {
            steps {
                // Limpiamos el comando run para que sea una sola línea simple [cite: 3, 4]
                sh "docker rm -f test-container || true"
                sh "docker run --name test-container -d ${env.IMAGE_NAME}:latest"
            }
        }
    }
}
