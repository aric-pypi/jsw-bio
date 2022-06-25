import jsw_bio as bio
import jsw_nx as nx


def test_ncbi_ipg_test():
    # the 28 records
    instance = bio.NcbiIpgSearch(term='CRISPR-associated')
    res = instance.get(1)
    assert (len(res)) == 20
    res2 = instance.get(1, size=200)
    assert len(res2) == 200
