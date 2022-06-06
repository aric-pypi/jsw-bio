import jsw_bio as bio
import jsw_nx as nx


def test_ncbi_fasta_text():
    # the 28 records
    res1 = bio.ncbi_fasta_text(id='EU490707.1')
    res2 = bio.ncbi_fasta_text(id='EU490707.1', serialize=True)

    assert nx.includes(res1, '\n') == True
    assert nx.includes(res1, '>') == True
    assert nx.includes(res2, '\n') == False
    assert len(res2) == 1302
