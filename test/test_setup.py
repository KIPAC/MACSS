import os
import macss

def test_setup(setup_data: int) -> None:
    assert setup_data == 0
    HOME = os.environ['HOME']
    data_dir = f"{HOME}/macss"
    print(f"The data have been succesfully downloaded and uncompressed, you can find them in {data_dir}")
    print("You can also ignore any errors from py.test")
    return
