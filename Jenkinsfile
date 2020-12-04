pipeline {
    agent any

    stages {
        stage('Ansible') {
            steps {
                echo 'Running Playbook..'
                sh ". ./scripts/run_playbook.sh"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh ". ./scripts/test.sh"
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                sh ". ./scripts/build.sh"
            }
        }
        stage('Push') {
            steps {
                echo 'Pushing....'
                sh ". ./scripts/push.sh"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh ". ./scripts/deploy.sh"
            }
        }
    }
}