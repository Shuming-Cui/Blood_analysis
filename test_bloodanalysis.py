def test_HDL_analysis():
    from bloodanalysis import HDL_analysis
    answer = HDL_analysis(80)
    expected = "Normal"
    assert answer == expected


def test_HDL_analysis_bl():
    from bloodanalysis import HDL_analysis
    answer = HDL_analysis(40)
    expected = "Borderline low"
    assert answer == expected


def test_HDL_analysis_l():
    from bloodanalysis import HDL_analysis
    answer = HDL_analysis(20)
    expected = "Low"
    assert answer == expected


def test_LDL_analysis():
    from bloodanalysis import LDL_analysis
    answer = LDL_analysis(100)
    expected = "Normal"
    assert answer == expected
