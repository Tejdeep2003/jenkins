pipeline{
agent any
    stages{
        stage('clone'){
            steps{
                git 'https://github.com/Tejdeep2003/jenkins.git'
            }
        }
        stage('Build'){
            steps{
                sh "chmod u+x Prog1.py"
                sh "./Prog1.py"
            }
        }
        stage('Test'){
            steps{
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    }
}
