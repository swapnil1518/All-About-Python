import pytest

from Learnings.age import validate_age


def test_validate_age_valid_age():
    validate_age(10)

def test_validate_age_invalid_agee():
    with pytest.raises(ValueError, match="Age can't be less than 0"):
        validate_age(-1)
        



def test_validate_age_invalid_age():
    with pytest.raises(ValueError) as exc_info:         # exc_info means expected info
        validate_age(-1)                                # this function gives error. this is expected error
    assert (str(exc_info.value)) == "Age can't be less than 0"
    # this print s the exact msg along with testcase
    # either write 1. assert (str(exc_info.value))  == "Age can't be less than 0"  OR write
    # 2. print(str(exc_info.value))
    # 3. another way without creating exc_info. is with pytest.raises(ValueError), match ="Age can't be less than 0"

"""
with pytest.raises(ValueError): this function will protect the below function to give error
 in o/p it will try to avoid the expected error.
If we give a valid age no in the function with valueerror function above it will give error 
 in o/p that E       Failed: DID NOT RAISE <class 'ValueError'> 
"""