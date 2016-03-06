from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://localhost:8080'
    server = Jenkins(jenkins_url)
    return server

print "jenkins version:",get_server_instance().version
