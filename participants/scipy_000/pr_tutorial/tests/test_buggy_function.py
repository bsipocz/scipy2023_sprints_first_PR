from pr_tutorial.buggy_function import angle_to_sexigesimal

def test_angle_to_sexigesimal_30():
    assert angle_to_sexigesimal(30) == "2:0:0.000"
