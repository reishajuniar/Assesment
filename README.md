# Assesment
Test assesment

Please run TestOrderFunction.py and TestSearchFunction.py to see the test results.

To verify the test cases:
* test_search_with_invalid_data: it should be successful if the page resource contains ‘No result were found’. This test case will be failed if the page resource doesn’t contains the expected message.
* test_search_with_valid_data: it should be successful if the page resource doesn’t contains ‘No result were found’.  This test case will be failed if the page resource contains the expected message.
* test_login_with_valid_data: it should be successful if the page resource doesn’t contains ‘Welcome to your account’. This test case will be failed if the page resource contains error for invalid account.
* test_login_with_invalid_data: it should be successful if the page resource contains ‘Invalid password’. This test case will be failed if the page resource doesn’t contains the expected message.
* test_order_single_product: it should be successfully if the test passed several process:
    * Product is successfully added. The page source will contains message ‘Product successfully added’.
    * Total of the quantity in cart summary equal with 1.
    * Pass the checkout process from step 1 until the end process.
    * Page source will contain ‘Your order on My Store is complete.’ if the process is successful.
	This test cases will be failed if one of the process is failed
	or the result is not as the expected
* test_order_multiple_products:
    * Product is successfully added. The page source will contains message ‘Product successfully added’.
    * Total of the quantity in cart summary equal with 3.
    * Pass the checkout process from step 1 until the end process.
    * Page source will contain ‘Your order on My Store is complete.’ if the process is successful.
	This test cases will be failed if one of the process is failed
	or the result is not as the expected
