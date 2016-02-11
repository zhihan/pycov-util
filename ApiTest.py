import coverage

def myfun(x):
    if x:
        return True
    else:
        return False


def collect_coverage():
    cov = coverage.Coverage(data_file="mycoverage.dat",
                            branch=True)
    cov.start()

    myfun(True)

    cov.stop()
    cov.html_report()
    cov.save()

def analyze_coverage():
    cov = coverage.Coverage(data_file="mycoverage.dat",
                            branch=True)
    cov.load()
    cov.report(file=open('report.dat', 'w'))
    (filename, executed, excluded, missing, s) = cov.analysis2(__file__)
    print("Filename %s" % filename)
    print("Instrumented " + repr(executed))
    print("Excluded " + repr(excluded))
    print("Missing " + repr(missing))
    print("Last " + s)

if __name__ == "__main__":
    collect_coverage()
    analyze_coverage()
