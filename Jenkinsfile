pipeline {
    agent any
    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Run Tests on Python 3.12 and 3.13') {
            parallel {
                stage('Python 3.12 Tests') {
                    agent {
                        docker { image 'python:3.12' }
                    }
                    steps {
                        script {
                            sh '''
                                python3.12 -m venv .venv12
                                . .venv12/bin/activate
                                pip install -r requirements.txt
                                pytest --html=report_312.html --self-contained-html
                            '''
                        }
                    }
                    post {
                        always {
                            // Archive the HTML report as an artifact
                            archiveArtifacts artifacts: 'report_312.html', allowEmptyArchive: true

                            // Publish HTML report using the HTML Publisher Plugin
                            publishHTML(target: [
                                reportName: 'Python 3.12 Test Report',
                                reportDir: '.',  // Path to report file
                                reportFiles: 'report_312.html',  // Name of the HTML report file
                                keepAll: true,  // Keep all reports for all builds
                                alwaysLinkToLatest: true,  // Link to the latest report
                                allowExternal: true  // Allow external scripts to be run (if applicable)
                            ])
                        }
                    }
                }

                stage('Python 3.13 Tests') {
                    agent {
                        docker { image 'python:3.13' }
                    }
                    steps {
                        script {
                            sh '''
                                python3.13 -m venv .venv13
                                . .venv13/bin/activate
                                pip install -r requirements.txt
                                pytest --html=report_313.html --self-contained-html
                            '''
                        }
                    }
                    post {
                        always {
                            // Archive the HTML report as an artifact
                            archiveArtifacts artifacts: 'report_313.html', allowEmptyArchive: true

                            // Publish HTML report using the HTML Publisher Plugin
                            publishHTML(target: [
                                reportName: 'Python 3.13 Test Report',
                                reportDir: '.',  // Path to report file
                                reportFiles: 'report_313.html',  // Name of the HTML report file
                                keepAll: true,  // Keep all reports for all builds
                                alwaysLinkToLatest: true,  // Link to the latest report
                                allowExternal: true  // Allow external scripts to be run (if applicable)
                            ])
                        }
                    }
                }
            }
        }
    }
}
