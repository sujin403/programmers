# dfs�� ��͸� �����
# idx �� curr�� 0���� �����ϰ� dfs��͸� ��
def solution(numbers, target):
    idx = curr = 0

    def dfs(nums, target, curr, idx):
        # ��� �񱳴� �������� �ε����� ������ ���� �� ��
        if idx == len(nums):
            return 1 if curr == target else 0

        # idx�� ��ĭ �������ְ� curr�� �̹� ���� ���ϰų� ����
        return dfs(nums, target, curr + nums[idx], idx + 1) \
                + dfs(nums, target, curr - nums[idx], idx + 1)

    answer = dfs(numbers, target, idx, curr)
    return answer
