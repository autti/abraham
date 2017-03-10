

def parse(frame):
    """
    Receives a string and returns id, data.
      frame: String input (e.g. 415#19E6D0F907FA07FA
)
    Output
    id (hex), data ([hex])
    """
    str_id, str_data = frame.split("#")

    assert len(str_data) == 16

    list_data = [str_data[0:2], str_data[2:4],
                 str_data[4:6], str_data[6:8],
                 str_data[8:10], str_data[10:12],
                 str_data[12:14], str_data[14:16]]

    data = [int(item, 16) for item in list_data]

    return int(str_id, 16), data
