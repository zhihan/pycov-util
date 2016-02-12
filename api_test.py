import coverage
import tempfile

def myfun(x):
    if x:
        return True
    else:
        return False


def collect_coverage(data_file):
    cov = coverage.Coverage(data_file=data_file,
                            branch=True)
    cov.start()

    myfun(True)

    cov.stop()
    cov.html_report()
    cov.save()

def analyze_coverage(data_file):
    cov = coverage.Coverage(data_file=data_file,
                            branch=True)
    cov.load()
    cov.report(file=open('report.dat', 'w'))
    (filename, executed, excluded, missing, s) = cov.analysis2(__file__)
    print("Filename %s" % filename)
    print("Instrumented " + repr(executed))
    print("Excluded " + repr(excluded))
    print("Missing " + repr(missing))
    print("Last " + s)


def annotate_coverage(data_file):
    cov = coverage.Coverage(data_file=data_file,
                            branch=True)
    cov.load()
    cov.annotate()
    

    
if __name__ == "__main__":
    _, cov_dat = tempfile.mkstemp()
    
    collect_coverage(cov_dat)
    analyze_coverage(cov_dat)
    annotate_coverage(cov_dat)
