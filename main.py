import os
import subprocess
import animation
import time

def main():

    wait = animation.Wait('spinner')
    projectName = input('Enter project name : ')
    projectStructure = [
        'Scenes',
        'Navigations',
        'Components',
        'Styles',
        'Assets',
        'Actions',
        'Constants',
        'Reducers',
        'Stores',
        'Utils'
    ]
    navigations = ['app','auth','tab']
    try:
        print('\nCreating a new react-native project!')
        wait.start()
        initProject = subprocess.Popen(['npx', 'react-native', 'init', projectName],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

        stdout, stderr = initProject.communicate()
        wait.stop()
        if stdout != '':
            print('[ Project ] - ' + projectName + 'Created')
             # Create project structure container
            for i in range(len(projectStructure)):
                os.makedirs(projectName + '/src/' + projectStructure[i])
                path = projectName + '/src/' + projectStructure[i] + '/' + 'index.js'
                open(path, 'w').close()
        
            for i in range(len(navigations)):
                os.makedirs(projectName + '/src/Navigations/' + navigations[i])
                
            subprocess.check_call('tree ' + projectName + '/src', shell=True)
            
            rnative_base = input('Do you want to install native-base? (YES/NO) : ').lower()
            if rnative_base == 'y' or rnative_base == 'yes':
                print('Installing native-base . . . .')
                inative_base = subprocess.Popen(['yarn', '--cwd', projectName, 'add', 'native-base'],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
                stdout, stderr = inative_base.communicate()
                print('[ Native Base ] Successfully installed')
    

            rnavigation = input('Do you want to install react-navigation? (YES/NO) : ').lower()
            if rnavigation == 'y' or rnavigation == 'yes':
                print('Installing react-navigation . . . .')

                wait.start()
                # Installing react navigation native
                irnavigationative = subprocess.Popen(['yarn', '--cwd', projectName, 'add', '@react-navigation/native'],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
                stdout, stderr = irnavigationative.communicate()

                # Installing dependencies into a bare React Native project
                irnavigationdependencies = subprocess.Popen(['yarn', '--cwd', projectName, 'add', 'react-native-gesture-handler react-native-reanimated react-native-screens react-native-safe-area-context @react-native-community/masked-view'],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
                stdout, stderr = irnavigationdependencies.communicate()


                # Installing react navigation stack
                irnavigationstack = subprocess.Popen(['yarn', '--cwd', projectName, 'add', '@react-navigation/native'],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
                stdout, stderr = irnavigationstack.communicate()
                wait.stop()

                print('[ @react-navigation/native ] Successfully installed')
                print('[ @react-navigation/stack ] Successfully installed')
                print('[ react navigation dependencies ] Successfully installed')

    except FileExistsError:
        print("Project " , projectName ,  " already exists")

    

main()