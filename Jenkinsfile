pipeline {
    agent any
    
    environment {
        // Definimos el nombre de la imagen para usarlo en varias etapas
        IMAGE_NAME = "fase1"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm [cite: 1]
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Invocamos la herramienta que configuraste en Jenkins
                    def scannerHome = tool 'SonarScanner'
                    
                    // Usamos el entorno del servidor SonarQube-Server
                    withSonarQubeEnv('SonarQube-Server') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // Jenkins espera a que SonarQube dé el visto bueno
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
         
        stage('Build Image') {
            steps {
                // Usamos variables para que sea más limpio
                sh "docker build -t ${IMAGE_NAME}:latest ." [cite: 2]
            }
        }

        stage('Run Container') {
            steps {
                // Eliminamos cualquier contenedor previo con el mismo nombre para evitar errores
                sh "docker rm -f test-container || true"
                sh "docker run --name test-container -d ${IMAGE_NAME}:latest" [cite: 4]
            }
        }
    }
}
