from features.utils.main import validate_email


# def test_correct_email_is_valid():
    
#     emails = [
#         "john.doe@example.com",
#         "aaaaaa.com@",
#         "test@domain.",
#         "test@domian",
#         "test@domaincom.",
#         "test@domain.com.",
#         "test@domain.com_",
#         "_@domain.com_"
#     ]

#     first = validate_email()
#     second = validate_email()
#     third = validate_email("@aaaaaa.com")
#     third = validate_email("@aaaaaa.com")
#     third = validate_email("@aaaaaa.com")
#     third = validate_email("@aaaaaa.com")

#     assert first == True
#     assert second == False
#     assert third == False

# # def test_wrong_email_isnt_valid():
    
#     result = validate_email(CORRECT)

#     assert result == False