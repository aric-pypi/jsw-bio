import jsw_bio as bio
import jsw_nx as nx


def test_download_accids():

    # the 28 records
    res1 = bio.ncbi_download_accids(term='cas12')

    # not exist
    res2 = bio.ncbi_download_accids(term='cas12xxxxxxx')

    assert len(res1) > 0
    assert len(res2) == 0
