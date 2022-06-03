import jsw_bio as bio
import jsw_nx as nx


def test_ncbi_gb_tet():

    # the 28 records
    res = bio.ncbi_gb_text(id='EU490707.1')
