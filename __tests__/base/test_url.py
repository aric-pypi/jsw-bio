import jsw_bio as bio


def test_url():
    assert bio.url('7EU9_A',
                   'fasta') == 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=7EU9_A&db=protein&retmode=text&report=fasta'

    assert bio.url('7EU9_A',
                   'gb') == 'https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id=7EU9_A&db=protein&retmode=text&report=gb'
