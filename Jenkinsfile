pipeline {
    agent any
    
    environment {
        // Definimos el nombre de la imagen para usarlo en varias etapas
        IMAGE_NAME = "fase1" [cite: 1]
    }

    stages {
        stage('Checkout') {
            steps {
                // Descarga del código fuente desde el repositorio configurado
                checkout scm [cite: 1]
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Localiza la herramienta SonarScanner en el servidor Jenkins
                    def scannerHome = tool 'SonarScanner' [cite: 3]
                    
                    // Ejecuta el análisis usando el servidor configurado y tus parámetros específicos
                    withSonarQubeEnv('SonarQube-Server') { [cite: 4]
                        sh "${scannerHome}/bin/sonar-scanner \
                          -Dsonar.projectKey=Jenkins \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://localhost:9100 \
                          -Dsonar.login=squ_925bd641615fa8749e0d005b16317695e31bc541"
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                // Jenkins detendrá el pipeline si SonarQube determina que el código no es apto
                timeout(time: 5, unit: 'MINUTES') { [cite: 5]
                    waitForQualityGate abortPipeline: true [cite: 5]
                }
            }
        }
         
        stage('Build Image') {
            steps {
                // Construcción de la imagen Docker utilizando la variable de entorno
                sh "docker build -t ${IMAGE_NAME}:latest ." [cite: 6, 7]
            }
        }

        stage('Run Container') {
            steps {
                // Limpieza de contenedores previos para evitar conflictos de nombre
                sh "docker rm -f test-container || true" [cite: 8]
                // Despliegue del nuevo contenedor basado en la imagen construida
                sh "docker run --name test-container -d ${IMAGE_NAME}:latest" [cite: 8]
            }
        }
    }
}
