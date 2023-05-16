# ��ȣ ȸ���ϱ�
#���� ��ȣ�� ���� ������, ������ ��ȣ�� �������� Ȯ���Ͽ� ans�� 1�� ������

def solution(s):
    ans, pair = 0, {'{':'}', '[':']', '(':')'}
    for i in range(len(s)):
        iscorrect, stack = True, []
        for v in s:
            # ���� ��ȣ�� ������ stack�� �߰���
            if v in ['{','[','(']: stack.append(v)
            # ���ذ� �� �Ǵ��� üũ��
            elif not stack or v != pair[stack[-1]]: iscorrect = False
            # �� ������ ������ ��� ��ȣ�� ������
            else: stack = stack[:-1]
        # iscorrect�� �����鼭 stack�� ������ ans�� �߰�����
        ans += int(iscorrect and not stack)
        s = s[1:]+s[0]

    return ans