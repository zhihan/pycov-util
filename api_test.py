import coverage
import tempfile
from coverage import files

def myfun(x):
    if x:
        a = 1 + 2
        return a
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
    

def display_arcs(data_file):
    cov = coverage.Coverage(data_file=data_file,
                            branch=True)
    cov.load()
    covdata = cov.get_data()
    print("Has ars: %d" % covdata.has_arcs())
    cf = files.canonical_filename(__file__)
    print("Executed Arcs: " + str(covdata.arcs(cf)))
    
if __name__ == "__main__":
    _, cov_dat = tempfile.mkstemp()
    print("Temp file %s" % cov_dat)
    
    collect_coverage(cov_dat)
    analyze_coverage(cov_dat)
    annotate_coverage(cov_dat)
    display_arcs(cov_dat)
          
