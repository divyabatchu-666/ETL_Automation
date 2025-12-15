pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                C:\\Users\\divya\\PycharmProjects\\ETL_Automation\\.venv\\Scripts\\pip.exe install -r requirements.txt
                '''
            }
        }

        stage('Run ETL Tests') {
            steps {
                bat '''
                C:\\Users\\divya\\PycharmProjects\\ETL_Automation\\.venv\\Scripts\\pytest.exe -s tests/test_select_from_emp.py
                '''
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
