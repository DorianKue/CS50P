from project import get_results, analyze_results, get_odds


def test_get_results():
    results = get_results(1)
    assert set(results) == {"Heads"} or set(results) == {"Tails"}
    
    results = get_results(4)
    assert len(results) == 4
    for result in results:
        assert result in ["Heads", "Tails"]


def test_get_odds():
    assert get_odds(1, 1) == 50.0
    assert get_odds(1, 0) == 50.0
    assert get_odds(9, 1) == 0.9765625
    assert get_odds(0, 0) == 0


def test_analyze_results():
    assert analyze_results(["Heads", "Tails"]) == (1, 50, 1, 50)
    assert analyze_results(["Heads", "Heads"]) == (2, 100, 0, 0)
    assert analyze_results(["Tails", "Tails"]) == (0, 0, 2, 100)
