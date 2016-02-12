import coverage


class MyTracer(coverage.FileTracer):
    def __init__(self, filename):
        print('Init MyTracer for %s' % filename)
        super().__init__()
        self.filename = filename

    def source_filename(self):
        return self.filename

class MyReporter(coverage.FileReporter):
    def __init__(self, filename):
        print('Init MyReporter for %s' % filename)
        self.filename = filename
        super().__init__(filename)
        
    def lines(self):
        return set()


class MyPlugin(coverage.CoveragePlugin):
    def file_tracer(self, filename):
        return MyTracer(filename)

    def file_reporter(self, filename):
        return MyReporter(filename)
    
def coverage_init(reg, options):
    reg.add_file_tracer(MyPlugin())
    
    
def myfun(x):
    if x:
        return True
    else:
        return False

def collect_coverage(data_file):
    cov = coverage.Coverage(data_file=data_file,
                            config_file="coveragerc")
    cov.start()
    myfun(False)
    cov.stop()
    cov.save()

    x = cov.analysis2(__file__)
    print ("Result is " + str(x))
    
if __name__ == "__main__":
    cov_dat = "coverage.dat"
    collect_coverage(cov_dat)
