pipeline {
    agent {
        docker {
            args '-u root:root'
        }
    }
    stages {
        parallel {
                stage('Python 3.12 Tests') {
                    agent {
                        docker { image 'python:3.12' }
                    }
                    steps {
                        script {
                            sh 'python3.12 -m venv12 .venv'
                            sh '. .venv/bin/activate'
                            sh 'pip install -r requirements.txt'
                            sh 'pytest --html=report_313.html --self-contained-html'
                        }
                    }
                }

                stage('Python 3.13 Tests') {
                    agent {
                        docker { image 'python:3.13' }
                    }
                    steps {
                        script {

                            sh 'python3.13 -m venv13 .venv'
                            sh '. .venv/bin/activate'
                            sh 'pip install -r requirements.txt'
                            sh 'pytest --html=report_313.html --self-contained-html'
                        }
                    }
                }
        }
    }
}
