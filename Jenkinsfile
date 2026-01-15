pipeline {
    agent any
    
    environment {
        // Definimos la variable sin caracteres especiales problemáticos
        IMAGE_NAME = "fase1"
    }

    stages {
        stage('Checkout') {
            steps {
                // Descarga el código del repositorio 
                checkout scm 
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Localizamos la herramienta configurada en Jenkins
                    def scannerHome = tool 'SonarScanner'
                    
                    // Ejecución con los parámetros de tu servidor local
                    withSonarQubeEnv('SonarQube-Server') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=Jenkins \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://sonarqube:9000 \
                            -Dsonar.login=squ_925bd641615fa8749e0d005b16317695e31bc541"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // Se envuelve en un bloque script para asegurar que waitForQualityGate funcione bien
                script {
                    timeout(time: 5, unit: 'MINUTES') {
                        waitForQualityGate abortPipeline: true
                    }
                }
            }
        }
         
        stage('Build Image') {
            steps {
                // Construcción de la imagen Docker 
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Run Container') {
            steps {
                // Gestión del contenedor para evitar conflictos
                sh "docker rm -f test-container || true"
                sh "docker run --name test-container -d ${IMAGE_NAME}:latest"
            }
        }
    }
}
