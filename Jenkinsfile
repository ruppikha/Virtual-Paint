pipeline {
    agent any

    environment {
        NAME_VAR = ""
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Hello World'
                sh "git --version"
                sh "python3 --version"
                git branch: 'python-add-arrays', url: 'https://github.com/ruppikha/test.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install numpy pandas'
            }
        }
        
        stage('Get Input') {
            steps {
                script {
                    timeout(time: 60, unit: 'SECONDS') {
                        NAME_VAR = input message: 'Enter name:', parameters: [string(description: 'hi', name: 'name_var')]
                    }
                }

                echo "Name entered: ${NAME_VAR}"
            }
        }
        stage('Running application') {
            steps {
                sh "pwd"
                sh "python3 main.py ${NAME_VAR}"
            }
        }
        
        stage('Test Application') {
            steps {
                script {
                    if (NAME_VAR ==~ /^[a-zA-Z]{3,}$/) {
                        echo 'Name is valid.'
                    } else {
                        error 'Name is not valid. Pipeline will stop.'
                    }
                }
            }
        }
        
        stage('Commit and Push') {
            steps {
                script {
                    sh """
                        git config user.name "ruppikha"
                        git config user.email "ruppikha@gmail.com"
                        git add docs/index.html
                        git commit -m 'Update output with name ${NAME_VAR}'
                        git push origin python-add-arrays
                    """
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
