from abraham import parse

def test_parse():
    can_id = 0x415
    data = [25, 230, 208, 249, 7, 250, 7, 250]
    frame = "415#19E6D0F907FA07FA"

    parsed_can_id, parsed_data = parse(frame)

    assert parsed_can_id == can_id

    assert parsed_data == data

