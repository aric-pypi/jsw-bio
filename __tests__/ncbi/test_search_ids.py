import jsw_bio as bio
import jsw_nx as nx


def test_ncbi_search_ids():
    # the 28 records
    res = bio.ncbi_search_ids(term="cas12")

    assert nx.type(res) == 'list'
    assert len(res) > 0
