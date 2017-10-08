import os.path
import jsonpickle


def json_write(test_data, file_name):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/%s.json" % file_name)

    with open(file, "w") as out:
        jsonpickle.set_encoder_options("json", indent=2)
        out.write(jsonpickle.encode(test_data))