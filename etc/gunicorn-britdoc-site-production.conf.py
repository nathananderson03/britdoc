import os

# from example config at http://gunicorn.org/configure.html

def numCPUs():
    if not hasattr(os, "sysconf"):
        raise RuntimeError("No sysconf detected.")
    return os.sysconf("SC_NPROCESSORS_ONLN")

bind = "127.0.0.1:8051"  # note that this linesup with nginx-britdoc-site-production.conf
workers = numCPUs() * 2 + 1
