try:

    import os
    import sys
    from zipfile import ZipFile
    import os
    from os.path import basename
    from sys import platform
    import zipfile
    import requests
except Exception as e:
    print("Error : {} ".format(e))


class ShellExecutor(object):

    @staticmethod
    def execute(command='echo hello'):
        executor = os.popen(command).read()
        return executor


class Tree(object):
    @staticmethod
    def remove(target):
        for d in os.listdir(target):
            try:
                Tree.remove(target + '/' + d)
            except OSError:
                os.remove(target + '/' + d)

        os.rmdir(target)


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))


def main():
    print("\n")
    print("="*55)
    print("Open Source Library to Generate Deployment Package for AWS Lambda  ")
    print("="*55)
    print("\n")

    _PIP = 'pip3'
    print("-"*55)
    pythonVersion = input("Enter Python Version you are using for your AWS  Lambda on  ie 3.6 or 3.8: ")
    print("-"*55)
    packageName = input("Please Enter Package Name for which you want to create a AWS Layers ie requests : ")
    print("-"*55)

    try:

        # =============================================
        #       Step 1 : Delete the Tree if exists
        # =============================================
        try:Tree.remove(target='build')
        except Exception as e: pass

        # =============================================
        #       Step 2 : Create a Directory Structure
        # =============================================
        try:
            dir = "build/python/lib/python{}/site-packages".format(pythonVersion)
            os.makedirs(os.path.join(os.getcwd(), dir))
        except Exception as e:
            pass

        # ============================================================
        #       Step 3 : Check Platform and Install Dependencies
        # ============================================================
        if platform.__str__() == "linux" or platform == "linux2":

            print('-'*55)
            dir = "build/python/lib/python{}/site-packages".format(pythonVersion)
            print("Your System is linux ")
            _shell = "{} install  {} -t {} --system ".format(_PIP, packageName, dir)
            print(_shell)
            res = ShellExecutor.execute(command="pip3 install  {} -t {}  ".format(packageName, dir))
            print(res)
            print('-'*55)

        elif platform.__str__() == "darwin":

            print('-'*55)
            dir = "build/python/lib/python{}/site-packages".format(pythonVersion)
            print("Your System is darwin ")
            _shell = "{} install  {} -t {} --system ".format(_PIP, packageName, dir)
            print(_shell)
            res = ShellExecutor.execute(command="pip3 install  {} -t {}  ".format(packageName, dir))
            print(res)
            print('-'*55)

        elif platform.__str__() == "win32":

            print('-'*55)
            dir = "build/python/lib/python{}/site-packages".format(pythonVersion)
            print("Your System is windows ")
            _shell = "{} install  {} -t {}  ".format(_PIP, packageName, dir)
            print(_shell)
            res = ShellExecutor.execute(command= "pip3 install  {} -t {}  ".format(packageName, dir))
            print(res)
            print('-'*55)


        # ============================================================
        #       Step 4 : Change Directory
        # ============================================================
        os.chdir(os.path.join(os.getcwd(), "build"))
        print("-"*55)
        print(print("Crawling your Files and Creating Zip Files "))
        print("-"*55)

        zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
        zipdir('python/', zipf)
        zipf.close()

        print('\n')
        print('-'*55)
        print("Deployment Package Created with Name Python.zip ")
        print('-'*55)
        print('\n')

    except Exception as e:
        print("Error  :{}  ".format(e))


if __name__ == "__main__":
    main()
