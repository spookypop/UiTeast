def assertion_equal(actual, expect, case_description='用例', success_msg='成功', fail_msg='失败'):
    if actual == expect:
        print(case_description + '--' + success_msg)

    else:
        print(case_description + '--' + fail_msg)
