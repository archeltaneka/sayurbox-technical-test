class UnitTest():
    
    def assert_positive_non_zero_k(k):
        
        assert k > 0, 'The number of elements in array (k) must be greater than 0'
    
    def assert_positive_non_zero_n(n):
        
        assert n > 0, 'n must be greater than 0'
    
    def case_1(arr, n):
        
        assert len(arr) >= n, 'The number of input array must be greater than or equal to n'
        
    def case_2(arr, n):
        
        unique = []
        for num in arr:
            if num not in unique:
                unique.append(num)
                
        assert len(unique) >= n, 'The number of n requested is greater than the number of unique elements in the input array'