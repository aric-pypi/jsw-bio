import pkg_resources

version = pkg_resources.get_distribution('jsw-bio').version
__version__ = version

# next base
from jsw_bio.base.url import url
from jsw_bio.base.keyword import keyword
from jsw_bio.ncbi.download_accids import download_accids
