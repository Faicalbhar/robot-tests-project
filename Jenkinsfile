pipeline {
    agent any
    stages {
        stage('Run Tests') {
            steps {
                bat 'python run_tests.py'
            }
        }
        stage('Parse Results') {
            steps {
                bat 'python parse_results.py'
            }
        }
        stage('Analyse IA') {
            steps {
                bat 'python gpt_analysis.py'
            }
        }
        stage('Create JIRA Tickets') {
            steps {
                bat 'python create_jira_ticket.py'
            }
        }
    }
}
