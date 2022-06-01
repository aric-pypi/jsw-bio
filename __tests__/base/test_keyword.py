import jsw_bio as bio


def test_keyword():
    assert bio.keyword('In vivo targeting of a variant causing vanishing white matter using CRISPR/Cas9') == [
        'crispr/cas9']
