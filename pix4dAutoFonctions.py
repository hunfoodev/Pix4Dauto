import os

def write_pix4dBat_thermal(baseDir, template):
    """

    :param baseDir: base directory where a raw folder containing images is located
    :param template: name of the pix4d template used to define setttings
    :return: message
    """
    # get list of image folders of flights
    raw = os.listdir(baseDir + 'raw')

    # create file where automating project script will be
    file = open(baseDir + 'projectAuto.bat', 'w')

    # write to .bat file commands to run projects successively one after the other
    for fol in raw:

        # check if folder is not of thermal images
        # if project is not thermal, run with TELUQgeneral template
        ty = fol.split('-')[-1]
        if ty != 'thermal':
            file.write(
            '''echo RUNNING PROJECT ''' +ty.upper() + '''\n"C:\\Program Files\\Pix4Dmapper\\pix4dmapper" -c -n --image-dir "''' + fol + '''" --template ''' + template +''' "C:\\Users\\zdeziel\\Documents\\TELUQ\\missions\\thetford-20180713\\''' + fol +'''.p4d"\necho PROCESSING FINISHED\n\n'''
            )

        else:
            file.write(
            '''echo RUNNING INITIAL PROCESSING ''' + ty.upper() + '''\n"C:\\Program Files\\Pix4Dmapper\\pix4dmapper" -c --cam-param-project -i --image-dir "''' + fol + '''" --template ''' + template +''' "C:\\Users\\zdeziel\\Documents\\TELUQ\\missions\\thetford-20180713\\''' + fol + '''.p4d"\necho INITIAL PROCESSING FINISHED\n\n'''
            )

    # close file to save changes
    file.close()

    return 'Your projectAuto.bat file has been written.'


def write_pix4dBat(baseDir, template):
    """

    :param baseDir: base directory where a raw folder containing images is located
    :param template: name of the pix4d template used to define setttings
    :return: message
    """
    # get list of image folders of flights
    raw = os.listdir(baseDir + 'raw')

    # create file where automating project script will be
    file = open(baseDir + 'projectAuto.bat', 'w')

    # write to .bat file commands to run projects successively one after the other
    for fol in raw:
        
        ty = fol.split('-')[-1]
        file.write(
            '''echo RUNNING PROJECT ''' + ty.upper() + '''\n"C:\\Program Files\\Pix4Dmapper\\pix4dmapper" -c -n --image-dir "''' + fol + '''" --template ''' + template + ''' "C:\\Users\\zdeziel\\Documents\\TELUQ\\missions\\thetford-20180713\\''' + fol + '''.p4d"\necho PROCESSING FINISHED\n\n'''
        )

    # close file to save changes
    file.close()

    return 'Your projectAuto.bat file has been written.'
