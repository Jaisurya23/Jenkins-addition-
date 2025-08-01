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
                bat '"C:\\Users\\welcome\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m xmlrunner discover -s tests -o test-reports'
            }
        }

        stage('Publish Test Report') {
            steps {
                junit 'test-reports/**/*.xml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished'
        }
    }
}
