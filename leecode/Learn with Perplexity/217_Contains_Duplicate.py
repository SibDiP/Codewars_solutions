"""
LeetCode #217: Contains Duplicate

Link: https://leetcode.com/problems/contains-duplicate/
Date: 2026-01-22
Difficulty: Easy
Category: Arrays & Hashing

Problem Description:
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Examples:
    Input: nums = [1,2,3,1]
    Output: true
    
    Input: nums = [1,2,3,4]
    Output: false
    
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Key Concepts:
    - Big O notation: importance of understanding time complexity growth
    - Trade-off: time vs space complexity
    - Hash table (set) lookup is O(1), not O(n)
    - Choosing right data structure matters for optimization
    
Big O Analysis:
    - Brute Force: O(n²) time, O(1) space
    - Set Comparison: O(n) time, O(n) space
    - Set with Loop: O(n) time, O(n) space
    
Important Notes:
    - `in` operator for list is O(n), for set is O(1)
    - Constants are ignored in Big O notation
    - Always consider worst-case scenario when analyzing
"""

# ============================================================================
# SOLUTION 1: BRUTE FORCE (O(n²) time, O(1) space)
# ============================================================================

class Solution_BruteForce:
    """
    Two nested loops comparing each element with all elements that come after it.
    
    Time Complexity: O(n²)
        - Outer loop: n iterations
        - Inner loop: n iterations (worst case)
        - Total: n * n = n²
    
    Space Complexity: O(1)
        - Only using variables i, j (no extra data structures)
    
    Why O(n²)?
        - We have nested loops where both depend on input size n
        - In worst case (no duplicates), we compare all pairs
        - For n=1000: 1,000,000 comparisons
        - For n=10,000: 100,000,000 comparisons
    
    Worst Case: array with all unique elements [1,2,3,4,...,n]
    Best Case: duplicates found at beginning, early return
    """
    
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_len = len(nums)
        
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                # We start j at i+1 to avoid:
                # 1. Comparing element with itself
                # 2. Comparing same pairs twice
                if nums[i] == nums[j]:
                    return True
        
        return False


# ============================================================================
# SOLUTION 2: SET COMPARISON - LENGTH CHECK (O(n) time, O(n) space)
# ============================================================================

class Solution_SetComparison:
    """
    Convert list to set (removes duplicates) and compare lengths.
    If set is smaller, duplicates existed.
    
    Time Complexity: O(n)
        - set(nums): O(n) to create set from list
        - len(): O(1) to compare lengths
        - Total: O(n)
    
    Space Complexity: O(n)
        - set_nums stores up to n elements
    
    Why O(n)?
        - Single pass through the list to create set
        - Set creation uses hash table internally
        - Comparison is instant
    
    Pros: Simple, elegant
    Cons: Creates full set even if duplicate found early
    """
    
    def containsDuplicate(self, nums: list[int]) -> bool:
        set_nums = set(nums)  # O(n) operation
        return len(set_nums) < len(nums)  # O(1) comparison


# ============================================================================
# SOLUTION 3: SET WITH LOOP - OPTIMAL (O(n) time, O(n) space)
# ============================================================================

class Solution_SetWithLoop:
    """
    Iterate through list, check if element is in set (O(1)),
    return True immediately on first duplicate found.
    
    Time Complexity: O(n)
        - for loop: n iterations
        - if num in set_nums: O(1) hash table lookup
        - set_nums.add(num): O(1) insertion
        - Tело цикла: O(1)
        - Total: n * O(1) = O(n)
    
    Space Complexity: O(n)
        - set_nums can store up to n elements
    
    Why O(n) NOT O(n²)?
        - CRITICAL: `in` operator for set is O(1), NOT O(n)!
        - `in` for list would be O(n), making this O(n²)
        - Hash table provides constant time lookup
    
    Pros: Optimal time complexity, early exit on first duplicate
    Cons: Uses extra space O(n)
    
    Key Difference from Brute Force:
        - Brute: nested loops → O(n²)
        - Optimal: single loop with O(1) lookups → O(n)
    """
    
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        
        for num in nums:  # n iterations
            if num in seen:  # O(1) - hash table lookup
                return True  # Early exit when duplicate found
            seen.add(num)  # O(1) - add to hash table
        
        return False


# ============================================================================
# BIG O COMPLEXITY COMPARISON
# ============================================================================

"""
Data Growth Analysis:

n=10:
    - Brute Force: 100 operations (10²)
    - Set Comparison: 10 operations (10)
    - Set with Loop: 10 operations (10)

n=100:
    - Brute Force: 10,000 operations (100²)
    - Set Comparison: 100 operations (100)
    - Set with Loop: 100 operations (100)

n=1,000:
    - Brute Force: 1,000,000 operations (1000²)
    - Set Comparison: 1,000 operations (1000)
    - Set with Loop: 1,000 operations (1000)

n=10,000:
    - Brute Force: 100,000,000 operations (10000²)
    - Set Comparison: 10,000 operations (10000)
    - Set with Loop: 10,000 operations (10000)

Key Insight: As n grows, brute force becomes exponentially slower!
This is why interviewers ask for optimization.
"""


# ============================================================================
# IMPORTANT CONCEPTS
# ============================================================================

"""
1. WHY CONSTANTS DON'T MATTER IN BIG O:
   - O(1) + O(1) + O(1) = O(1) (not O(3))
   - O(n) + O(n) = O(n) (not O(2n))
   - Because at large n, constants become negligible
   
   Example: 2n + 1000000
   At n = 10,000,000: this ≈ 2n anyway
   
2. DOMINATION IN BIG O:
   - O(n) + O(n²) = O(n²) (quadratic dominates)
   - O(1) + O(n) = O(n) (linear dominates)
   - We always take the worst/largest complexity
   
3. DATA STRUCTURE MATTERS:
   
   Operation:    List     Set      Dict
   x in items    O(n)     O(1)     O(1)    ← BIG DIFFERENCE!
   items.add()   N/A      O(1)     N/A
   append()      O(1)*    N/A      N/A
   
   * amortized O(1)
   
4. HOW TO COUNT COMPLEXITY:
   Step 1: Find all loops (for, while, recursion)
   Step 2: Count iterations for each loop
   Step 3: Count operations inside loop body
   Step 4: Multiply: iterations * body_complexity
   Step 5: Take maximum if multiple loops/sections
   
   Formula: Σ(iterations × body_complexity) = Total
"""


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),
        ([1, 2], False),
        ([99, 99], True),
    ]
    
    solutions = [
        ("Brute Force O(n²)", Solution_BruteForce()),
        ("Set Comparison O(n)", Solution_SetComparison()),
        ("Set with Loop O(n)", Solution_SetWithLoop()),
    ]
    
    print("Testing all solutions:\n")
    
    for sol_name, solution in solutions:
        print(f"--- {sol_name} ---")
        all_pass = True
        
        for nums, expected in test_cases:
            result = solution.containsDuplicate(nums)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_pass = False
            
            print(f"{status} nums={nums} → {result} (expected {expected})")
        
        print(f"Result: {'ALL PASS' if all_pass else 'FAILED'}\n")