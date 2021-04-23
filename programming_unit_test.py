class UnitTest():
    
    def assert_positive_non_zero_k(k):
        """
        Assert k (length of the input array) is a positive integer
        """
        assert k > 0, 'The number of elements in array (k) must be greater than 0'
    
    def assert_positive_non_zero_n(n):
        """
        Assert n (most frequent numbers to show) is a positive integer
        """
        assert n > 0, 'n must be greater than 0'
          
    def assert_unique_numbers_and_n(arr, n):
        """
        Assert length of the unique numbers in the input array is greater than n

        Failed test case example: 
        k = 5
        arr = [3,3,2,2,1]
        n = 4

        The example above will raise an error because there are only 3 numbers taken into account while n = 4.
        """
        unique = []
        for num in arr:
            if num not in unique:
                unique.append(num)
                
        assert len(unique) >= n, 'The number of n requested is greater than the number of unique elements in the input array'