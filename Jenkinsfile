pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run ETL Tests') {
            steps {
                bat 'pytest -s'
            }
        }
    }

    post {
        success {
            echo 'ETL validation PASSED'
        }
        failure {
            echo 'ETL validation FAILED'
        }
    }
}
