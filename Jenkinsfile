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
            emailext(
                subject: "Build ${env.JOB_NAME} #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: """
                Hi Team,

                Job Name: ${env.JOB_NAME}
                Build Number: ${env.BUILD_NUMBER}
                Status: ${currentBuild.currentResult}
                URL: ${env.BUILD_URL}

                Regards,
                Jenkins
                """,
                from: 'jaisuryafirerockers@gmail.com',
                to: 'jaisuryafirerockers@gmail.com'
            )
            echo 'Email notification sent.'
            echo 'Successfully completed the pipeline.'
        }
    }
}
