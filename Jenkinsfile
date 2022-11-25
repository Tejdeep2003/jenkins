pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Tejdeep2003/jenkins.git'
            }
        }
      stage('Provide permissions'){
        steps{
             sh "chmod u+x subtraction.py"
             sh "chmod u+x test.py test1.py test2.py test3.py test4.py test5.py"
        }
      }
        stage('Build Code') {
            steps {
                sh "./subtraction.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "./test.py"
            }
        }
        stage('Test Code1') {
            steps {                
                sh "./test1.py"
            }
        }
        stage('Test Code2') {
            steps {                
                sh "./test2.py"
            }
        }
        stage('Test Code3') {
            steps {
                sh "./test3.py"
            }
        }
        stage('Test Code4') {
            steps {
                sh "./test4.py"
            }
        }
        stage('Test Code5') {
            steps {
                sh "./test5.py"
            }
        }
    } 
}
