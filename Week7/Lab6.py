# Lab6
# Author:


## add in functions from test.py's test statements here to make the pytest work

def calculate_rectangle_area(length, width):
    return length * width

def main():
    def test_rectangle_area():
        assert calculate_rectangle_area(3, 4) == 12
        assert calculate_rectangle_area(5, 5) == 25
        assert calculate_rectangle_area(0, 0) == 0
        assert calculate_rectangle_area(10, 20) == 200

    test_rectangle_area()

if __name__ == "__main__":
    main()
