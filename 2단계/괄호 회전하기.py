# 괄호 회전하기
#열린 기호가 먼저 나오고, 닫히는 기호가 나오는지 확인하여 ans에 1씩 더해줌

def solution(s):
    ans, pair = 0, {'{':'}', '[':']', '(':')'}
    for i in range(len(s)):
        iscorrect, stack = True, []
        for v in s:
            # 열린 기호가 나오면 stack에 추가함
            if v in ['{','[','(']: stack.append(v)
            # 스텍과 페어가 되는지 체크함
            elif not stack or v != pair[stack[-1]]: iscorrect = False
            # 위 조건을 충족한 경우 기호를 지워줌
            else: stack = stack[:-1]
        # iscorrect가 있으면서 stack이 있으면 ans를 추가해줌
        ans += int(iscorrect and not stack)
        s = s[1:]+s[0]

    return ans