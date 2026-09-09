pipeline {
    agent any

    environment {
        CI = 'true'
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Preparar Entorno') {
            steps {
                echo 'Validando instalación de Python y Git...'
                // En Windows usar bat, en Linux/Mac usar sh
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                echo 'Instalando librerías desde requirements.txt...'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas BDD') {
            steps {
                echo 'Corriendo escenarios de Behave...'
                // Se asegura la salida limpia y generación de resultados
                bat 'behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results features/'
            }
        }

        stage('Generar Reporte Visual') {
            steps {
                echo 'Procesando resultados JSON a reporte HTML...'
                bat 'python generar_reporte.py'
            }
        }
    }

    post {
        always {
            echo 'Archivando evidencias de la ejecución...'
            archiveArtifacts artifacts: 'reports/reporte.html, reports/allure-results/*', allowEmptyArchive: true
        }
        failure {
            echo 'La ejecución contiene escenarios fallidos.'
        }
        success {
            echo 'Todos los escenarios BDD concluyeron con éxito.'
        }
    }
}