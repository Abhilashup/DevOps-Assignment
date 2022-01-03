pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'C:/ProgramData/Jenkins/.jenkins/workspace/Assignment/calc.py'
            }
        }
        stage('test') {
            steps {
                sh 'C:/ProgramData/Jenkins/.jenkins/workspace/Assignment/test_calc.py'
            }
        }
    }
}
