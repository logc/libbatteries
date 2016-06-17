import os
env = Environment(ENV = {'PATH' : os.environ['PATH']})
env.ParseConfig('pkg-config check --cflags --libs')
env.SharedLibrary('batteries', Glob('src/*.c'))
env.Program('test_batteries', Glob('tests/test_*.c'),
            LIBS=(env['LIBS'] + ['batteries']),
            LIBPATH=(env['LIBPATH'] + ['.']))
