class Log:
    def write_log(msg):
        with open('log_file', 'a+') as log_file:
            log_file.write(msg + '\n')
