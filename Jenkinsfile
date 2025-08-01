pipeline {
    agent any

    stages {
        stage('Check Python Version') {
            steps {
                bat '"C:\\Users\\welcome\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
            }
        }

        stage('Run Addition Script') {
            steps {
                bat '"C:\\Users\\welcome\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" addition.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '"C:\\Users\\welcome\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" test_addition.py'
            }
        }
    }
}


    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }

