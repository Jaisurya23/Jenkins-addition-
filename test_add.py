from add import add
def test_add():
    assert add(2, 3) == "The sum of 2 and 3 is 5."
    assert add(-1, 1) == "The sum of -1 and 1 is 0."
    assert add(0, 0) == "The sum of 0 and 0 is 0."
    assert add(100, 200) == "The sum of 100 and 200 is 300."
    assert add(-5, -5) == "The sum of -5 and -5 is -10."
    print("All tests passed!")  # This line is for demonstration purposes only
if __name__ == "__main__":
    test_add()  # Run the tests when this script is executed directly