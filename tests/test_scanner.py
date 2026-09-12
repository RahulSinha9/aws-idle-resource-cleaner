from src.scanner import ResourceFinding, is_low_utilization, rank_findings

def test_low_utilization():
    assert is_low_utilization(2.4)
    assert not is_low_utilization(7.1)

def test_rank():
    items = [
        ResourceFinding("a","ebs","unused",.8,10),
        ResourceFinding("b","eip","unused",.9,5),
    ]
    assert rank_findings(items)[0].resource_id == "b"
