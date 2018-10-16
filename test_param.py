import sys, getopt, os

def main(argv):
    command = ''
    try:
      opts, args = getopt.getopt(argv,"hc:d:",["command=","directory="])
    except getopt.GetoptError:
      print 'test.py -c <command> -d <directory>'
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
        print 'test.py -c <command> -d <directory>'
        sys.exit()
      elif opt in ("-c", "--command"):
        command = arg
      elif opt in ("-d", "--directory"):
        directory = arg
        command = command + " " + directory
    print os.system(command)

if __name__ == "__main__":
    main(sys.argv[1:])
