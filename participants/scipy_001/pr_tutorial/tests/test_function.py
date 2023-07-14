from pr_tutorial.buggy_function import angle_to_sexigesimal

def test_angle():
    sex = angle_to_sexigesimal(32.231515, decimals=3)
    assert sex == '04:17:51.127'

