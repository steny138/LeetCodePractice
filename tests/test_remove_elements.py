from problems.remove_elements import Solution

class Test27:

    def test_ex1(self):

        executer = Solution()
        nums = [3,2,2,3]
        
        actual = executer.removeElement(nums, 3)

        assert nums == [2, 2]