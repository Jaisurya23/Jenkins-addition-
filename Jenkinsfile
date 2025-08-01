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
                bat '"C:\\Users\\welcome\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" add.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '"C:\\Users\\welcome\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" test_add.py'
            }
        }
    }
    stage('Publish Test Report') {
            steps {
                junit 'test-reports/**/*.xml'
            }
        }
}



 